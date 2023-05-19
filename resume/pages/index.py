import pynecone as pc
from resume.components.header import header
from resume.components.sidebar import sidebar
from resume.components.drawer import drawer
from resume.pages.sections.academic_achievements import section
import importlib
from pathlib import Path

sections_path = Path("resume/pages/sections")
section_functions = []

for file_path in sections_path.glob('*.py'):
    # Import the module dynamically
    module_name = file_path.stem
    module_path = str(file_path.resolve())
    spec = importlib.util.spec_from_file_location(module_name, module_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)

    # Check if the module has a 'section' function
    if hasattr(module, 'section'):
        # Retrieve the 'section' function from the module
        func = getattr(module, 'section')
        section_functions.append(func)


def body() -> pc.Component:
    return pc.box(
        *[f() for f in section_functions],
        style={
            "overflowY": "auto",
            "m": "15px 0px !important",
            "height": "calc(100vh - 60px - 15px - 15px)",
            "width": "85vw",
            # "m": "0px !important",
        },
    )


def index() -> pc.Component:
    return pc.vstack(
        header(),
        pc.hstack(
            drawer(), sidebar(), body(),
            style={
                "spacing": 0,
                "m": "0px !important",
                "position": "relative"}
        ),
    )
