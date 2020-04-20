import sqlite3


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
    DROP TABLE IF EXISTS student;
    CREATE TABLE IF NOT EXISTS uczen(
        id INTEGER PRIMARY KEY ASC,
        first_name varchar(250) NOT NULL,
        last_name varchar(250) NOT NULL,
        class_id INTEGER NOT NULL,
        FOREIGN KEY(klasa_id) REFERENCES klasa(id)
    )""")

# We put some data in table
cur.execute("INSERT INTO class (name, profile) VALUES(?, ?)", ('1A', 'humanistic'))
cur.execute("INSERT INTO class (name, profile) VALUES(?, ?)", ('1B', 'math'))

# We take a class which has specific name
cur.execute("SELECT * FROM class WHERE name = ?", ('1A',))
class_id = cur.fetchone()[0]
print(class_id)


