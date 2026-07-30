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
        "fit_type": "Ajuste con amplia holgura",
        "description": "Ajuste con amplia holgura para componentes con bajas exigencias de precisión.",
        "applications": "Mecanismos agrícolas, estructuras metálicas, uniones de fabricación económica y equipos donde la suciedad o la corrosión pueden estar presentes.",
        "advantages": "Montaje y desmontaje muy sencillos, bajo costo de fabricación y buena tolerancia a contaminantes.",
        "disadvantages": "Gran juego entre las piezas y baja precisión de posicionamiento.",
        "assembly": "Montaje completamente manual sin herramientas especiales.",
        "notes": "Recomendado únicamente cuando la precisión no es un requisito importante.",
        "standard": Standard.ISO_286,
    },

    "H9/d9": {
        "fit": "H9/d9",
        "category": FitCategory.CLEARANCE,
        "fit_type": "Ajuste de funcionamiento libre",
        "description": "Ajuste con holgura amplia para movimientos libres y continuos.",
        "applications": "Ejes de transmisión lenta, mecanismos expuestos a polvo, humedad o dilataciones térmicas importantes.",
        "advantages": "Excelente libertad de movimiento y mínima probabilidad de agarrotamiento.",
        "disadvantages": "No proporciona precisión de guiado ni buen centrado.",
        "assembly": "Montaje manual con lubricación convencional.",
        "notes": "Adecuado cuando la confiabilidad del movimiento es más importante que la precisión.",
        "standard": Standard.ISO_286,
    },

    "H8/e8": {
        "fit": "H8/e8",
        "category": FitCategory.CLEARANCE,
        "fit_type": "Ajuste de funcionamiento suave",
        "description": "Ajuste con holgura moderada para ejes que deben girar con suavidad.",
        "applications": "Ventiladores, bombas centrífugas, poleas y equipos industriales de velocidad moderada.",
        "advantages": "Movimiento suave, buena lubricación y bajo desgaste durante el funcionamiento.",
        "disadvantages": "No garantiza un posicionamiento preciso bajo cargas elevadas.",
        "assembly": "Montaje manual con lubricación ligera.",
        "notes": "Muy utilizado cuando se prioriza un funcionamiento suave y confiable.",
        "standard": Standard.ISO_286,
    },

    "H8/f7": {
        "fit": "H8/f7",
        "category": FitCategory.CLEARANCE,
        "fit_type": "Ajuste de funcionamiento preciso",
        "description": "Ajuste con holgura reducida para mejorar el guiado del eje manteniendo un giro libre.",
        "applications": "Bombas, motores eléctricos, reductores y maquinaria de precisión media.",
        "advantages": "Buen equilibrio entre precisión y facilidad de movimiento.",
        "disadvantages": "Requiere un mejor control dimensional durante la fabricación.",
        "assembly": "Montaje manual con lubricación adecuada.",
        "notes": "Muy empleado en maquinaria industrial de uso continuo.",
        "standard": Standard.ISO_286,
    },

    "H7/g6": {
        "fit": "H7/g6",
        "category": FitCategory.CLEARANCE,
        "fit_type": "Ajuste general de funcionamiento",
        "description": "Ajuste con holgura controlada para ejes giratorios de uso general.",
        "applications": "Motores eléctricos, bombas, ventiladores y mecanismos industriales de propósito general.",
        "advantages": "Excelente equilibrio entre precisión, facilidad de montaje y funcionamiento suave.",
        "disadvantages": "No es adecuado cuando se requiere una localización extremadamente precisa.",
        "assembly": "Montaje manual con ligera lubricación.",
        "notes": "Es uno de los ajustes con holgura más utilizados en ingeniería mecánica.",
        "standard": Standard.ISO_286,
    },

    "H7/h6": {
        "fit": "H7/h6",
        "category": FitCategory.CLEARANCE,
        "fit_type": "Ajuste de localización con holgura",
        "description": "Ajuste con holgura mínima destinado a obtener una buena localización de las piezas.",
        "applications": "Cubos de poleas, engranajes, acoples desmontables y componentes que requieren un buen centrado.",
        "advantages": "Excelente precisión de posicionamiento manteniendo facilidad de desmontaje.",
        "disadvantages": "Tolera poca suciedad y requiere mayor precisión de fabricación.",
        "assembly": "Montaje manual cuidadoso, normalmente con ligera lubricación.",
        "notes": "Frecuentemente utilizado cuando la precisión de centrado es importante sin llegar a un ajuste de transición.",
        "standard": Standard.ISO_286,
    },

    "H7/js6": {
    "fit": "H7/js6",
    "category": FitCategory.TRANSITION,
    "fit_type": "Ajuste de transición de localización",
    "description": "Ajuste de transición con posibilidad de obtener una ligera holgura o una ligera interferencia, destinado a lograr un posicionamiento preciso.",
    "applications": "Acoples desmontables de precisión, engranajes, poleas, cubos y componentes que requieren una excelente concentricidad.",
    "advantages": "Excelente precisión de centrado y buena repetibilidad en el montaje.",
    "disadvantages": "Dependiendo de las tolerancias reales puede requerir una ligera presión durante el montaje.",
    "assembly": "Montaje manual o con pequeños golpes utilizando un mazo de goma o prensa ligera.",
    "notes": "Es uno de los ajustes de transición más utilizados cuando se requiere precisión sin un montaje permanente.",
    "standard": Standard.ISO_286,
},

