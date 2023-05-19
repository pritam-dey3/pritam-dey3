import pynecone as pc


def section() -> pc.Component:
    return pc.vstack(
        pc.heading(pc.text("""Projects"""), size="2xl"),
        pc.heading(
            pc.text(
                """Automatic team detection for any Bundesliga football match (March - April 2022)"""
            ),
            size="xl",
        ),
        pc.vstack(
            pc.text(
                """Key points: Use YoloV7 for human, ball detection. Apply a sequence of classical computer vision + ML methods to detect specific jersey colors. I was able to overcome some critical challenges such as video feeds containing different lighting conditions (day / night), different colors of grass and jerseys of referees. """
            ),
            pc.link(
                pc.text("""GitHub"""),
                href="https://github.com/pritam-dey3/VisionDuo",
            ),
        ),
        pc.heading(
            pc.text(
                """Predicting survival chances of passengers in Titanic (March 2020)"""
            ),
            size="xl",
        ),
        pc.text(
            """Key points: Applying various machine learning tools like decision tree, random forests, extreme boosted trees, support vector machine, KNN and finally creating an ensemble model with all the classifiers."""
        ),
        pc.link(
            pc.text("""GitHub"""),
            href="https://github.com/pritam-dey3/Titanic-Passenger-Survival-Prediction",
        ),
        pc.heading(
            pc.text(
                """Inspecting insurance availability in Chicago (October - November 2019)"""
            ),
            size="xl",
        ),
        pc.text("""Advisor: Prof. Swagata Nandi"""),
        pc.text(
            """Key points: Validation of basic parametric assumptions and transforming data to assure normality. Detection and Rejection of outliers. Basic linear regression and inference."""
        ),
        pc.link(
            pc.text("""GitHub"""),
            href="https://github.com/pritam-dey3/Project-On-Regression",
        ),
        pc.heading(
            pc.text(
                """Shell Sort: Description and empirical evaluation of performance for various gap sequences"""
            ),
            size="xl",
        ),
        pc.text("""Advisor: Prof. Deepayan Sarkar"""),
        pc.text(
            """Key points: Analysing sorting algorithms and their comparison, writing C++ code and using them in R for faster runtime. Comparison of Shell Sort with best gap sequence with Quick Sort."""
        ),
        pc.link(
            pc.text("""GitHub"""),
            href="https://github.com/pritam-dey3/Shell-Sort",
        ),
        pc.heading(
            pc.text(
                """Tests on dispersion of Capon's statistic and Savage statistic (March - May 2020)"""
            ),
            size="xl",
        ),
        pc.text("""Advisor: Prof. Isha Dewan"""),
        pc.text(
            """Key points: Analysing various non-parametric tests of scale parameter of different distribution through simulation."""
        ),
        pc.link(
            pc.text("""GitHub"""),
            href="https://github.com/pritam-dey3/nonparametric_project",
        ),
        pc.heading(
            pc.text("""Analysis of Egyptian skull data: (March - May 2020)"""),
            size="xl",
        ),
        pc.text("""Advisor: Prof. Swagata Nandi"""),
        pc.text(
            """Key points: Applying linear discriminant analysis to classify skull of different age, Factor analysis."""
        ),
        pc.heading(pc.text("""E2E NLG challenge (Jan - May 2021)"""), size="xl"),
        pc.text("""Advisor: Prof. Utpal Garain"""),
        pc.text(
            """Key points: Building a transformer model from scratch to convert structured data about restaurants into text."""
        ),
        pc.link(
            pc.text("""GitHub"""),
            href="https://github.com/pritam-dey3/e2e_nlg_tf",
        ),
    )
