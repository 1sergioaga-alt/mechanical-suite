from mechanical_suite.localization.translation_key import TranslationKey
class Recommendation:
    """Represents an ISO 286 fit recommendation."""

    def __init__(
        self,
        fit: str,
        description: TranslationKey,
        applications: TranslationKey,
        advantages: TranslationKey,
        disadvantages: TranslationKey,
        assembly: TranslationKey,
        notes: TranslationKey,
        standard: TranslationKey,
    ):
        self.fit = fit
        self.description_key = description
        self.applications_key = applications
        self.advantages_key = advantages
        self.disadvantages_key = disadvantages