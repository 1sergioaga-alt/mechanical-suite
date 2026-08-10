from mechanical_suite.fits.knowledge.selection_questions import (
    SELECTION_QUESTIONS,
)


def test_selection_questions_exist():
    assert len(SELECTION_QUESTIONS) == 3