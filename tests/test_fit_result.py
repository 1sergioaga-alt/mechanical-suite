from mechanical_suite.fits.models.fit_result import FitResult


def test_create_fit_result():
    result = FitResult(
        hole_upper_deviation=25,
        hole_lower_deviation=0,
        shaft_upper_deviation=-9,
        shaft_lower_deviation=-25,
        hole_maximum_size=50.025,
        hole_minimum_size=50.000,
        shaft_maximum_size=49.991,
        shaft_minimum_size=49.975,
        minimum_clearance=0.009,
        maximum_clearance=0.050,
        fit_type="Clearance",
    )

    assert result.hole_upper_deviation == 25
    assert result.hole_lower_deviation == 0
    assert result.fit_type == "Clearance"