"H7/k6": {
    "fit": "H7/k6",
    "category": FitCategory.TRANSITION,
    "fit_type": "Ajuste de transición medio",
    "description": "Ajuste de transición que proporciona un posicionamiento preciso con una ligera interferencia en la mayoría de los casos.",
    "applications": "Poleas, engranajes, acoples, ruedas dentadas y componentes sometidos a cargas moderadas.",
    "advantages": "Muy buen centrado y transmisión segura de cargas moderadas.",
    "disadvantages": "El desmontaje puede requerir herramientas mecánicas.",
    "assembly": "Montaje mediante prensa ligera o pequeños golpes controlados.",
    "notes": "Muy utilizado cuando se busca un equilibrio entre desmontabilidad y precisión.",
    "standard": Standard.ISO_286,
},

"H7/m6": {
    "fit": "H7/m6",
    "category": FitCategory.TRANSITION,
    "fit_type": "Ajuste de transición con interferencia ligera",
    "description": "Ajuste con tendencia a producir una ligera interferencia para mejorar la rigidez de la unión.",
    "applications": "Cubos de engranajes, poleas, volantes y elementos sometidos a cargas dinámicas moderadas.",
    "advantages": "Excelente concentricidad y mayor capacidad para transmitir esfuerzos.",
    "disadvantages": "Generalmente requiere prensa para el montaje y desmontaje.",
    "assembly": "Montaje mediante prensa mecánica.",
    "notes": "Adecuado cuando se desea minimizar cualquier movimiento relativo entre las piezas.",
    "standard": Standard.ISO_286,
},

"H7/n6": {
    "fit": "H7/n6",
    "category": FitCategory.INTERFERENCE,
    "fit_type": "Ajuste de apriete ligero",
    "description": "Ajuste con interferencia ligera destinado a obtener una unión firme sin recurrir a métodos térmicos.",
    "applications": "Poleas, engranajes, bujes y elementos sometidos a cargas relativamente elevadas.",
    "advantages": "Buena transmisión de torque y excelente rigidez de la unión.",
    "disadvantages": "El desmontaje normalmente requiere extractor o prensa.",
    "assembly": "Montaje mediante prensa hidráulica o mecánica.",
    "notes": "Con frecuencia constituye el primer ajuste de interferencia recomendado.",
    "standard": Standard.ISO_286,
},

"H7/p6": {
    "fit": "H7/p6",
    "category": FitCategory.INTERFERENCE,
    "fit_type": "Ajuste de apriete medio",
    "description": "Ajuste con interferencia moderada para obtener una unión firme entre el eje y el alojamiento.",
    "applications": "Poleas, engranajes, acoples, ruedas y componentes sometidos a cargas moderadas o elevadas.",
    "advantages": "Excelente transmisión de torque y alta resistencia al deslizamiento.",
    "disadvantages": "El montaje y desmontaje requieren herramientas mecánicas adecuadas.",
    "assembly": "Montaje mediante prensa hidráulica o mecánica.",
    "notes": "Muy utilizado cuando se requiere una unión permanente pero desmontable con herramientas.",
    "standard": Standard.ISO_286,
},

