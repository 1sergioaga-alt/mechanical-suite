from mechanical_suite.fits.calculator import Calculator
from mechanical_suite.fits.models.fit import Fit
from mechanical_suite.fits.models.tolerance import Tolerance

fit = Fit(
    nominal_diameter=40,
    hole=Tolerance("H", 7),
    shaft=Tolerance("g", 6),
)

calculator = Calculator()

result = calculator.calculate(fit)

print(result)