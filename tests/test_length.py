from mechanical_suite.units.length import Length


def test_create_length():
    length = Length(25, "mm")

    assert length.value == 25
    assert length.unit == "mm"


def test_length_repr():
    length = Length(25, "mm")

    assert repr(length) == "25 mm"