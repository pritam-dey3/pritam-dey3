import pynecone as pc


def section() -> pc.Component:
    return pc.vstack(
        pc.heading(pc.text("""Technical Skills"""), size="2xl"),
        pc.list(
            pc.list_item(
                pc.text("""Statistical Modelling and Inference"""),
            ),
            pc.list_item(
                pc.text("""Robust regression techniques"""),
            ),
            pc.list_item(
                pc.text("""Machine Learning and AutoML."""),
            ),
            pc.list_item(
                pc.text("""Deep learning (NLP / NLG, Computer Vision)"""),
            ),
            pc.list_item(
                pc.text("""Programming languages: Python, R, MATLAB, C, C++"""),
            ),
            pc.list_item(
                pc.text("""Libraries/Frameworks: Tensorflow, Pytorch"""),
            ),
            pc.list_item(
                pc.text("""Reinforcement Learning"""),
            ),
            pc.list_item(
                pc.text("""Visualization: Plotly, Matplotlib etc."""),
            ),
            pc.list_item(
                pc.text("""Dashboarding: Streamlit, Gradio"""),
            ),
            pc.list_item(
                pc.text("""Database Management: SQL"""),
            ),
        ),
        pc.heading(pc.text("""Interests"""), size="2xl"),
        pc.list(
            pc.list_item(
                pc.text(
                    """Playing with data and extracting stories from real world datasets"""
                ),
            ),
            pc.list_item(
                pc.text("""Applying machine learning tools to solve problems"""),
            ),
            pc.list_item(
                pc.text(
                    """NLP / NLG: Using large language models to explain or create structured data from text."""
                ),
            ),
            pc.list_item(
                pc.text(
                    """Computer Vision related problems. object detection, image segmentation, classification etc."""
                ),
            ),
            pc.list_item(
                pc.text(
                    """Studying state of the art machine learning and deep learning tools for data science"""
                ),
            ),
        ),
    )
