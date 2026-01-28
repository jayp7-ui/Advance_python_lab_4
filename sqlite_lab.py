import sqlite3

# Connect to (or create) database
conn = sqlite3.connect('example.db')
cursor = conn.cursor()

# Create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS users(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER,
    salary REAL,
    is_active BOOLEAN,
    bio TEXT,
    join_date DATETIME,
    profile_picture BLOB,
    misc_data NUMERIC,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
""")

# Insert data
cursor.execute("""
INSERT INTO users(name, age, salary, is_active, bio, join_date, profile_picture, misc_data)
VALUES (?, ?, ?, ?, ?, ?, ?, ?)
""", ("Alice", 30, 55000.50, 1, "Software Engineer", "2026-01-05 05:00:00", None, 123.45))

conn.commit()

# Read data
print("\nAll Users:")
for row in cursor.execute("SELECT * FROM users"):
    print(row)

# Update data
cursor.execute("UPDATE users SET salary=? WHERE name=?", (70000.00, "Alice"))
conn.commit()

print("\nAfter Salary Update:")
print(cursor.execute("SELECT name, salary FROM users WHERE name='Alice'").fetchone())

# Delete data
cursor.execute("DELETE FROM users WHERE name=?", ("Bob",))
conn.commit()

print("\nAfter Deletion Attempt (Bob):")
for row in cursor.execute("SELECT id, name FROM users"):
    print(row)

conn.close()
