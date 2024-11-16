import sqlite3

conn = sqlite3.connect('test.db')

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER
)
""")

# cursor.execute("INSERT INTO users (name, age) VALUES ('John', 25)")
# cursor.execute("INSERT INTO users (name, age) VALUES ('Jane', 30)")
# cursor.execute("DELETE FROM users WHERE age = 30")
cursor.execute("SELECT * FROM users")
rows = cursor.fetchall()

for row in rows:
    print(f"ID: {row[0]}, Name: {row[1]}, Age: {row[2]}")

conn.commit()
conn.close()
