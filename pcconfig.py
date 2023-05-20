import pynecone as pc

class ResumeConfig(pc.Config):
    pass

config = ResumeConfig(
    app_name="resume",
    db_url="sqlite:///pynecone.db",
    env=pc.Env.DEV,
    frontend_packages=[
        "@mantine/core",
        "@mantine/hooks"
    ]
)


style_config = {
    "sidebar_width": "20vw",
    "header_height": "60px"
}
