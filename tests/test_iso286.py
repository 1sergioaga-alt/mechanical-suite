from mechanical_suite.fits.iso286 import ISO286


def test_get_tolerance_definition_for_g6_shaft():
    iso286 = ISO286()

    lower, upper = iso286.get_tolerance_definition(
        diameter=40,
        letter="g",
        element_type="shaft",
        grade="IT6",
    )

    assert lower == -25
    assert upper == -9