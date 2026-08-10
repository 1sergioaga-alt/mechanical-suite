from mechanical_suite.fits.models.recommendation import Recommendation
from mechanical_suite.fits.models.selection_criteria import SelectionCriteria
from mechanical_suite.fits.recommendation_engine import RecommendationEngine


class Selector:

    def __init__(self):
        self._engine = RecommendationEngine()

    def recommend(
        self,
        criteria: SelectionCriteria,
    ) -> Recommendation:

        return self._engine.recommend(criteria)