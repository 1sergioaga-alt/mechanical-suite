class Tolerance:
    """Represents an ISO tolerance designation (e.g. H7, g6)."""

    def __init__(self, letter: str, grade: int):
        self.letter = letter
        self.grade = grade

    def __repr__(self):
        return f"{self.letter}{self.grade}"