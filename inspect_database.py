from pathlib import Path
import sqlite3

database_path = Path("database") / "mechanical_suite.db"

connection = sqlite3.connect(database_path)

cursor = connection.execute(
    "SELECT name FROM sqlite_master WHERE type='table';"
)

for row in cursor:
    print(row[0])

print("\nTolerance grades:\n")

cursor = connection.execute("SELECT * FROM tolerance_grades")

for row in cursor:
    print(row)

print("\nFundamental deviations:\n")

cursor = connection.execute(
    "SELECT * FROM fundamental_deviations"
)

for row in cursor:
    print(row)

connection.close()