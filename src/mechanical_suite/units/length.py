from mechanical_suite.units.quantity import Quantity
class Length(Quantity):
    """Represents a length with its engineering unit."""
    _CONVERSION_FACTORS = {
        "um": 0.001,
        "mm": 1,
        "cm": 10,
        "m": 1000,
    }