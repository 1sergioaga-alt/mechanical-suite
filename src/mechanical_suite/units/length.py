from mechanical_suite.units.quantity import Quantity
class Length(Quantity):
    """Represents a length with its engineering unit."""
    _CONVERSION_FACTORS = {
        "mm": 1,
        "cm": 10,
        "m": 1000,
    }