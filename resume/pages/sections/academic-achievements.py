import pynecone as pc


def section() -> pc.Component:
    return pc.vstack(
        pc.heading(pc.text("""Academic Achievements"""), size="2xl"),
        pc.text(
            """During my academic career, I have achieved several notable accomplishments. Some of them are:"""
        ),
        pc.list(
            pc.list_item(
                pc.text("""Ranked 24 in Mathematical Statistics in IIT JAM 2019"""),
            ),
            pc.list_item(
                pc.text("""Ranked 17 in ISI M.Stat entrance 2019"""),
            ),
            pc.list_item(
                pc.text(
                    """Ranked in top 2 percentile in Introduction to R Software, NPTEL course"""
                ),
            ),
            pc.list_item(
                pc.text(
                    """Ranked in top 1 percentile in Data Structure, Algorithm and Programming Using Python, NPTEL course"""
                ),
            ),
        ),
        pc.text(
            """These achievements have been the result of my hard work, dedication, and passion for learning."""
        ),
    )
