import sqlite3
from pathlib import Path


DATABASE_PATH = (
    Path(__file__).resolve().parents[1]
    / "database"
    / "mechanical_suite.db"
    )


def test_tolerance_grades_have_no_duplicates():
    connection = sqlite3.connect(DATABASE_PATH)

    rows = connection.execute(
        """
        SELECT
            min_diameter,
            max_diameter,
            grade,
            COUNT(*)
        FROM tolerance_grades
        GROUP BY
            min_diameter,
            max_diameter,
            grade
        HAVING COUNT(*) > 1
        """
    ).fetchall()

    connection.close()

    assert rows == []