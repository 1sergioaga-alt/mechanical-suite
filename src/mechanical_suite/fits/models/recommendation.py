from mechanical_suite.fits.models.recommendation_level import RecommendationLevel


class Recommendation:
    def __init__(
        self,
        fit: str | None,
        level: RecommendationLevel,
        alternatives: tuple[str, ...] = (),
    ):
        self.fit = fit
        self.level = level
        self.alternatives = alternatives