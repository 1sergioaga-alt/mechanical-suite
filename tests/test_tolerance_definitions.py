import sqlite3
from pathlib import Path


DATABASE_PATH = (
    Path(__file__).resolve().parents[1]
    / "database"
    / "mechanical_suite.db"
    )


def test_tolerance_definitions_have_no_duplicates():
    connection = sqlite3.connect(DATABASE_PATH)

    rows = connection.execute(
        """
        SELECT
            letter,
            element_type,
            grade,
            min_diameter,
            max_diameter,
            COUNT(*)
        FROM tolerance_definitions
        GROUP BY
            letter,
            element_type,
            grade,
            min_diameter,
            max_diameter
        HAVING COUNT(*) > 1
        """
    ).fetchall()

    connection.close()

    assert rows == []