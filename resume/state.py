import pynecone as pc


nav_content = ("Kavya", "Notes", "CV")

sidebar_content = (
    "Home",
    "About",
    "Services",
    "Blog",
    "Portfolio",
    "Contact",
    "Settings",
)

class State(pc.State):
    body_txt: str
    drawer_is_open: bool = False

    def __init__(self):
        super().__init__()

    def toggle_drawer(self) -> None:
        self.drawer_is_open = not self.drawer_is_open

