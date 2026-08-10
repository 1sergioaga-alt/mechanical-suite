import pytest

from mechanical_suite.enums.motion import Motion
from mechanical_suite.enums.precision import Precision
from mechanical_suite.fits.models.selection_criteria import SelectionCriteria
from mechanical_suite.fits.recommendation_engine import RecommendationEngine
from mechanical_suite.fits.models.recommendation_level import RecommendationLevel



def test_recommendation_engine_returns_expected_recommendation():
    engine = RecommendationEngine()

    criteria = SelectionCriteria(
        motion=Motion.ROTATING,
        precision=Precision.HIGH,
        removable=True,
    )

    recommendation = engine.recommend(criteria)

    assert recommendation.fit == "H7/g6"
    assert recommendation.level == RecommendationLevel.DIRECT
    assert recommendation.alternatives == ()


def test_recommendation_engine_raises_when_no_recommendation_exists():
    engine = RecommendationEngine()

    criteria = SelectionCriteria(
        motion="Any",
        precision=Precision.LOW,
        removable=True,
    )

    with pytest.raises(ValueError, match="No recommendation available."):
        engine.recommend(criteria)

def test_recommendation_engine_returns_second_recommendation():
    engine = RecommendationEngine()

    criteria = SelectionCriteria(
        motion=Motion.FIXED,
        precision=Precision.HIGH,
        removable=True,
    )

    recommendation = engine.recommend(criteria)

    assert recommendation.fit == "H7/h6"
    assert recommendation.level == RecommendationLevel.DIRECT
    assert recommendation.alternatives == ()

def test_recommendation_engine_rotating_medium_removable():
    engine = RecommendationEngine()

    criteria = SelectionCriteria(
        motion=Motion.ROTATING,
        precision=Precision.MEDIUM,
        removable=True,
    )

    recommendation = engine.recommend(criteria)

    assert recommendation.fit == "H8/f7"
    assert recommendation.level == RecommendationLevel.DIRECT
    assert recommendation.alternatives == ()


def test_recommendation_engine_rotating_low_removable():
    engine = RecommendationEngine()

    criteria = SelectionCriteria(
        motion=Motion.ROTATING,
        precision=Precision.LOW,
        removable=True,
    )

    recommendation = engine.recommend(criteria)

    assert recommendation.fit == "H9/d9"
    assert recommendation.level == RecommendationLevel.DIRECT
    assert recommendation.alternatives == ()


def test_recommendation_engine_sliding_high_removable():
    engine = RecommendationEngine()

    criteria = SelectionCriteria(
        motion=Motion.SLIDING,
        precision=Precision.HIGH,
        removable=True,
    )

    recommendation = engine.recommend(criteria)

    assert recommendation.fit == "H7/h6"
    assert recommendation.level == RecommendationLevel.DIRECT
    assert recommendation.alternatives == ()


def test_recommendation_engine_sliding_medium_removable():
    engine = RecommendationEngine()

    criteria = SelectionCriteria(
        motion=Motion.SLIDING,
        precision=Precision.MEDIUM,
        removable=True,
    )

    recommendation = engine.recommend(criteria)

    assert recommendation.fit == "H8/e8"
    assert recommendation.level == RecommendationLevel.DIRECT
    assert recommendation.alternatives == ()


def test_recommendation_engine_sliding_low_removable():
    engine = RecommendationEngine()

    criteria = SelectionCriteria(
        motion=Motion.SLIDING,
        precision=Precision.LOW,
        removable=True,
    )

    recommendation = engine.recommend(criteria)

    assert recommendation.fit == "H11/c11"
    assert recommendation.level == RecommendationLevel.DIRECT
    assert recommendation.alternatives == ()


def test_recommendation_engine_fixed_high_removable():
    engine = RecommendationEngine()

    criteria = SelectionCriteria(
        motion=Motion.FIXED,
        precision=Precision.HIGH,
        removable=True,
    )

    recommendation = engine.recommend(criteria)

    assert recommendation.fit == "H7/h6"
    assert recommendation.level == RecommendationLevel.DIRECT
    assert recommendation.alternatives == ()


def test_recommendation_engine_fixed_medium_removable():
    engine = RecommendationEngine()

    criteria = SelectionCriteria(
        motion=Motion.FIXED,
        precision=Precision.MEDIUM,
        removable=True,
    )

    recommendation = engine.recommend(criteria)

    assert recommendation.fit == "H7/h6"
    assert recommendation.level == RecommendationLevel.DIRECT
    assert recommendation.alternatives == ()

