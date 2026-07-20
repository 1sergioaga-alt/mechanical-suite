import pytest

from mechanical_suite.fits.calculator import Calculator
from mechanical_suite.fits.models.fit import Fit
from mechanical_suite.fits.models.tolerance import Tolerance


def test_calculate_h7_g6():
    fit = Fit(
        nominal_diameter=40,
        hole=Tolerance("H", 7),
        shaft=Tolerance("g", 6),
    )

    calculator = Calculator()

    result = calculator.calculate(fit)

    # Hole deviations
    assert result.hole_lower_deviation.value == 0
    assert result.hole_lower_deviation.unit == "um"

    assert result.hole_upper_deviation.value == 25
    assert result.hole_upper_deviation.unit == "um"

    # Shaft deviations
    assert result.shaft_lower_deviation.value == -25
    assert result.shaft_lower_deviation.unit == "um"

    assert result.shaft_upper_deviation.value == -9
    assert result.shaft_upper_deviation.unit == "um"

    # Hole limits
    assert result.hole_minimum_size.value == pytest.approx(40.000)
    assert result.hole_minimum_size.unit == "mm"

    assert result.hole_maximum_size.value == pytest.approx(40.025)
    assert result.hole_maximum_size.unit == "mm"

    # Shaft limits
    assert result.shaft_minimum_size.value == pytest.approx(39.975)
    assert result.shaft_minimum_size.unit == "mm"

    assert result.shaft_maximum_size.value == pytest.approx(39.991)
    assert result.shaft_maximum_size.unit == "mm"

    # Clearances
    assert result.minimum_clearance.value == pytest.approx(0.009)
    assert result.minimum_clearance.unit == "mm"

    assert result.maximum_clearance.value == pytest.approx(0.050)
    assert result.maximum_clearance.unit == "mm"

    # Fit type
    assert result.fit_type == "Clearance"