from mechanical_suite.enums.language import Language
from mechanical_suite.localization.translation_key import TranslationKey
from mechanical_suite.localization.translator import Translator


def test_translator_stores_selected_language():
    translator = Translator(Language.SPANISH)

    assert translator.language == Language.SPANISH


def test_translator_returns_spanish_text():
    translator = Translator(Language.SPANISH)

    text = translator.translate(
        TranslationKey.FIT_GENERAL_RUNNING
    )

    assert text == "Ajuste con holgura controlada para ejes giratorios de uso general."

def test_translator_returns_english_text():
    translator = Translator(Language.ENGLISH)

    text = translator.translate(
        TranslationKey.FIT_GENERAL_RUNNING
    )

    assert text == "Controlled clearance fit for general-purpose rotating shafts."


# ==========================================================
# H7/f7 - Locational Clearance Fit
# ==========================================================

def test_translator_returns_locational_clearance_in_spanish():
    translator = Translator(Language.SPANISH)

    text = translator.translate(
        TranslationKey.FIT_LOCATIONAL_CLEARANCE
    )

    assert (
        text
        == "Ajuste de localización con pequeña holgura para un posicionamiento preciso."
    )


def test_translator_returns_locational_clearance_applications_in_spanish():
    translator = Translator(Language.SPANISH)

    text = translator.translate(
        TranslationKey.APPLICATIONS_LOCATIONAL_CLEARANCE
    )

    assert (
        text
        == "Rodamientos, poleas, engranajes, acoples y componentes que requieren un posicionamiento preciso con fácil desmontaje."
    )


def test_translator_returns_locational_clearance_advantages_in_spanish():
    translator = Translator(Language.SPANISH)

    text = translator.translate(
        TranslationKey.ADVANTAGES_LOCATIONAL_CLEARANCE
    )

    assert (
        text
        == "Proporciona un posicionamiento preciso, mantiene una pequeña holgura y facilita el desmontaje para inspección y mantenimiento."
    )


def test_translator_returns_locational_clearance_disadvantages_in_spanish():
    translator = Translator(Language.SPANISH)

    text = translator.translate(
        TranslationKey.DISADVANTAGES_LOCATIONAL_CLEARANCE
    )

    assert (
        text
        == "No elimina completamente el juego y no es adecuado para transmitir par mediante interferencia."
    )


def test_translator_returns_locational_clearance_assembly_in_spanish():
    translator = Translator(Language.SPANISH)

    text = translator.translate(
        TranslationKey.ASSEMBLY_LOCATIONAL_CLEARANCE
    )

    assert (
        text
        == "Montaje manual. Normalmente no requiere prensa ni calentamiento. Se recomienda una ligera lubricación durante el ensamblaje."
    )


def test_translator_returns_locational_clearance_notes_in_spanish():
    translator = Translator(Language.SPANISH)

    text = translator.translate(
        TranslationKey.NOTES_LOCATIONAL_CLEARANCE
    )

    assert (
        text
        == "Muy utilizado cuando el componente debe quedar correctamente centrado y, al mismo tiempo, poder desmontarse con facilidad."
    )



def assert_all_translation_keys_exist(language: Language):
    translator = Translator(language)

    for key in TranslationKey:
        text = translator.translate(key)

        assert isinstance(text, str)
        assert text.strip() != ""

def test_all_translation_keys_exist_in_spanish():
    assert_all_translation_keys_exist(Language.SPANISH)


def test_all_translation_keys_exist_in_english():
    assert_all_translation_keys_exist(Language.ENGLISH)