"H7/r6": {
    "fit": "H7/r6",
    "category": FitCategory.INTERFERENCE,
    "fit_type": "Ajuste de fuerte apriete",
    "description": "Ajuste con interferencia elevada para aplicaciones sometidas a cargas importantes.",
    "applications": "Cubos de engranajes, ruedas dentadas, rotores, acoples y elementos sometidos a vibraciones.",
    "advantages": "Gran capacidad para transmitir esfuerzos sin movimiento relativo entre las piezas.",
    "disadvantages": "El desmontaje normalmente requiere extractor de alta capacidad o calentamiento.",
    "assembly": "Montaje mediante prensa de mayor capacidad o calentamiento del alojamiento.",
    "notes": "Recomendado cuando la rigidez de la unión es prioritaria.",
    "standard": Standard.ISO_286,
},

"H7/s6": {
    "fit": "H7/s6",
    "category": FitCategory.INTERFERENCE,
    "fit_type": "Ajuste de interferencia fuerte",
    "description": "Ajuste con elevada interferencia destinado a obtener una unión prácticamente permanente.",
    "applications": "Rotores eléctricos, ruedas ferroviarias, volantes de inercia y componentes sometidos a grandes esfuerzos.",
    "advantages": "Máxima capacidad de transmisión de torque y excelente comportamiento frente a cargas dinámicas.",
    "disadvantages": "El desmontaje suele requerir calentamiento, extracción especializada o incluso destrucción de alguna pieza.",
    "assembly": "Montaje mediante calentamiento del alojamiento, enfriamiento del eje o combinación de ambos métodos.",
    "notes": "Adecuado para aplicaciones donde no se prevé un desmontaje frecuente.",
    "standard": Standard.ISO_286,
},

"H7/u6": {
    "fit": "H7/u6",
    "category": FitCategory.INTERFERENCE,
    "fit_type": "Ajuste de interferencia muy fuerte",
    "description": "Ajuste con interferencia muy elevada para uniones prácticamente permanentes sometidas a cargas extremas.",
    "applications": "Grandes rotores, ruedas pesadas, ejes principales y equipos industriales de alta potencia.",
    "advantages": "Máxima rigidez estructural y excelente transmisión de esfuerzos elevados.",
    "disadvantages": "Montaje y desmontaje complejos que requieren procedimientos térmicos y equipos especializados.",
    "assembly": "Montaje por contracción térmica mediante calentamiento del alojamiento y/o enfriamiento del eje.",
    "notes": "Reservado para aplicaciones críticas donde la seguridad y la rigidez son prioritarias.",
    "standard": Standard.ISO_286,
    },

    "H7/c6": {
    "fit": "H7/c6",
    "category": FitCategory.CLEARANCE,
    "fit_type": "Ajuste de gran holgura",
    "description": "Ajuste con holgura amplia diseñado para garantizar un movimiento completamente libre incluso en presencia de suciedad, corrosión o dilataciones térmicas importantes.",
    "applications": "Maquinaria agrícola, equipos para minería, mecanismos expuestos al exterior, articulaciones de baja precisión y equipos de construcción.",
    "advantages": "Excelente libertad de movimiento, gran tolerancia a contaminantes y facilidad de montaje.",
    "disadvantages": "Posicionamiento poco preciso y elevada holgura entre los componentes.",
    "assembly": "Montaje manual sin herramientas especiales.",
    "notes": "Adecuado cuando la confiabilidad del movimiento es más importante que la precisión.",
    "standard": Standard.ISO_286,
},

"H7/d6": {
    "fit": "H7/d6",
    "category": FitCategory.CLEARANCE,
    "fit_type": "Ajuste de holgura amplia",
    "description": "Ajuste con holgura considerable para ejes que deben girar libremente con bajo riesgo de agarrotamiento.",
    "applications": "Rodillos, poleas lentas, mecanismos industriales de servicio continuo y equipos sometidos a variaciones térmicas.",
    "advantages": "Funcionamiento suave y bajo riesgo de bloqueo por expansión térmica.",
    "disadvantages": "Menor precisión de guiado que ajustes de holgura reducida.",
    "assembly": "Montaje manual con lubricación convencional.",
    "notes": "Recomendado cuando se prioriza la confiabilidad del funcionamiento.",
    "standard": Standard.ISO_286,
},

