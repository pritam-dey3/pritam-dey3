import pynecone as pc


def section() -> pc.Component:
    return pc.vstack(
        pc.heading(pc.text("""Education and Qualifications"""), class_name="xxl"),
        pc.list(
            pc.list_item(
                pc.text("""Indian Statistical Institute - (2019 - 2021)"""),
                pc.list(
                    pc.list_item(
                        pc.text("""Master of Statistics"""),
                        pc.list(
                            pc.list_item(
                                pc.text("""Grade: 73%"""),
                            ),
                        ),
                    ),
                ),
            ),
            pc.list_item(
                pc.text(
                    """Ramakrishna Mission Residential College, Narendrapur - (2016 - 2019)"""
                ),
                pc.list(
                    pc.list_item(
                        pc.text("""BSc (Hons.) Statistics"""),
                        pc.list(
                            pc.list_item(
                                pc.text("""CGPA: 8.88"""),
                            ),
                        ),
                    ),
                ),
            ),
            pc.list_item(
                pc.text(
                    """Ramakrishna Mission Vidyalaya, Narendrapur - (2014 - 2016)"""
                ),
                pc.list(
                    pc.list_item(
                        pc.text("""Grade: 88.8% in WBCHSE class XII-Science"""),
                    ),
                ),
            ),
        ),
        class_name="section",
        align_items="flex-start",
    )
