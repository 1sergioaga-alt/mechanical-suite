from mechanical_suite.fits.models.selection_criteria import SelectionCriteria
from mechanical_suite.fits.models.recommendation import Recommendation
from mechanical_suite.enums.fit_type import FitType
from mechanical_suite.enums.motion import Motion
from mechanical_suite.enums.precision import Precision


ISO286_RECOMMENDATIONS = [
    (
        SelectionCriteria   (
            motion=Motion.ROTATING,
            precision=Precision.HIGH,
            removable=True,
        ),
        Recommendation(
            fit="H7/g6",
            description="General running fit for rotating shafts.",
            applications=[
                "Electric motors",
                "Pumps",
                "Gearboxes",
            ],
            advantages=[
                "Easy assembly",
                "Low friction",
                "Good concentricity",
            ],
            disadvantages=[
                "Small radial play",
            ],
            alternatives=[
                "H8/f7",
                "H7/h5",
            ],
        ),
    ),
]