from mistune.renderers.markdown import MarkdownRenderer
from mistune.core import BlockState
from typing import Any, Dict
import black


class PyneconeMarkdown(MarkdownRenderer):
    text_tmpl = "pc.text('''{raw}'''{props}), "
    block_tmpl = "pc.box({children}{props}), "
    paragraph_tmpl = "pc.vstack({children}{props}), "
    heading_tmpl = "pc.heading({children}{props}), "
    list_tmpl = "pc.list({children}{props}), "
    list_item_tmpl = "pc.list_item({children}{props}), "
    link_tmpl = "pc.link({children}{props}), "
    output_tmpl = "import pynecone as pc\ndef section()->pc.Component:\n\treturn pc.vstack({children}{props})"

    def __call__(self, tokens, state: BlockState):
        body = self.render_tokens(tokens, state)
        body = self.output_tmpl.format(
            children=body, props="class_name='section', align_items='flex-start'"
        )
        return black.format_str(body, mode=black.FileMode())

    def text(self, token: dict[str, Any], state: BlockState) -> str:
        return self.text_tmpl.format(raw=token["raw"], props="")

    def block_text(self, token: dict[str, Any], state: BlockState) -> str:
        if "children" in token:
            if len(token["children"]) == 1:
                return self.render_children(token, state)
        return self.block_tmpl.format(
            children=self.render_children(token, state), props=""
        )

    def paragraph(self, token: Dict[str, Any], state: BlockState) -> str:
        if "children" in token:
            if len(token["children"]) == 1:
                return self.render_children(token, state)
        return self.paragraph_tmpl.format(
            children=self.render_children(token, state), props=""
        )

    def heading(self, token: Dict[str, Any], state: BlockState) -> str:
        level = token["attrs"]["level"]
        size = {1: "xxl", 2: "xl", 3: "lg", 4: "md", 5: "sm"}[level]
        return self.heading_tmpl.format(
            children=self.render_children(token, state), props=f"class_name='{size}'"
        )

    def list(self, token: Dict[str, Any], state: BlockState) -> str:
        ordered = token["attrs"]["ordered"]
        return self.list_tmpl.format(
            children=self.render_children(token, state), props=""
        )

    def list_item(self, token: Dict[str, Any], state: BlockState) -> str:
        return self.list_item_tmpl.format(
            children=self.render_children(token, state), props=""
        )

    def link(self, token: Dict[str, Any], state: BlockState) -> str:
        label = token.get("label")
        text = self.render_children(token, state)
        attrs = token["attrs"]
        url = attrs["url"]
        title = attrs.get("title")
        return self.link_tmpl.format(children=text, props=f"href='{url}', ")
