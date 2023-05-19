import pynecone as pc
from resume.state import nav_content, sidebar_content
from resume.state import State
from typing import Set

sidebar_links = [pc.link(name, href=f"/#{name}") for name in sidebar_content]
nav_links = [pc.link(name, href=f"/#{name}") for name in nav_content]


class Collapse(pc.Component):
    library = "@mantine/core"
    tag = "Collapse"

    # variables
    in_: pc.Var[bool]  # type: ignore
    animate_opacity: pc.Var[bool]  # type: ignore
    transition_duration: pc.Var[int]  # type: ignore

    @classmethod
    def get_triggers(cls) -> Set[str]:
        """Get the event triggers for the component.

        Returns:
            The event triggers.
        """
        return super().get_triggers()



collapse = Collapse.create


def drawer_() -> pc.Component:
    return pc.drawer(
        pc.drawer_content(
            pc.drawer_body(
                pc.vstack(*nav_links, on_click=State.toggle_drawer),
                pc.markdown("------"),
                pc.vstack(*sidebar_links, on_click=State.toggle_drawer),
            )
        ),
        is_open=State.drawer_is_open,
        placement="left",
        get_container=False,
        on_close=State.toggle_drawer,
        closable=False,
        style={"position": "absolute !important"},
    )


def drawer_content() -> pc.Component:
    return pc.vstack(*nav_links,
        pc.divider(border_color="black"),*sidebar_links, on_click=State.toggle_drawer,
        style={
                "bg": "#efe3ca",
                "width": "100%",
                "height": "calc(80vh - 60px)"
               })


def drawer() -> pc.Component:
    return pc.box(
        collapse(drawer_content(),
        in_=State.drawer_is_open,
        on_click=State.toggle_drawer,
        on_blur=State.toggle_drawer,
        animate_opacity=False,
        transition_duration=1000,
        style={"height": "calc(80vh - 60px)"}
    ),
        style={"position": "absolute",
               "top": 0,
               "left": 0,
               "width": "100%"}
    )
