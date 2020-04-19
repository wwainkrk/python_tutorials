import sqlite3


# Creating a simply connection with database which will be hold on device/disk
# or in memory (:memory:)
con = sqlite3.connect("test.db")

# Access to the column through index and names
con.row_factory = sqlite3.Row

# Creating a cursor object
cur = con.cursor()