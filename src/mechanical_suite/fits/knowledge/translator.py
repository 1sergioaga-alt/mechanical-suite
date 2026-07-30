from mechanical_suite.enums.language import Language

from mechanical_suite.fits.knowledge.languages.es import FITS as ES

from mechanical_suite.fits.knowledge.languages.en import FITS as EN

from mechanical_suite.fits.knowledge.languages.pt import FITS as PT

from mechanical_suite.fits.knowledge.languages.fr import FITS as FR


class Translator:

    _LANGUAGES = {

        Language.SPANISH: ES,

        Language.ENGLISH: EN,

        Language.PORTUGUESE: PT,

        Language.FRENCH: FR,

    }

    def __init__(self, language: Language):

        self.language = language

    def fit(self, fit: str):

        return self._LANGUAGES[self.language][fit]