import psycopg2
conn = psycopg2.connect(
    dbname="postgres",
    user="postgres",
    password="123",
    host="localhost", #127.0.0.1
    port="5432"
)
cur = conn.cursor()
sql1 = '''
select * from categories
'''

s2 = '''

'''

# Malumot qo‘shish

cur.execute(sql1)
s = cur.fetchall()
print(s)
for item in s:
    print(item[0],item[1])

conn.commit()
cur.close()
conn.close()
