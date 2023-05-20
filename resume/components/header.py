import pynecone as pc
from resume.state import nav_content, State
from pcconfig import style_config

nav_links = [pc.link(name, href=f"/#{name}") for name in nav_content]


def header() -> pc.Component:
    return pc.box(
        pc.flex(
            pc.text("Pritam Dey", style={"pl": "40px", "font_size": "1.2em"}),
            pc.spacer(),
            pc.hstack(
                *nav_links,
                display=["none", "none", "flex", "flex", "flex"],
                style={"pr": "20px"},
            ),
            pc.box(
                pc.icon(tag="chevron_down", box_size=8),
                display=["flex", "flex", "none", "none", "none"],
                on_click=State.toggle_drawer,
            ),
            style={"align_items": "center", "h": "100%"},
        ),
        style={
            "width": "100%",
            "height": style_config["header_height"],
            "border_bottom": "1px solid",
        },
    )
