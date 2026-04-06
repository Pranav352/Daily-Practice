import sqlite3

# create Table
# con = sqlite3.connect("emp.db")

# cursor = con.cursor()

# cursor.execute(("""
# CREATE TABLE IF NOT EXISTS students (
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     name TEXT,
#     age INTEGER
# )
# """)
# )
# con.commit()
# con.close()


# Insert Data
# con = sqlite3.connect("emp.db")

# cursor = con.cursor()
# name = "jems"
# age = 20

# cursor.execute ("INSERT INTO students (name, age) VALUES (?, ?)",(name,age))

# con.commit()
# con.close()

# print("Record inserted successfully")

# Read Data
con = sqlite3.connect("emp.db")
cursor = con.cursor()
cursor.execute("SELECT * FROM students")
rows = cursor.fetchall()

for row in rows:
    print(row)

con.close()


# Updata data
# con = sqlite3.connect("Student.db")
# cursor = con.cursor()
# cursor.execute("UPDATE students SET age = ? WHERE id = ?", (22, 1))
# con.commit()
# con.close()

# print("Record updated successfully")


# # Delete Data
# con = sqlite3.connect("Student.db")
# cursor = con.cursor()

# cursor.execute("DELETE FROM students WHERE id = ?", (2,))
# con.commit()
# con.close()

# print("Record deleted successfully")



