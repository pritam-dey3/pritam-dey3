from resume.contents.document import Document
from resume.contents.renderer import PyneconeMarkdown
from mistune import create_markdown
import black
from pathlib import Path
from glob import glob


root_folder = Path("resume/")
sections_folder = root_folder / "contents" / "sections"
target_folder = root_folder / "pages" / "sections"
markdown = create_markdown(renderer=PyneconeMarkdown())


def transform_file(file: Path) -> str:
    doc = Document(file, markdown)
    body = black.format_str(doc.body, mode=black.FileMode())
    return body


def compile() -> None:
    for file in sections_folder.glob("*.md"):
        try:
            code = transform_file(file)
            with open(target_folder / (file.stem + ".py"), "w+") as f:
                f.write(code)

            print(f"{file.name} is transformed.")

        except black.InvalidInput as e:
            print(f"error parsing {file.name}.")
