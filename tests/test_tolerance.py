from mechanical_suite.fits.models.tolerance import Tolerance


def test_create_tolerance():
    tolerance = Tolerance("H", 7)

    assert tolerance.letter == "H"
    assert tolerance.grade == 7
    
def test_tolerance_repr():
    tolerance = Tolerance("g", 6)

    assert repr(tolerance) == "g6"