import pynecone as pc


def section() -> pc.Component:
    return pc.responsive_grid(
        pc.image(
            name="Pritam Dey",
            src="profile_img.jpg",
            style={"m": "0px !important", "p": "21px", "height": "100%"},
        ),
        pc.box(
            pc.heading("About me", class_name="xl"),
            pc.text(
                """As a data scientist with a curious mindset, I am passionate about staying up-to-date on the latest developments in machine learning and artificial intelligence. My interests lie in NLP/NLG, computer vision, and traditional ML, and I hope to comprehensively understand models and find their practical applications, in order to solve intricate real world challenges. I am committed to leveraging my skills to develop innovative solutions that drive meaningful results and create value for businesses and individuals alike."""
            ),
            style={"m": "0px !important", "p": "21px"},
        ),
        columns=[1, 1, 2, 2, 2, 2]
    )
