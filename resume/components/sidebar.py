import pynecone as pc
from resume.state import all_meta
from pcconfig import style_config


sidebar_links = [
    pc.box(
        pc.link(meta["title"], href=f"/#{meta['slug']}"),
        min_h="39px",
        align_items="center",
        class_name="list-group-item",
        style={"m": "0px !important", "display": "flex", "px": "21px", "width": "100%"},
    )
    for meta in all_meta
]


def sidebar() -> pc.Component:
    return pc.box(
        pc.vstack(*sidebar_links, style={"align_items": "flex_start", "width": "100%"}),
        style={
            "w": style_config["sidebar_width"],
            "h": f"calc(100vh - {style_config['header_height']})",
            "m": "0px !important",
            # "position": "absolute",
            # "top": "0px",
            # "left": "0px"
        },
        display=["none", "none", "flex", "flex", "flex"],
        id="sections",
    )
