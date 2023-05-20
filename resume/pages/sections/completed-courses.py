import pynecone as pc


def section() -> pc.Component:
    return pc.vstack(
        pc.heading(pc.text("""Completed Courses"""), class_name="xxl"),
        pc.text(
            """Throughout my academic and professional journey, I have completed several courses to enhance my knowledge and skills. Some of the courses that I have completed are:"""
        ),
        pc.list(
            pc.list_item(
                pc.text(
                    """Machine Learning course offered by Stanford University on Coursera."""
                ),
            ),
            pc.list_item(
                pc.text(
                    """Sequence, Time Series, Prediction Course offered by deeplearning.ai"""
                ),
            ),
            pc.list_item(
                pc.text("""Complete SQL Bootcamp Course offered by Udemy"""),
            ),
            pc.list_item(
                pc.text(
                    """CS224n: Natural Language Processing with Deep Learning (open course) from Stanford University"""
                ),
            ),
        ),
        class_name="section",
        align_items="flex-start",
    )
