from enum import Enum
class FitType(Enum):
    """Represents the ISO 286 fit classification."""

    CLEARANCE = "clearance"
    TRANSITION = "transition"
    INTERFERENCE = "interference"
