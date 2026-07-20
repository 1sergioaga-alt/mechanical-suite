from pathlib import Path
import sqlite3

database_path = Path("database") / "mechanical_suite.db"

connection = sqlite3.connect(database_path)

connection.execute(
    """
    INSERT INTO tolerance_grades
    (min_diameter, max_diameter, grade, value_um)
    VALUES (?, ?, ?, ?)
    """,
    (30, 50, "IT7", 25)
)

connection.execute(
    """
    INSERT INTO fundamental_deviations
    (
        letter,
        element_type,
        min_diameter,
        max_diameter,
        lower_deviation_um,
        upper_deviation_um
    )
    VALUES (?, ?, ?, ?, ?, ?)
    """,
    ("H", "hole", 30, 50, 0, 0)
)

connection.execute(
    """
    INSERT INTO fundamental_deviations
    (
        letter,
        element_type,
        min_diameter,
        max_diameter,
        lower_deviation_um,
        upper_deviation_um
    )
    VALUES (?, ?, ?, ?, ?, ?)
    """,
    ("g", "shaft", 30, 50, -25, -9)
)

connection.commit()

print("Tolerance grade inserted successfully.")

connection.close()