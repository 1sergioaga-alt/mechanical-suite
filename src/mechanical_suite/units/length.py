"""
Length module for Mechanical Suite.

Provides the Length class and unit conversions.
"""


class Length:
    """Represents a length with its engineering unit."""

    def __init__(self, value: float, unit: str):
        self.value = value
        self.unit = unit

    def __repr__(self):
        return f"{self.value} {self.unit}"