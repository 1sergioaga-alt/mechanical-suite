from mechanical_suite.enums.motion import Motion
from mechanical_suite.enums.precision import Precision


class SelectionCriteria:
    """Represents the application requirements for selecting an ISO 286 fit."""

    def __init__(
        self,
        motion: Motion,
        precision: Precision,
        removable: bool,
    ):
        self.motion = motion
        self.precision = precision
        self.removable = removable