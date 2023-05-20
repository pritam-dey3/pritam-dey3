import pynecone as pc


def section() -> pc.Component:
    return pc.vstack(
        pc.heading(pc.text("""Extra Curricular Activities"""), size="2xl"),
        pc.list(
            pc.list_item(
                pc.text(
                    """Music - Playing guitar, Tabla, Keyboard, Mouth organ, Composing music"""
                ),
            ),
            pc.list_item(
                pc.text(
                    """Creative Involvement - Actively participated in Inter Bhavana Drama Competition in Ramakrishna Mission Residential College"""
                ),
            ),
            pc.list_item(
                pc.text("""Sports - Badminton, Table tennis, Chess"""),
            ),
        ),
    )
