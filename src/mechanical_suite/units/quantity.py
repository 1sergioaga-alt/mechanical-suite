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