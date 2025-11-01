import sqlite3

conn = sqlite3.connect("database.db")  # Agar fayl bo‘lmasa, avtomatik yaratiladi
cur = conn.cursor()  # Kursor obyektini yaratamiz

s1 = """
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        age INTEGER
    )
"""
s12="""
insert into users(name,age) 
values ('ali1',21),('ali2',12);
"""

s2="SELECT * FROM users"
conn.commit()  # O‘zgarishlarni saqlash

# cur.execute(s1)
cur.executescript(s12) # malumot Qo'shish
print("bajarildi")
# rows = cur.fetchall()  # Natijalarni olish
# print(rows)
# for row in rows:
#
#     print(row)  # Har bir qatorni chiqarish
cur.close()
conn.close()
