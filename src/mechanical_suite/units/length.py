class Length:
    """Represents a length with its engineering unit."""

    def __init__(self, value: float, unit: str):
        self.value = value
        self.unit = unit

    def __repr__(self):
        return f"{self.value} {self.unit}"

    def to(self, new_unit: str):
        """Convert length to another unit."""

        factors = {
            "mm": 1,
            "cm": 10,
            "m": 1000,
        }

        if self.unit not in factors:
            raise ValueError(f"Unsupported unit: {self.unit}")

        if new_unit not in factors:
            raise ValueError(f"Unsupported unit: {new_unit}")

        value_mm = self.value * factors[self.unit]
        new_value = value_mm / factors[new_unit]

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