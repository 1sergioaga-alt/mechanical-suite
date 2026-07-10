from mechanical_suite.units.quantity import Quantity
class Length(Quantity):
    """Represents a length with its engineering unit."""
    _CONVERSION_FACTORS = {
        "mm": 1,
        "cm": 10,
        "m": 1000,
    }

    def to(self, new_unit: str):
        """Convert length to another unit."""

        if self.unit not in self._CONVERSION_FACTORS:
            raise ValueError(f"Unsupported unit: {self.unit}")

        if new_unit not in self._CONVERSION_FACTORS:
            raise ValueError(f"Unsupported unit: {new_unit}")

        value_mm = self.value * self._CONVERSION_FACTORS[self.unit]
        new_value = value_mm / self._CONVERSION_FACTORS[new_unit]

        return self.__class__(new_value, new_unit)