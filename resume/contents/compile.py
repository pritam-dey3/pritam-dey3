from resume.contents.document import Document
from resume.contents.renderer import PyneconeMarkdown
from mistune import create_markdown
import black
from pathlib import Path
import json


root_folder = Path("resume/")
sections_folder = root_folder / "contents" / "sections"
target_folder = root_folder / "pages" / "sections"
markdown = create_markdown(renderer=PyneconeMarkdown())


def transform_file(file: Path) -> tuple[str, dict[str, str]]:
    doc = Document(file, markdown)
    body = black.format_str(doc.body, mode=black.FileMode())
    return body, doc.metadata


def compile() -> None:
    all_meta = []
    for file in sections_folder.glob("*.md"):
        try:
            code, metadata = transform_file(file)

            # add module path to metadata
            target_filename = target_folder / (file.stem + ".py")
            metadata["module_path"] = str(target_filename.resolve())
            all_meta.append(metadata)

            # write code at the target folder
            with open(target_filename, "w+") as f:
                f.write(code)

            print(f"{file.name} is transformed.")

        except black.InvalidInput:
            print(f"error parsing {file.name}.")

    with open(target_folder / "metadata.json", "w+") as f:
        json.dump(all_meta, f)
