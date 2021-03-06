import sqlite3
from csvbase import *

# Creating a simply connection with database which will be hold on device/disk
# or in memory (:memory:)
con = sqlite3.connect("test.db")

# Access to the column through index and names
con.row_factory = sqlite3.Row

# Creating a cursor object
cur = con.cursor()

# Create a tables
cur.execute("DROP TABLE IF EXISTS klasa")

cur.execute("""
        CREATE TABLE IF NOT EXISTS class(
            id INTEGER PRIMARY KEY ASC,
            name varchar(250) NOT NULL,
            profile varchar(250) DEFAULT ''
        )""")

# Execute more than one command - all SQL script
cur.executescript("""
    DROP TABLE IF EXISTS students;
    CREATE TABLE IF NOT EXISTS students(
        id INTEGER PRIMARY KEY ASC,
        first_name varchar(250) NOT NULL,
        last_name varchar(250) NOT NULL,
        class_id INTEGER NOT NULL,
        FOREIGN KEY(class_id) REFERENCES class(id)
    )""")

# We put some data in table
cur.execute("INSERT INTO class (name, profile) VALUES(?, ?)", ('1A', 'humanistic'))
cur.execute("INSERT INTO class (name, profile) VALUES(?, ?)", ('1B', 'math'))

con.commit()

# We take a class which has specific name
cur.execute("SELECT id FROM class WHERE name = ?", ('1A',))
class_id = cur.fetchone()[0]
#print(class_id)

students = (
    ('Tomasz', 'Nowak', class_id),
    ('Jan', 'Kos', class_id),
    ('Piotr', 'Kowalski', class_id)
)

# We put some data into second table
cur.executemany("INSERT INTO students (first_name, last_name, class_id) VALUES(?, ?, ?)", students)

# confirm changes in database
con.commit()


# Download data from database
def read_data():
    """
    We download data from database
    """
    cur.execute("SELECT students.id, first_name, last_name, name FROM students, "
                "class WHERE students.class_id = class.id")
    students_list = cur.fetchall()

    for student in students_list:
        # We can take value from a list by name column, because we declare row_factory as row, at the beginning
        print(student['id'], student['first_name'], student['last_name'], student['name'])


read_data()

# Changes in student class with student index = 2
cur.execute("SELECT id FROM class WHERE name = ?", ('1B',))
class_id = cur.fetchone()[0]
cur.execute("UPDATE students SET class_id=? WHERE id=?", (class_id, 2))

# Delete a record from student table with id = 3 / Delete a student with index = 3
cur.execute("DELETE FROM students WHERE id=?", (3,))

read_data()

students_csv = read_csv("students.csv")
cur.executescript("""
    DROP TABLE IF EXISTS students;
    CREATE TABLE IF NOT EXISTS students(
        id INTEGER PRIMARY KEY ASC,
        first_name varchar(250) NOT NULL,
        last_name varchar(250) NOT NULL,
        class_id INTEGER NOT NULL,
        FOREIGN KEY(class_id) REFERENCES class(id)
    );""")

cur.executemany("INSERT INTO students (first_name, last_name, class_id) VALUES (?, ?, ?)", students_csv)

read_data()
