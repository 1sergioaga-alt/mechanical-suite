from mechanical_suite.fits.selector import Selector
from mechanical_suite.fits.models.selection_criteria import SelectionCriteria
from mechanical_suite.enums.motion import Motion
from mechanical_suite.enums.precision import Precision

def test_selector_recommends_h7_g6_for_rotating_motion():
    selector = Selector()

    criteria = SelectionCriteria(
        motion=Motion.ROTATING,
        precision=Precision.HIGH,
        removable=True,
    )

    recommendation = selector.recommend(criteria)

    assert recommendation.fit == "H7/g6"