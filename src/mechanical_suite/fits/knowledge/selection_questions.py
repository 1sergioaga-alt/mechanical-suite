from mechanical_suite.fits.models.selection_question import SelectionQuestion


SELECTION_QUESTIONS = (
    SelectionQuestion(
        id="motion",
        options=(
            "rotating",
            "sliding",
            "fixed",
        ),
    ),
    SelectionQuestion(
        id="precision",
        options=(
            "low",
            "medium",
            "high",
        ),
    ),
    SelectionQuestion(
        id="removable",
        options=(
            "yes",
            "no",
        ),
    ),
)