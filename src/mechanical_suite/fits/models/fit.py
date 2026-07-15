from mechanical_suite.fits.models.tolerance import Tolerance
class Fit:
    """Represents an ISO fit."""

    def __init__(
        self,
        nominal_diameter: float,
        hole: Tolerance,
        shaft: Tolerance,
    ):
        self.nominal_diameter = nominal_diameter
        self.hole = hole
        self.shaft = shaft
    
    def __repr__(self):
        return (
            f"{self.nominal_diameter} "
            f"{self.hole}/{self.shaft}"
        )