"""Welcome to Pynecone! This file outlines the steps to create a basic app."""
from resume.pages.index import index
from resume.state import State


import pynecone as pc

# Add state and page to the app.
app = pc.App(
    state=State,
    stylesheets=[
        "styles.css",  # This path is relative to assets/
    ],
)
app.add_page(index)
app.compile()
