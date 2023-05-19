from mistune import Markdown
import re
import yaml
from pathlib import Path


class Document:
    def __init__(self, path: str | Path, markdown: Markdown) -> None:
        self.path = path
        self.raw: str
        self.body: str
        self.metadata: dict[str, str] = {}
        self.markdown = markdown

        self.process()

    def load(self) -> None:
        with open(self.path, "r") as f:
            self.raw = f.read()

    def extract(self) -> None:
        pattern = r"-+\n(.*?)\n-+"
        match = re.search(pattern, self.raw, re.DOTALL)

        if not match:
            self.body = self.markdown(self.raw)
            return

        index = match.end()

        self.body = self.markdown(self.raw[index:])

        metatext = self.raw[:index]
        self.metadata = yaml.safe_load(re.sub(r"-+", "", metatext))

        return

    def add_metadata(self):
        self.metadata["path"] = self.path

    def process(self):
        self.load()
        self.extract()
        self.add_metadata()
