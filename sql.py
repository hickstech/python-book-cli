import sqlite3

conn = sqlite3.connect("books.db")
c = conn.cursor()

c.execute("""CREATE TABLE if not exists books(
            title TEXT,
            pages INTEGER
        )
""")

# c.execute("INSERT INTO books VALUES ('Are You My Mother?', 72)")
# conn.commit()
# books = [
#    ("The Cat in the Hat", 61),
#    ("Green Eggs and Ham", 62),
#    ("One Fish Two Fish Red Fish Blue Fish", 62),
# ]
# c.executemany("INSERT INTO books VALUES (?, ?)", books)
# conn.commit()
#
# c.execute("SELECT rowid, * FROM books")
# print(c.fetchall())
#
# c.execute("SELECT rowid, * FROM books LIMIT 1")
# print(c.fetchall())
#
# c.execute("DELETE FROM books WHERE rowid = ?", (1,))
# conn.commit()
#
# c.execute("SELECT * FROM books")
# print(c.fetchall())
# c.execute(
#    "UPDATE books SET pages=64 WHERE title = 'One Fish Two Fish Red Fish Blue Fish'"
# )
conn.commit()
c.execute("SELECT * FROM books WHERE title = 'One Fish Two Fish Red Fish Blue Fish'")
data = c.fetchone()
print(data)
