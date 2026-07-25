from enum import Enum


class Precision(Enum):
    """Represents the required fit precision."""

    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"