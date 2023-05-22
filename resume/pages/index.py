import pynecone as pc
from resume.components.header import header
from resume.components.sidebar import sidebar
from resume.components.drawer import drawer
from resume.pages.sections.cover import section as cover
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
    return pc.vstack(
        cover(),
        *[f() for f, md in get_sections()],
        style={
            "overflowY": "auto",
            "m": "15px 21px !important",
            "height": f"calc(100vh - {style_config['header_height']} - 15px - 15px)",
            "width": f"calc(100vw - {style_config['sidebar_width']} - 42px)",
        },
        align_items="flex-start",
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