def test_recommendation_engine_rotating_high_not_removable():
    engine = RecommendationEngine()

    criteria = SelectionCriteria(
        motion=Motion.ROTATING,
        precision=Precision.HIGH,
        removable=False,
    )

    recommendation = engine.recommend(criteria)

    assert recommendation.fit == "H7/p6"
    assert recommendation.level == RecommendationLevel.ORIENTATIVE
    assert recommendation.alternatives == ("H7/k6", "H7/n6")

def test_recommendation_engine_rotating_medium_not_removable():
    engine = RecommendationEngine()

    criteria = SelectionCriteria(
        motion=Motion.ROTATING,
        precision=Precision.MEDIUM,
        removable=False,
    )

    recommendation = engine.recommend(criteria)

    assert recommendation.fit == "H7/n6"
    assert recommendation.level == RecommendationLevel.ORIENTATIVE
    assert recommendation.alternatives == ("H7/m6", "H7/p6")

def test_recommendation_engine_rotating_low_not_removable():
    engine = RecommendationEngine()

    criteria = SelectionCriteria(
        motion=Motion.ROTATING,
        precision=Precision.LOW,
        removable=False,
    )

    recommendation = engine.recommend(criteria)

    assert recommendation.fit == "H7/s6"
    assert recommendation.level == RecommendationLevel.ORIENTATIVE
    assert recommendation.alternatives == ("H7/r6", "H7/p6")

def test_recommendation_engine_sliding_high_not_removable():
    engine = RecommendationEngine()

    criteria = SelectionCriteria(
        motion=Motion.SLIDING,
        precision=Precision.HIGH,
        removable=False,
    )

    recommendation = engine.recommend(criteria)

    assert recommendation.fit == "H7/k6"
    assert recommendation.level == RecommendationLevel.ORIENTATIVE
    assert recommendation.alternatives == ("H7/m6", "H7/n6")

def test_recommendation_engine_sliding_medium_not_removable():
    engine = RecommendationEngine()

    criteria = SelectionCriteria(
        motion=Motion.SLIDING,
        precision=Precision.MEDIUM,
        removable=False,
    )

    recommendation = engine.recommend(criteria)

    assert recommendation.fit == "H7/m6"
    assert recommendation.level == RecommendationLevel.ORIENTATIVE
    assert recommendation.alternatives == ("H7/k6", "H7/n6")

def test_recommendation_engine_sliding_low_not_removable():
    engine = RecommendationEngine()

    criteria = SelectionCriteria(
        motion=Motion.SLIDING,
        precision=Precision.LOW,
        removable=False,
    )

    recommendation = engine.recommend(criteria)

    assert recommendation.fit == "H7/r6"
    assert recommendation.level == RecommendationLevel.ORIENTATIVE
    assert recommendation.alternatives == ("H7/s6", "H7/m6")

def test_recommendation_engine_fixed_high_not_removable():
    engine = RecommendationEngine()

    criteria = SelectionCriteria(
        motion=Motion.FIXED,
        precision=Precision.HIGH,
        removable=False,
    )

    recommendation = engine.recommend(criteria)

    assert recommendation.fit == "H7/p6"
    assert recommendation.level == RecommendationLevel.ORIENTATIVE
    assert recommendation.alternatives == ("H7/k6", "H7/n6")

def test_recommendation_engine_fixed_medium_not_removable():
    engine = RecommendationEngine()

    criteria = SelectionCriteria(
        motion=Motion.FIXED,
        precision=Precision.MEDIUM,
        removable=False,
    )

    recommendation = engine.recommend(criteria)

    assert recommendation.fit == "H7/n6"
    assert recommendation.level == RecommendationLevel.ORIENTATIVE
    assert recommendation.alternatives == ("H7/m6", "H7/p6")

def test_recommendation_engine_fixed_low_not_removable():
    engine = RecommendationEngine()

    criteria = SelectionCriteria(
        motion=Motion.FIXED,
        precision=Precision.LOW,
        removable=False,
    )

    recommendation = engine.recommend(criteria)

    assert recommendation.fit == "H7/s6"
    assert recommendation.level == RecommendationLevel.ORIENTATIVE
    assert recommendation.alternatives == ("H7/r6", "H7/p6")

def test_recommendation_engine_fixed_low_removable():
    engine = RecommendationEngine()

    criteria = SelectionCriteria(
        motion=Motion.FIXED,
        precision=Precision.LOW,
        removable=True,
    )

    recommendation = engine.recommend(criteria)

    assert recommendation.fit is None
    assert recommendation.level == RecommendationLevel.INSUFFICIENT
    assert recommendation.alternatives == (
        "H7/g6",
        "H7/h6",
        "H8/f7",
    )