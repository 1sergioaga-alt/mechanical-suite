class Recommendation:
    """Represents a recommended ISO 286 fit."""

    def __init__(
        self,
        fit: str,
        description: str,
        applications: list[str],
        advantages: list[str],
        disadvantages: list[str],
        alternatives: list[str],
    ):
        self.fit = fit
        self.description = description
        self.applications = applications
        self.advantages = advantages
        self.disadvantages = disadvantages
        self.alternatives = alternatives

    def __repr__(self):
        return (
            f"Recommended fit: {self.fit}\n\n"
            f"Description: {self.description}\n\n"
            f"Applications: {', '.join(self.applications)}\n"
            f"Advantages: {', '.join(self.advantages)}\n"
            f"Disadvantages: {', '.join(self.disadvantages)}\n"
            f"Alternatives: {', '.join(self.alternatives)}"
        )