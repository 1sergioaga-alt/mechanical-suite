class FitResult:
    """Represents the result of an ISO 286 fit calculation."""

    def __init__(
        self,
        hole_upper_deviation,
        hole_lower_deviation,
        shaft_upper_deviation,
        shaft_lower_deviation,
        hole_maximum_size,
        hole_minimum_size,
        shaft_maximum_size,
        shaft_minimum_size,
        minimum_clearance,
        maximum_clearance,
        fit_type,
    ):
        self.hole_upper_deviation = hole_upper_deviation
        self.hole_lower_deviation = hole_lower_deviation

        self.shaft_upper_deviation = shaft_upper_deviation
        self.shaft_lower_deviation = shaft_lower_deviation

        self.hole_maximum_size = hole_maximum_size
        self.hole_minimum_size = hole_minimum_size

        self.shaft_maximum_size = shaft_maximum_size
        self.shaft_minimum_size = shaft_minimum_size

        self.minimum_clearance = minimum_clearance
        self.maximum_clearance = maximum_clearance

        self.fit_type = fit_type

    def __repr__(self):
        return (
            "Fit Result\n"
            "-----------------------------\n"
            "Hole\n"
            f"  Lower deviation : {self.hole_lower_deviation}\n"
            f"  Upper deviation : {self.hole_upper_deviation}\n"
            f"  Minimum size    : {self.hole_minimum_size}\n"
            f"  Maximum size    : {self.hole_maximum_size}\n\n"
            "Shaft\n"
            f"  Lower deviation : {self.shaft_lower_deviation}\n"
            f"  Upper deviation : {self.shaft_upper_deviation}\n"
            f"  Minimum size    : {self.shaft_minimum_size}\n"
            f"  Maximum size    : {self.shaft_maximum_size}\n\n"
            "Clearances\n"
            f"  Minimum         : {self.minimum_clearance}\n"
            f"  Maximum         : {self.maximum_clearance}\n\n"
            f"Fit type          : {self.fit_type}"
        )