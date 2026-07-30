from mechanical_suite.fits.models.selection_criteria import SelectionCriteria
from mechanical_suite.fits.models.recommendation import Recommendation
from mechanical_suite.enums.fit_category import FitCategory
from mechanical_suite.enums.motion import Motion
from mechanical_suite.enums.precision import Precision
from mechanical_suite.localization.translation_key import TranslationKey


ISO286_RECOMMENDATIONS = [
    (
        SelectionCriteria   (
            motion=Motion.ROTATING,
            precision=Precision.HIGH,
            removable=True,
        ),
        Recommendation(
            fit="H7/g6",
            description=TranslationKey.FIT_GENERAL_RUNNING,
            applications=TranslationKey.APPLICATIONS_GENERAL_RUNNING,
            advantages=TranslationKey.ADVANTAGES_GENERAL_RUNNING,
            disadvantages=TranslationKey.DISADVANTAGES_GENERAL_RUNNING,
            assembly=TranslationKey.ASSEMBLY_GENERAL_RUNNING,
            notes=TranslationKey.NOTES_GENERAL_RUNNING,
            standard=TranslationKey.STANDARD_ISO286,
            ),
       
        ),
]