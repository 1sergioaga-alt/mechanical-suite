from mechanical_suite.enums.language import Language
from mechanical_suite.localization.translation_key import TranslationKey

from mechanical_suite.localization.languages.es import TEXT as ES_TEXT
from mechanical_suite.localization.languages.en import TEXT as EN_TEXT
from mechanical_suite.localization.languages.pt import TEXT as PT_TEXT
from mechanical_suite.localization.languages.fr import TEXT as FR_TEXT


class Translator:
    """Translates domain keys into localized text."""

    _LANGUAGES = {
        Language.SPANISH: ES_TEXT,
        Language.ENGLISH: EN_TEXT,
        Language.PORTUGUESE: PT_TEXT,
        Language.FRENCH: FR_TEXT,
    }

    def __init__(
        self,
        language: Language,
    ):
        self.language = language

    def translate(
        self,
        key: TranslationKey,
    ) -> str:
        return self._LANGUAGES[self.language][key.value]