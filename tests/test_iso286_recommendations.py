from mechanical_suite.enums.motion import Motion
from mechanical_suite.enums.precision import Precision
from mechanical_suite.fits.knowledge.iso286_recommendations import (
    ISO286_RECOMMENDATIONS,
)


def test_iso286_recommendations_cover_all_matrix():
    combinations = {
        (
            criteria.motion,
            criteria.precision,
            criteria.removable,
        )
        for criteria, _ in ISO286_RECOMMENDATIONS
    }

    expected_combinations = {
        (motion, precision, removable)
        for motion in Motion
        for precision in Precision
        for removable in (True, False)
    }

    assert combinations == expected_combinations