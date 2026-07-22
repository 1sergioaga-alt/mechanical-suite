from mechanical_suite.units.quantity import Quantity
class Length(Quantity):
    """Represents a length with its engineering unit."""
    _CONVERSION_FACTORS = {
        "um": 0.001,
        "mm": 1,
        "cm": 10,
        "m": 1000,
    }

    _DISPLAY_DECIMALS = {
        "um": 0,
        "mm": 3,
        "cm": 3,
        "m": 3,
    }

    def __repr__(self):
        decimals = self._DISPLAY_DECIMALS.get(self.unit)
        if decimals is None:
            return f"{self.value} {self.unit}"
        return f"{self.value:.{decimals}f} {self.unit}"