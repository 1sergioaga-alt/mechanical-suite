from mechanical_suite.units.quantity import Quantity
class Mass(Quantity):
    """Represents a mass with its engineering unit."""
    _CONVERSION_FACTORS = {
        "mg": 1,
        "g": 1000,
        "kg": 1000000,
    }