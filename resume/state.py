import pynecone as pc
from pathlib import Path
import json


sections_path = Path("resume/pages/sections")

with open(sections_path / "metadata.json") as f:
    all_meta: list[dict[str, str]] = json.load(f)
# sort metadatas based on rank
all_meta = sorted(all_meta, key=lambda x: x["rank"])

nav_content = ("Kavya", "Notes", "CV")


class State(pc.State):
    body_txt: str
    drawer_is_open: bool = False

    def __init__(self):
        super().__init__()

    def toggle_drawer(self) -> None:
        self.drawer_is_open = not self.drawer_is_open
