from mechanical_suite.fits.selector import Selector
def test_selector_exists():
    selector = Selector()

    assert selector is not None