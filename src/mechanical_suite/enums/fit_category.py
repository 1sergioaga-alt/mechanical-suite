from enum import Enum
class FitCategory(Enum):
    """Represents the ISO 286 fit classification."""

    CLEARANCE = "clearance"
    TRANSITION = "transition"
    INTERFERENCE = "interference"
