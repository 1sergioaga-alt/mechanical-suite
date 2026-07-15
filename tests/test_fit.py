from mechanical_suite.fits.models.fit import Fit
from mechanical_suite.fits.models.tolerance import Tolerance


def test_create_fit():
    fit = Fit(
        50,
        Tolerance("H", 7),
        Tolerance("g", 6),
    )

    assert fit.nominal_diameter == 50
    assert fit.hole.letter == "H"
    assert fit.hole.grade == 7
    assert fit.shaft.letter == "g"
    assert fit.shaft.grade == 6

def test_fit_repr():
    fit = Fit(
        50,
        Tolerance("H", 7),
        Tolerance("g", 6),
    )

    assert repr(fit) == "50 H7/g6"