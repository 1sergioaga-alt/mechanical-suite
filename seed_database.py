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

connection.commit()

print("Tolerance grade inserted successfully.")

connection.close()