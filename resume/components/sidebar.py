import pynecone as pc
from resume.state import sidebar_content

sidebar_links = [pc.link(name, href=f"/#{name}", class_name="list-group-item") for name in sidebar_content]

def sidebar() -> pc.Component:
    return pc.box(
        pc.vstack(*sidebar_links, style={
            "align_items": "flex_start"}),
        style={"w": "15vw",
               "h": "calc(100vh - 64px)",
               "m": "0px !important",
               "p": "21px"},
        display=["none", "none", "flex", "flex", "flex"],
    )
