from mechanical_suite.fits.models.fit import Fit
from pathlib import Path
import sqlite3

class ISO286:
    """Provides ISO 286 calculations."""
    def __init__(self):
        database_path = Path("database") / "mechanical_suite.db"
        self.connection = sqlite3.connect(database_path)

    def get_hole_deviations(self, fit: Fit):
        it = self._get_tolerance_grade(
        fit.nominal_diameter,
        f"IT{fit.hole.grade}",
        )
        lower, upper = self._get_fundamental_deviation(
        fit.nominal_diameter,
        fit.hole.letter,
        "hole",
        )
        upper = lower + it
        
        return lower, upper

    def get_shaft_deviations(self, fit: Fit):
        lower, upper = self._get_fundamental_deviation(
        fit.nominal_diameter,
        fit.shaft.letter,
        "shaft",
        )

        return lower, upper

    def get_fit_limits(self, fit: Fit):
        pass

    def get_fit_type(self, fit: Fit):
        pass

    def calculate(self, fit: Fit):
        pass

    def _get_tolerance_grade(
        self,
        diameter: float,
        grade: str,
    ):
        cursor = self.connection.execute(
        """
        SELECT value_um
        FROM tolerance_grades
        WHERE
        min_diameter <= ?
        AND max_diameter >= ?
        AND grade = ?
        """,
        (diameter, diameter, grade),
        )

        row = cursor.fetchone()

        if row is None:
            raise ValueError("Tolerance grade not found.")
        
        return row[0]
    
    def _get_fundamental_deviation(
        self,
        diameter: float,
        letter: str,
        element_type: str,
    ):
        cursor = self.connection.execute(
            """
            SELECT lower_deviation_um, upper_deviation_um
            FROM fundamental_deviations
            WHERE
                min_diameter <= ?
                AND max_diameter >= ?
                AND letter = ?
                AND element_type = ?
            """,
            (diameter, diameter, letter, element_type),
        )

        row = cursor.fetchone()

        if row is None:
            raise ValueError("Fundamental deviation not found.")
        lower_deviation, upper_deviation = row
        return lower_deviation, upper_deviation