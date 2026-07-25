from enum import Enum


class Motion(Enum):
    """Represents the relative motion between two parts."""

    ROTATING = "rotating"
    SLIDING = "sliding"
    FIXED = "fixed"