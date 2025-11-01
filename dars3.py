DB_NAME = "contactdb"
DB_USER = "postgres"
DB_PASS = "12345"
DB_HOST = "localhost"
DB_PORT = "5432"
import psycopg2
from psycopg2 import sql
from datetime import datetime

#  PostgreSQL ulanish ma'lumotlari
DB_NAME = "contactdb"
DB_USER = "postgres"
DB_PASS = "12345"
DB_HOST = "localhost"
DB_PORT = "5432"


def get_connection():
    return psycopg2.connect(
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASS,
        host=DB_HOST,
        port=DB_PORT
    )


# 🔹 Jadval yaratish
def create_table():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS contacts (
            id SERIAL PRIMARY KEY,
            name VARCHAR(100),
            phone VARCHAR(20) UNIQUE,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
    """)
    conn.commit()
    conn.close()
    print("Jadval tayyor (contacts).")


#  Kontakt qo‘shish
def add_contact(name, phone):
    conn = get_connection()
    cur = conn.cursor()
    try:
        cur.execute("""
            INSERT INTO contacts (name, phone)
            VALUES (%s, %s)
        """, (name, phone))
        conn.commit()
        print(f" Qo‘shildi: {name} — {phone}")
    except psycopg2.errors.UniqueViolation:
        print(" Bu telefon raqami allaqachon mavjud.")
    finally:
        conn.close()


#  Barcha kontaktlarni ko‘rish
def list_contacts():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT id, name, phone, created_at FROM contacts ORDER BY id")
    rows = cur.fetchall()

    if not rows:
        print("Kontaktlar yo‘q.")
    else:
        print(f"{'ID':<5} {'NAME':<20} {'PHONE':<15} {'CREATED_AT'}")
        print("-" * 60)
        for r in rows:
            print(f"{r[0]:<5} {r[1]:<20} {r[2]:<15} {r[3]}")

    conn.close()


# 🔹 Kontaktni o‘chirish
def delete_contact(contact_id):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM contacts WHERE id = %s", (contact_id,))
    conn.commit()
    if cur.rowcount > 0:
        print(f" ID={contact_id} o‘chirildi.")
    else:
        print(f" ID={contact_id} topilmadi.")
    conn.close()


# Bosh menyu
def main():
    while True:
        print("""
=====  CONTACT MANAGER =====
1. Jadval yaratish
2. Kontakt qo‘shish
3. Barcha kontaktlarni ko‘rish
4. Kontaktni o‘chirish
5. Chiqish
""")
        tanlov = input("Tanlang (1-5): ")

        if tanlov == "1":
            create_table()
        elif tanlov == "2":
            name = input("Ism kiriting: ")
            phone = input("Telefon raqam kiriting: ")
            add_contact(name, phone)
        elif tanlov == "3":
            list_contacts()
        elif tanlov == "4":
            cid = input("O‘chiriladigan kontakt ID sini kiriting: ")
            delete_contact(cid)
        elif tanlov == "5":
            print("Dastur tugadi.")
            break
        else:
            print(" Noto‘g‘ri tanlov!")


if __name__ == "__main__":
    main()

