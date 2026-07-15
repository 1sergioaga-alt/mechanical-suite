class Quantity:
    """Base class for all physical quantities."""

    def __init__(self, value: float, unit: str):
        self.value = value
        self.unit = unit

    def __repr__(self):
        return f"{self.value} {self.unit}"

    
    def __add__(self, other):
        """Return the sum of two quantities."""
        if not isinstance(other, Quantity):
            return NotImplemented

        other_converted = other.to(self.unit)

        return self.__class__(
        self.value + other_converted.value,
        self.unit
    )

    def __sub__(self, other):
        """Return the difference between two quantities."""
        if not isinstance(other, Quantity):
            return NotImplemented
        other_converted = other.to(self.unit)
        return self.__class__(
        self.value - other_converted.value,
        self.unit
    )

    def __mul__(self, other):
        """Multiply the quantity by a scalar."""
        if isinstance(other, (int, float)):
            return self.__class__(self.value * other, self.unit)
        raise TypeError("Can only multiply by a number")

    def __truediv__(self, other):
        """Divide the quantity by a scalar."""
        if isinstance(other, (int, float)):
            return self.__class__(self.value / other, self.unit)

        raise TypeError("Can only divide by a number")
    
    def to(self, new_unit: str):
        """Convert quantity to another unit."""
        if self.unit not in self._CONVERSION_FACTORS:
            raise ValueError(f"Unsupported unit: {self.unit}")

        if new_unit not in self._CONVERSION_FACTORS:
            raise ValueError(f"Unsupported unit: {new_unit}")

        value_base = self.value * self._CONVERSION_FACTORS[self.unit]
        new_value = value_base / self._CONVERSION_FACTORS[new_unit]

        return self.__class__(new_value, new_unit)