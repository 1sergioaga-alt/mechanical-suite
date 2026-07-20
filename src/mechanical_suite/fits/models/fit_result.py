from mechanical_suite.units.length import Length
class FitResult:

    def __init__(
        self,
        hole_upper_deviation: Length,
        hole_lower_deviation: Length,

        shaft_upper_deviation: Length,
        shaft_lower_deviation: Length,

        hole_maximum_size: Length,
        hole_minimum_size: Length,

        shaft_maximum_size: Length,
        shaft_minimum_size: Length,

        minimum_clearance: Length,
        maximum_clearance: Length,

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