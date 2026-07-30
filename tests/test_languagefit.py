from mechanical_suite.fits.knowledge.languages.es import FITS as ES_FITS
from mechanical_suite.fits.knowledge.languages.en import FITS as EN_FITS
from mechanical_suite.enums.fit_category import FitCategory
from mechanical_suite.enums.standard import Standard


REQUIRED_FIELDS = {
    "fit",
    "category",
    "fit_type",
    "description",
    "applications",
    "advantages",
    "disadvantages",
    "assembly",
    "notes",
    "standard",
}

def test_languages_have_same_fit_codes():
    assert set(ES_FITS.keys()) == set(EN_FITS.keys())

def test_all_spanish_fits_have_required_fields():
    for fit in ES_FITS.values():
        assert set(fit.keys()) == REQUIRED_FIELDS

def test_all_english_fits_have_required_fields():
    for fit in EN_FITS.values():
        assert set(fit.keys()) == REQUIRED_FIELDS

def test_fit_codes_are_unique():
    codes = list(ES_FITS.keys())
    assert len(codes) == len(set(codes))

def test_fit_code_matches_dictionary_key():
    for code, fit in ES_FITS.items():
        assert code == fit["fit"]

def test_all_categories_are_valid():
    for fit in ES_FITS.values():
        assert isinstance(fit["category"], FitCategory)

def test_all_standards_are_valid():
    for fit in ES_FITS.values():
        assert fit["standard"] == Standard.ISO_286

def test_no_empty_strings():
    text_fields = [
        "fit_type",
        "description",
        "applications",
        "advantages",
        "disadvantages",
        "assembly",
        "notes",
    ]

    for fit in ES_FITS.values():
        for field in text_fields:
            assert fit[field].strip() != ""

    for fit in EN_FITS.values():
        for field in text_fields:
            assert fit[field].strip() != ""