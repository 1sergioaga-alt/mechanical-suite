from typing import Any
from typing import TypedDict
from mechanical_suite.enums.fit_category import FitCategory
from mechanical_suite.enums.standard import Standard


class FitKnowledge(TypedDict):
    fit: str
    category: FitCategory
    fit_type: str
    description: str
    applications: str
    advantages: str
    disadvantages: str
    assembly: str
    notes: str
    standard: str

FITS: dict[str, FitKnowledge] = {

    "H11/c11": {
        "fit": "H11/c11",
        "category": FitCategory.CLEARANCE,
        "fit_type": "Loose running fit",
        "description": "Fit with large clearance intended for components with low precision requirements.",
        "applications": "Agricultural machinery, steel structures, low-cost assemblies and equipment exposed to dirt or corrosion.",
        "advantages": "Very easy assembly and disassembly, low manufacturing cost and excellent tolerance to contaminants.",
        "disadvantages": "Large play between components and poor positioning accuracy.",
        "assembly": "Manual assembly without special tools.",
        "notes": "Recommended only when precision is not a critical requirement.",
        "standard": Standard.ISO_286,
    },

    "H9/d9": {
        "fit": "H9/d9",
        "category": FitCategory.CLEARANCE,
        "fit_type": "Free running fit",
        "description": "Fit with generous clearance for continuous free movement.",
        "applications": "Slow rotating shafts, mechanisms exposed to dust, moisture or significant thermal expansion.",
        "advantages": "Excellent freedom of movement and minimal risk of seizure.",
        "disadvantages": "Does not provide accurate guidance or positioning.",
        "assembly": "Manual assembly with standard lubrication.",
        "notes": "Suitable when reliable movement is more important than precision.",
        "standard": Standard.ISO_286,
    },

    "H8/e8": {
        "fit": "H8/e8",
        "category": FitCategory.CLEARANCE,
        "fit_type": "Easy running fit",
        "description": "Fit with moderate clearance for shafts requiring smooth rotation.",
        "applications": "Fans, centrifugal pumps, pulleys and medium-speed industrial equipment.",
        "advantages": "Smooth operation, effective lubrication and reduced wear.",
        "disadvantages": "Does not ensure precise positioning under heavy loads.",
        "assembly": "Manual assembly with light lubrication.",
        "notes": "Commonly used where smooth and reliable operation is required.",
        "standard": Standard.ISO_286,
    },

    "H8/f7": {
        "fit": "H8/f7",
        "category": FitCategory.CLEARANCE,
        "fit_type": "Close running fit",
        "description": "Fit with reduced clearance providing improved shaft guidance while maintaining free rotation.",
        "applications": "Pumps, electric motors, gearboxes and medium-precision industrial machinery.",
        "advantages": "Good balance between positioning accuracy and ease of movement.",
        "disadvantages": "Requires tighter dimensional control during manufacturing.",
        "assembly": "Manual assembly with proper lubrication.",
        "notes": "Widely used in continuously operating industrial machinery.",
        "standard": Standard.ISO_286,
    },

    "H7/g6": {
        "fit": "H7/g6",
        "category": FitCategory.CLEARANCE,
        "fit_type": "General running fit",
        "description": "Controlled-clearance fit for general-purpose rotating shafts.",
        "applications": "Electric motors, pumps, fans and general industrial mechanisms.",
        "advantages": "Excellent balance between precision, ease of assembly and smooth operation.",
        "disadvantages": "Not suitable when extremely accurate positioning is required.",
        "assembly": "Manual assembly with light lubrication.",
        "notes": "One of the most commonly used clearance fits in mechanical engineering.",
        "standard": Standard.ISO_286,
    },

    "H7/h6": {
        "fit": "H7/h6",
        "category": FitCategory.CLEARANCE,
        "fit_type": "Locational clearance fit",
        "description": "Fit with minimum clearance designed to provide accurate component positioning.",
        "applications": "Pulley hubs, gears, detachable couplings and components requiring precise centering.",
        "advantages": "Excellent positioning accuracy while remaining easy to disassemble.",
        "disadvantages": "Low tolerance to contamination and requires tighter machining accuracy.",
        "assembly": "Careful manual assembly, usually with light lubrication.",
        "notes": "Frequently selected when accurate centering is required without using a transition fit.",
        "standard": Standard.ISO_286,
    },

    "H7/js6": {
        "fit": "H7/js6",
        "category": FitCategory.TRANSITION,
        "fit_type": "Locational transition fit",
        "description": "Transition fit that may result in either slight clearance or slight interference while providing accurate positioning.",
        "applications": "Precision detachable couplings, gears, pulleys and hubs requiring excellent concentricity.",
        "advantages": "Excellent centering accuracy and repeatable assembly.",
        "disadvantages": "Depending on actual tolerances, light pressing may be required during assembly.",
        "assembly": "Manual assembly or light press fit.",
        "notes": "One of the most common transition fits when precise positioning is required.",
        "standard": Standard.ISO_286,
    },

    "H7/k6": {
        "fit": "H7/k6",
        "category": FitCategory.TRANSITION,
        "fit_type": "Medium transition fit",
        "description": "Transition fit providing precise positioning with slight interference in most cases.",
        "applications": "Pulleys, gears, couplings and components subjected to moderate loads.",
        "advantages": "Excellent centering and reliable torque transmission.",
        "disadvantages": "Removal may require mechanical tools.",
        "assembly": "Light press fit.",
        "notes": "Widely used when balancing precision and serviceability.",
        "standard": Standard.ISO_286,
    },

    "H7/m6": {
        "fit": "H7/m6",
        "category": FitCategory.TRANSITION,
        "fit_type": "Light interference transition fit",
        "description": "Transition fit tending toward light interference to improve joint rigidity.",
        "applications": "Gear hubs, pulleys, flywheels and dynamically loaded components.",
        "advantages": "Excellent concentricity and improved load transmission.",
        "disadvantages": "Assembly and disassembly generally require a press.",
        "assembly": "Mechanical press fit.",
        "notes": "Suitable where relative movement between components must be minimized.",
        "standard": Standard.ISO_286,
    },

    "H7/n6": {
        "fit": "H7/n6",
        "category": FitCategory.INTERFERENCE,
        "fit_type": "Light press fit",
        "description": "Light interference fit providing a firm joint without thermal assembly methods.",
        "applications": "Pulleys, gears, bushings and moderately loaded components.",
        "advantages": "Reliable torque transmission and excellent joint rigidity.",
        "disadvantages": "Disassembly usually requires a press or puller.",
        "assembly": "Mechanical or hydraulic press fit.",
        "notes": "Often considered the first practical interference fit.",
        "standard": Standard.ISO_286,
    },

    "H7/p6": {
        "fit": "H7/p6",
        "category": FitCategory.INTERFERENCE,
        "fit_type": "Medium press fit",
        "description": "Moderate interference fit providing a secure shaft-hub connection.",
        "applications": "Pulleys, gears, couplings and components subjected to moderate or heavy loads.",
        "advantages": "Excellent torque transmission and resistance to slipping.",
        "disadvantages": "Assembly and removal require mechanical equipment.",
        "assembly": "Hydraulic or mechanical press fit.",
        "notes": "Commonly used for permanent but serviceable mechanical joints.",
        "standard": Standard.ISO_286,
    },

    "H7/r6": {
        "fit": "H7/r6",
        "category": FitCategory.INTERFERENCE,
        "fit_type": "Heavy press fit",
        "description": "High interference fit intended for heavily loaded assemblies.",
        "applications": "Gear hubs, rotors, couplings and components subjected to vibration.",
        "advantages": "High torque capacity and excellent resistance to relative movement.",
        "disadvantages": "Disassembly generally requires heavy-duty pullers or heating.",
        "assembly": "Heavy press fit or thermal assistance.",
        "notes": "Recommended when joint rigidity is a priority.",
        "standard": Standard.ISO_286,
    },

    "H7/s6": {
        "fit": "H7/s6",
        "category": FitCategory.INTERFERENCE,
        "fit_type": "Force fit",
        "description": "High interference fit intended for nearly permanent assemblies.",
        "applications": "Electric motor rotors, railway wheels, flywheels and heavily loaded machinery.",
        "advantages": "Maximum torque transmission and excellent dynamic performance.",
        "disadvantages": "Disassembly often requires heating or specialized extraction equipment.",
        "assembly": "Thermal shrink fitting or heavy press fit.",
        "notes": "Recommended where frequent disassembly is not expected.",
        "standard": Standard.ISO_286,
    },

    "H7/u6": {
        "fit": "H7/u6",
        "category": FitCategory.INTERFERENCE,
        "fit_type": "Heavy drive fit",
        "description": "Very high interference fit for critical heavy-duty assemblies.",
        "applications": "Large rotors, heavy wheels, main shafts and high-power industrial equipment.",
        "advantages": "Maximum joint rigidity and outstanding load transmission.",
        "disadvantages": "Assembly and disassembly require specialized thermal procedures and equipment.",
        "assembly": "Shrink fitting using heating, cooling or both.",
        "notes": "Reserved for critical applications where structural integrity is paramount.",
        "standard": Standard.ISO_286,
    },

    "H7/c6": {
    "fit": "H7/c6",
    "category": FitCategory.CLEARANCE,
    "fit_type": "Wide clearance fit",
    "description": "Fit with generous clearance designed to ensure completely free movement even in the presence of dirt, corrosion or significant thermal expansion.",
    "applications": "Agricultural machinery, mining equipment, outdoor mechanisms, low-precision joints and construction equipment.",
    "advantages": "Excellent freedom of movement, high tolerance to contaminants and easy assembly.",
    "disadvantages": "Poor positioning accuracy and large clearance between components.",
    "assembly": "Manual assembly without special tools.",
    "notes": "Recommended when reliable movement is more important than positioning accuracy.",
    "standard": Standard.ISO_286,
},

"H7/d6": {
    "fit": "H7/d6",
    "category": FitCategory.CLEARANCE,
    "fit_type": "Wide running fit",
    "description": "Fit with considerable clearance for shafts that must rotate freely with minimal risk of seizure.",
    "applications": "Rollers, slow-speed pulleys, continuous-duty industrial mechanisms and equipment subjected to thermal variations.",
    "advantages": "Smooth operation and low risk of seizure due to thermal expansion.",
    "disadvantages": "Lower guiding accuracy than close-clearance fits.",
    "assembly": "Manual assembly with standard lubrication.",
    "notes": "Recommended when operational reliability is the primary concern.",
    "standard": Standard.ISO_286,
},

"H7/e6": {
    "fit": "H7/e6",
    "category": FitCategory.CLEARANCE,
    "fit_type": "Medium clearance fit",
    "description": "Fit with moderate clearance providing a good balance between free movement and positioning accuracy.",
    "applications": "Pumps, fans, gearboxes, electric motors and general industrial machinery.",
    "advantages": "Good dynamic performance and effective lubrication.",
    "disadvantages": "Does not provide the positioning accuracy of closer fits.",
    "assembly": "Manual assembly with light lubrication.",
    "notes": "Widely used in general-purpose industrial machinery.",
    "standard": Standard.ISO_286,
},

"H7/f6": {
    "fit": "H7/f6",
    "category": FitCategory.CLEARANCE,
    "fit_type": "Close clearance fit",
    "description": "Fit with small clearance designed to provide accurate guidance while maintaining completely free movement.",
    "applications": "Spindles, precision shafts, electric motors, centrifugal pumps and gearboxes.",
    "advantages": "Excellent balance between precision, smooth rotation and ease of assembly.",
    "disadvantages": "Requires tighter dimensional control during manufacturing.",
    "assembly": "Manual assembly with proper lubrication.",
    "notes": "One of the most widely used clearance fits in mechanical engineering.",
    "standard": Standard.ISO_286,
},

"H7/j6": {
    "fit": "H7/j6",
    "category": FitCategory.TRANSITION,
    "fit_type": "Light transition fit",
    "description": "Transition fit that may result in slight clearance or slight interference depending on the actual tolerance combination.",
    "applications": "Gears, pulleys, detachable couplings and components requiring accurate centering.",
    "advantages": "Excellent positioning accuracy and easy disassembly in most applications.",
    "disadvantages": "May require light assembly force depending on the actual tolerance combination.",
    "assembly": "Manual assembly or light press fitting.",
    "notes": "Represents the natural transition between clearance and interference fits.",
    "standard": Standard.ISO_286,
},

"H7/x6": {
    "fit": "H7/x6",
    "category": FitCategory.INTERFERENCE,
    "fit_type": "Heavy interference fit",
    "description": "Fit with high interference intended for permanent joints subjected to very heavy loads.",
    "applications": "Large rotors, railway wheels, main shafts and heavy industrial machinery.",
    "advantages": "Very high torque transmission capacity and maximum structural rigidity.",
    "disadvantages": "Disassembly generally requires heating or specialized equipment.",
    "assembly": "Shrink fitting or heavy press fitting.",
    "notes": "Recommended for critical applications where disassembly is not expected.",
    "standard": Standard.ISO_286,
},

"H7/z6": {
    "fit": "H7/z6",
    "category": FitCategory.INTERFERENCE,
    "fit_type": "Extreme interference fit",
    "description": "Fit with very high interference designed to create nearly permanent joints with maximum load transmission capability.",
    "applications": "High-power equipment, turbines, industrial rotors, heavily loaded shafts and critical mechanical components.",
    "advantages": "Maximum load transmission, excellent vibration resistance and outstanding joint rigidity.",
    "disadvantages": "Assembly and disassembly require carefully controlled thermal procedures.",
    "assembly": "Shrink fitting by heating the housing, cooling the shaft, or using both methods.",
    "notes": "Reserved for applications where safety and structural integrity are the highest priorities.",
    "standard": Standard.ISO_286,
    },

}