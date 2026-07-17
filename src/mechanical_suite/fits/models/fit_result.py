class FitResult:
    """Represents the result of an ISO 286 fit calculation."""

    def __init__(
        self,
        hole_upper_deviation: float,
        hole_lower_deviation: float,
        shaft_upper_deviation: float,
        shaft_lower_deviation: float,
        hole_maximum_size: float,
        hole_minimum_size: float,
        shaft_maximum_size: float,
        shaft_minimum_size: float,
        minimum_clearance: float,
        maximum_clearance: float,
        fit_type: str,
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