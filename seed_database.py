from pathlib import Path

import sqlite3


database_path = Path("database") / "mechanical_suite.db"

connection = sqlite3.connect(database_path)

tolerance_grades = [
    (30, 50, "IT1", 1.5),
    (30, 50, "IT2", 2.5),
    (30, 50, "IT3", 4),
    (30, 50, "IT4", 7),
    (30, 50, "IT5", 11),
    (30, 50, "IT6", 16),
    (30, 50, "IT7", 25),
    (30, 50, "IT8", 39),
    (30, 50, "IT9", 62),
    (30, 50, "IT10", 100),
    (30, 50, "IT11", 160),
    (30, 50, "IT12", 250),
    (30, 50, "IT13", 390),
    (30, 50, "IT14", 620),
]

for min_diameter, max_diameter, grade, value_um in tolerance_grades:
    connection.execute(
        """
        INSERT INTO tolerance_grades
        (min_diameter, max_diameter, grade, value_um)
        SELECT ?, ?, ?, ?
        WHERE NOT EXISTS (
            SELECT 1
            FROM tolerance_grades
            WHERE min_diameter = ?
              AND max_diameter = ?
              AND grade = ?
        )
        """,
        (
            min_diameter,
            max_diameter,
            grade,
            value_um,
            min_diameter,
            max_diameter,
            grade,
        ),
    )

connection.commit()

print(f"{len(tolerance_grades)} tolerance grades inserted successfully.")

connection.close()