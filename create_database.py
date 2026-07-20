from pathlib import Path
import sqlite3

# Create the database directory if it doesn't exist
database_dir = Path("database")
database_dir.mkdir(exist_ok=True)

# Create (or open) the database
database_path = database_dir / "mechanical_suite.db"

connection = sqlite3.connect(database_path)

connection.execute("""
CREATE TABLE IF NOT EXISTS tolerance_grades (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    min_diameter REAL NOT NULL,
    max_diameter REAL NOT NULL,
    grade TEXT NOT NULL,
    value_um INTEGER NOT NULL
)
""")

connection.execute("""
CREATE TABLE IF NOT EXISTS fundamental_deviations (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    letter TEXT NOT NULL,
    element_type TEXT NOT NULL,
    min_diameter REAL NOT NULL,
    max_diameter REAL NOT NULL,
    lower_deviation_um INTEGER NOT NULL,
    upper_deviation_um INTEGER NOT NULL
)
""")

connection.commit()

print(f"Database created at: {database_path}")

connection.close()