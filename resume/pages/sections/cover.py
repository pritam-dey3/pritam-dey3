import pynecone as pc


class Twitter(pc.Component):
    library = "react-icons/fa"
    tag = "FaTwitter"

    size: pc.Var[int]  # type: ignore
    color: pc.Var[str]  # type: ignore


class Linkedin(pc.Component):
    library = "react-icons/fa"
    tag = "FaLinkedin"

    size: pc.Var[int]  # type: ignore
    color: pc.Var[str]  # type: ignore


class Github(pc.Component):
    library = "react-icons/fa"
    tag = "FaGithub"

    size: pc.Var[int]  # type: ignore
    color: pc.Var[str]  # type: ignore


def section() -> pc.Component:
    return pc.responsive_grid(
        pc.image(
            name="Pritam Dey",
            src="profile_img.jpg",
            style={
                "m": "0px !important",
                "p": "21px",
                "height": "auto",
                "width": "100%",
                "border-radius": "50%",
            },
        ),
        pc.box(
            pc.vstack(
                pc.heading("About me", class_name="xl"),
                pc.text(
                    """As a data scientist with a curious mindset, I am passionate about staying up-to-date on the latest developments in machine learning and artificial intelligence. My interests lie in NLP/NLG, computer vision, and traditional ML, and I hope to comprehensively understand models and find their practical applications, in order to solve intricate real world challenges. I am committed to leveraging my skills to develop innovative solutions that drive meaningful results and create value for businesses and individuals alike."""
                ),
                pc.hstack(
                    pc.spacer(),
                    pc.link(Linkedin.create(size=33, color="#967E76"), href="https://www.linkedin.com/in/pritam-dey/"),
                    pc.link(Github.create(size=33, color="#967E76"), href="https://github.com/pritam-dey3"),
                    pc.link(Twitter.create(size=33, color="#967E76",), href="https://twitter.com/mePritam_Dey"),
                    pc.spacer(),
                    width="100%",
                    spacing="18px",
                ),
                style={"m": "0px !important", "p": "21px"},
                align_items="flex-start",
            )
        ),
        columns=[1, 1, 2, 2, 2, 2],
        align_items="center",
        justify_content="center",
    )
