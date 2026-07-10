from mechanical_suite.units.length import Length


def test_create_length():
    length = Length(25, "mm")

    assert length.value == 25
    assert length.unit == "mm"


def test_length_repr():
    length = Length(25, "mm")

    assert repr(length) == "25 mm"

def test_length_conversion():
    length = Length(1000, "mm")

    converted = length.to("m")

    assert converted.value == 1
    assert converted.unit == "m"

def test_add_lengths():
    a = Length(500, "mm")
    b = Length(1, "m")

    result = a + b

    assert result.value == 1500
    assert result.unit == "mm"
def test_subtract_lengths():
    a = Length(2, "m")
    b = Length(50, "cm")

    result = a - b

    assert result.value == 1.5
    assert result.unit == "m"

def test_multiply_length():
    length = Length(500, "mm")

    result = length * 2

    assert result.value == 1000
    assert result.unit == "mm"

def test_divide_length():
    length = Length(1000, "mm")

    result = length / 2

    assert result.value == 500
    assert result.unit == "mm"
    
def test_divide_by_zero():
    length = Length(100, "mm")

    try:
        length / 0
        assert False
    except ZeroDivisionError:
        assert True

def test_convert_mm_to_m():
    length = Length(1000, "mm")

    result = length.to("m")

    assert result.value == 1
    assert result.unit == "m"

def test_convert_cm_to_mm():
    length = Length(25, "cm")

    result = length.to("mm")

    assert result.value == 250
    assert result.unit == "mm"

def test_convert_m_to_cm():
    length = Length(2, "m")

    result = length.to("cm")

    assert result.value == 200
    assert result.unit == "cm"