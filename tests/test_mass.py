from mechanical_suite.units.mass import Mass
def test_create_mass():
    mass = Mass(25, "g")

    assert mass.value == 25
    assert mass.unit == "g"

def test_mass_repr():
    mass = Mass(25, "g")

    assert repr(mass) == "25 g"

def test_mass_conversion():
    mass = Mass(1000, "g")

    converted = mass.to("kg")

    assert converted.value == 1
    assert converted.unit == "kg"

def test_add_masses():
    a = Mass(500, "mg")
    b = Mass(1, "g")

    result = a + b

    assert result.value == 1500
    assert result.unit == "mg"

def test_subtract_masses():
    a = Mass(2, "g")
    b = Mass(50, "mg")

    result = a - b

    assert result.value == 1.95
    assert result.unit == "g"

def test_multiply_mass():
    mass = Mass(500, "g")

    result = mass * 2

    assert result.value == 1000
    assert result.unit == "g"

def test_divide_mass():
    mass = Mass(1000, "mg")

    result = mass / 2

    assert result.value == 500
    assert result.unit == "mg"    

def test_divide_by_zero():
    mass = Mass(100, "mg")

    try:
        mass / 0
        assert False

    except ZeroDivisionError:
        assert True

def test_convert_mg_to_g():
    mass = Mass(1000, "mg")

    result = mass.to("g")

    assert result.value == 1
    assert result.unit == "g"

def test_convert_g_to_kg():
    mass = Mass(2500, "g")

    result = mass.to("kg")

    assert result.value == 2.5
    assert result.unit == "kg"

def test_convert_g_to_mg():
    mass = Mass(2, "g")

    result = mass.to("mg")

    assert result.value == 2000
    assert result.unit == "mg"


