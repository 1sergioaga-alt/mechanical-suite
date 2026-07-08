class Length:
    """Represents a length with its engineering unit."""
    _CONVERSION_FACTORS = {
        "mm": 1,
        "cm": 10,
        "m": 1000,
    }

    def __init__(self, value: float, unit: str):
        self.value = value
        self.unit = unit

    def __repr__(self):
        return f"{self.value} {self.unit}"

    def to(self, new_unit: str):
        """Convert length to another unit."""

        if self.unit not in self._CONVERSION_FACTORS:
            raise ValueError(f"Unsupported unit: {self.unit}")

        if new_unit not in self._CONVERSION_FACTORS:
            raise ValueError(f"Unsupported unit: {new_unit}")

        value_mm = self.value * self._CONVERSION_FACTORS[self.unit]
        new_value = value_mm / self._CONVERSION_FACTORS[new_unit]

        return Length(new_value, new_unit)
    
    def __add__(self, other):
        """Add two Length objects."""

        if not isinstance(other, Length):
            return NotImplemented

        other_converted = other.to(self.unit)

        return Length(
            self.value + other_converted.value,
            self.unit
        )

    def __sub__(self, other):
        """Subtract two Length objects."""
        if not isinstance(other, Length):
            return NotImplemented
        other_converted = other.to(self.unit)
        return Length(
        self.value - other_converted.value,
        self.unit
    )

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return Length(self.value * other, self.unit)
        raise TypeError("Can only multiply Length by a number")

    def __truediv__(self, other):
        if isinstance(other, (int, float)):
            return Length(self.value / other, self.unit)

        raise TypeError("Can only divide Length by a number")