from mechanical_suite.fits.iso286 import ISO286
from mechanical_suite.fits.models.fit import Fit
from mechanical_suite.fits.models.fit_result import FitResult
from mechanical_suite.units.length import Length


class Calculator:
    """Calculates ISO 286 fits."""

    def __init__(self):
        self.iso286 = ISO286()

    def calculate(self, fit: Fit) -> FitResult:

        # Get deviations (µm)
        hole_lower, hole_upper = self.iso286.get_hole_deviations(fit)
        shaft_lower, shaft_upper = self.iso286.get_shaft_deviations(fit)

        # Create Length objects for deviations
        hole_lower_deviation = Length(hole_lower, "um")
        hole_upper_deviation = Length(hole_upper, "um")

        shaft_lower_deviation = Length(shaft_lower, "um")
        shaft_upper_deviation = Length(shaft_upper, "um")

        # Convert deviations to millimeters
        hole_lower_mm = hole_lower_deviation.to("mm")
        hole_upper_mm = hole_upper_deviation.to("mm")

        shaft_lower_mm = shaft_lower_deviation.to("mm")
        shaft_upper_mm = shaft_upper_deviation.to("mm")

        # Calculate hole sizes
        hole_minimum_size = Length(
            fit.nominal_diameter + hole_lower_mm.value,
            "mm",
        )

        hole_maximum_size = Length(
            fit.nominal_diameter + hole_upper_mm.value,
            "mm",
        )

        # Calculate shaft sizes
        shaft_minimum_size = Length(
            fit.nominal_diameter + shaft_lower_mm.value,
            "mm",
        )

        shaft_maximum_size = Length(
            fit.nominal_diameter + shaft_upper_mm.value,
            "mm",
        )

        # Calculate clearances
        minimum_clearance = Length(
            hole_minimum_size.value - shaft_maximum_size.value,
            "mm",
        )

        maximum_clearance = Length(
            hole_maximum_size.value - shaft_minimum_size.value,
            "mm",
        )

        # TODO: Implement fit type calculation
        fit_type = self._get_fit_type(
        minimum_clearance,
        maximum_clearance,
        )

        return FitResult(
            hole_upper_deviation=hole_upper_deviation,
            hole_lower_deviation=hole_lower_deviation,

            shaft_upper_deviation=shaft_upper_deviation,
            shaft_lower_deviation=shaft_lower_deviation,

            hole_maximum_size=hole_maximum_size,
            hole_minimum_size=hole_minimum_size,

            shaft_maximum_size=shaft_maximum_size,
            shaft_minimum_size=shaft_minimum_size,

            minimum_clearance=minimum_clearance,
            maximum_clearance=maximum_clearance,

            fit_type=fit_type,
        )

    def _get_fit_type(
        self,
        minimum_clearance: Length,
        maximum_clearance: Length,
    ) -> str:

        if minimum_clearance.value >= 0:
            return "Clearance"

        if maximum_clearance.value < 0:
            return "Interference"

        return "Transition"