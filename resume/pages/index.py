import pynecone as pc
from resume.components.header import header
from resume.components.sidebar import sidebar
from resume.components.drawer import drawer
import importlib
import re
from resume.state import all_meta
from pcconfig import style_config


def get_sections():
    section_functions = []
    for file_meta in all_meta:
        # Import the module dynamically
        module_path = file_meta["module_path"]
        module_name = re.search(r"[^/\\]*?(?=\.[^.]+$|$)", module_path).group()
        spec = importlib.util.spec_from_file_location(module_name, module_path)
        if not spec:
            print(f"{module_path} not found")
            continue
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)

        # Check if the module has a 'section' function
        if hasattr(module, "section"):
            # Retrieve the 'section' function from the module
            func = getattr(module, "section")
            section_functions.append((func, file_meta))

    return section_functions


def body() -> pc.Component:
    return pc.box(
        *[f() for f, md in get_sections()],
        style={
            "overflowY": "auto",
            "m": "15px 0px !important",
            "height": "calc(100vh - 60px - 15px - 15px)",
            "width": f"calc(100vw - {style_config['sidebar_width']})",
            "px": "21px",
        },
    )


def index() -> pc.Component:
    return pc.vstack(
        header(),
        pc.hstack(
            drawer(),
            sidebar(),
            body(),
            style={
                "spacing": 0,
                "m": "0px !important",
                "position": "relative",
            },
        ),
    )
