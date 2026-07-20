from mechanical_suite.fits.iso286 import ISO286

iso = ISO286()

value = iso._get_tolerance_grade(40, "IT7")

print(value)

from mechanical_suite.fits.iso286 import ISO286

iso = ISO286()

element_type = "shaft"
lower, upper = iso._get_fundamental_deviation(
    40,
    "g",
    element_type,
)
print(f"{element_type}")
print(f"Lower deviation : {lower}")
print(f"Upper deviation : {upper}")

element_type = "hole"
lower, upper = iso._get_fundamental_deviation(
    40,
    "H",
    element_type,
)
print(f"{element_type}")
print(f"Lower deviation : {lower}")
print(f"Upper deviation : {upper}")

from mechanical_suite.fits.iso286 import ISO286
from mechanical_suite.fits.models.fit import Fit
from mechanical_suite.fits.models.tolerance import Tolerance

iso = ISO286()

fit = Fit(
    nominal_diameter=40,
    hole=Tolerance("H", 7),
    shaft=Tolerance("g", 6),
)

print("\nFit:", fit)

print("\nHole deviations")
hole_lower, hole_upper = iso.get_hole_deviations(fit)

print(f"Lower deviation: {hole_lower} µm")
print(f"Upper deviation: {hole_upper} µm")

print("\nShaft deviations")
shaft_lower, shaft_upper = iso.get_shaft_deviations(fit)

print(f"Lower deviation: {shaft_lower} µm")
print(f"Upper deviation: {shaft_upper} µm")