"H7/e6": {
    "fit": "H7/e6",
    "category": FitCategory.CLEARANCE,
    "fit_type": "Ajuste de holgura media",
    "description": "Ajuste con holgura moderada que proporciona un buen equilibrio entre libertad de movimiento y precisión.",
    "applications": "Bombas, ventiladores, reductores, motores eléctricos y maquinaria industrial general.",
    "advantages": "Buen comportamiento dinámico y lubricación eficiente.",
    "disadvantages": "No proporciona la precisión de posicionamiento de ajustes más cerrados.",
    "assembly": "Montaje manual con lubricación ligera.",
    "notes": "Muy utilizado en maquinaria industrial de propósito general.",
    "standard": Standard.ISO_286,
},

"H7/f6": {
    "fit": "H7/f6",
    "category": FitCategory.CLEARANCE,
    "fit_type": "Ajuste de holgura reducida",
    "description": "Ajuste con pequeña holgura destinado a proporcionar un guiado preciso manteniendo un movimiento completamente libre.",
    "applications": "Husillos, ejes de precisión, motores eléctricos, bombas centrífugas y cajas de engranajes.",
    "advantages": "Excelente equilibrio entre precisión, suavidad de giro y facilidad de montaje.",
    "disadvantages": "Requiere un mayor control dimensional durante la fabricación.",
    "assembly": "Montaje manual con lubricación adecuada.",
    "notes": "Constituye uno de los ajustes de holgura más utilizados en ingeniería mecánica.",
    "standard": Standard.ISO_286,
},

"H7/j6": {
    "fit": "H7/j6",
    "category": FitCategory.TRANSITION,
    "fit_type": "Ajuste de transición ligero",
    "description": "Ajuste de transición que puede producir una ligera holgura o una ligera interferencia dependiendo de las tolerancias reales.",
    "applications": "Engranajes, poleas, acoples desmontables y componentes que requieren un centrado preciso.",
    "advantages": "Excelente precisión de posicionamiento y facilidad de desmontaje en la mayoría de aplicaciones.",
    "disadvantages": "Puede requerir ligeros esfuerzos durante el montaje dependiendo de la combinación real de tolerancias.",
    "assembly": "Montaje manual o mediante prensa ligera.",
    "notes": "Representa la transición natural entre los ajustes con holgura y los ajustes de apriete.",
    "standard": Standard.ISO_286,
},

"H7/x6": {
    "fit": "H7/x6",
    "category": FitCategory.INTERFERENCE,
    "fit_type": "Ajuste de fuerte interferencia",
    "description": "Ajuste con elevada interferencia destinado a uniones permanentes sometidas a esfuerzos muy elevados.",
    "applications": "Grandes rotores, ruedas ferroviarias, ejes principales y maquinaria pesada.",
    "advantages": "Muy elevada capacidad de transmisión de torque y máxima rigidez estructural.",
    "disadvantages": "El desmontaje normalmente requiere calentamiento o equipos especializados.",
    "assembly": "Montaje por contracción térmica o mediante prensa de alta capacidad.",
    "notes": "Adecuado para aplicaciones críticas donde no se espera desmontaje frecuente.",
    "standard": Standard.ISO_286,
},

"H7/z6": {
    "fit": "H7/z6",
    "category": FitCategory.INTERFERENCE,
    "fit_type": "Ajuste de interferencia extrema",
    "description": "Ajuste con interferencia muy elevada diseñado para obtener uniones prácticamente permanentes con máxima capacidad de transmisión de carga.",
    "applications": "Equipos de gran potencia, turbinas, rotores industriales, ejes de alta carga y componentes críticos.",
    "advantages": "Máxima transmisión de esfuerzos, excelente resistencia a vibraciones y gran rigidez de la unión.",
    "disadvantages": "Montaje y desmontaje complejos que requieren procedimientos térmicos cuidadosamente controlados.",
    "assembly": "Montaje mediante calentamiento del alojamiento, enfriamiento del eje o combinación de ambos métodos.",
    "notes": "Se reserva para aplicaciones donde la seguridad y la integridad estructural son prioritarias.",
    "standard": Standard.ISO_286,
    },

}
