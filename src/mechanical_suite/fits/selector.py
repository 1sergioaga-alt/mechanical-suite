from mechanical_suite.fits.knowledge.iso286_recommendations import ISO286_RECOMMENDATIONS
from mechanical_suite.fits.models.selection_criteria import SelectionCriteria
from mechanical_suite.fits.models.recommendation import Recommendation

class Selector:

    def recommend(
        self,
        criteria: SelectionCriteria,
    ) -> Recommendation:

        for stored_criteria, recommendation in ISO286_RECOMMENDATIONS:

            if (
                stored_criteria.motion == criteria.motion
                and stored_criteria.precision == criteria.precision
                and stored_criteria.removable == criteria.removable
            ):
                return recommendation

        raise ValueError("No recommendation available.")