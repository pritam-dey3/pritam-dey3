import pynecone as pc


def section() -> pc.Component:
    return pc.vstack(
        pc.heading(pc.text("""Experience"""), class_name="xxl"),
        pc.text(
            """During my professional career, I have gained experience working on various projects. Some of my notable experiences are:"""
        ),
        pc.heading(
            pc.text("""Data Scientist at Dr. Reddy's Laboratory (Aug-2021)"""),
            class_name="xl",
        ),
        pc.list(
            pc.list_item(
                pc.text(
                    """Google Of Investigations: Building a search engine from scratch that relates to various incident investigations in the company."""
                ),
            ),
            pc.list_item(
                pc.text(
                    """Stability Failure Prediction: Predicting whether a product will fail in a particular test based on few past timepoints (3-5) and historical data."""
                ),
            ),
            pc.list_item(
                pc.text(
                    """Cost of Poor Quality: Detecting the reasons behind poor quality in the manufactured batches of a drug."""
                ),
            ),
            pc.list_item(
                pc.text(
                    """Smart Scheduler: Optimizing visit plan for medical representatives."""
                ),
            ),
            pc.list_item(
                pc.text(
                    """Brand Gini: Recommendation system of brands that should be shown to the doctors based on their interest / speciality."""
                ),
            ),
            pc.list_item(
                pc.text(
                    """RCA: Root Cause Analysis of poor performance of Head Quarters"""
                ),
            ),
            pc.list_item(
                pc.text(
                    """Visual-Aid Analysis: Analyse Visual Aids shown to the doctors based on their colour balance, abundance of text / images, location of objects to measure how much visually appealing the slides are."""
                ),
            ),
        ),
        pc.text(
            """These experiences have provided me with valuable insights into the workings of the industry and helped me develop my skills as a data scientist."""
        ),
        class_name="section",
        align_items="flex-start",
    )
