import psycopg2

class Data_connect:
    def __init__(self, dbname, user, password, host='localhost', port=5432):
        self.connection = psycopg2.connect(
            dbname=dbname,
            user=user,
            password=password,
            host=host,
            port=port
        )
        self.cursor = self.connection.cursor()

    # ----CUSTOMER----
    def add_customer(self, name):
        s = '''
        INSERT INTO customers(name)
        VALUES(%s)
        '''
        self.cursor.execute(s, (name,))
        self.connection.commit()
        print(" Customer qo‘shildi.")

    def view_customer(self):
        s = 'SELECT * FROM customers'
        self.cursor.execute(s)
        rows = self.cursor.fetchall()
        print("\n--- CUSTOMER RO‘YXATI ---")
        for item in rows:
            print(f"ID: {item[0]} | Name: {item[1]}")

    def update_customers(self, id, new_title):
        s = 'UPDATE customers SET name=%s WHERE id=%s'
        self.cursor.execute(s, (new_title, id))
        self.connection.commit()
        print(" Customer yangilandi.")

    def delete_customers(self, id):
        s = 'DELETE FROM customers WHERE id=%s'
        self.cursor.execute(s, (id,))
        self.connection.commit()
        print(" Customer o‘chirildi.")

    # ----ORDER----
    def add_order(self, title, tipy):
        query = '''
        INSERT INTO orders(title, tipy, order_date)
        VALUES(%s, %s, CURRENT_DATE)
        '''
        self.cursor.execute(query, (title, tipy))
        self.connection.commit()
        print(" Order qo‘shildi.")

    def order_view(self):
        s = '''
        SELECT * FROM orders;
        '''
        self.cursor.execute(s)
        con = self.cursor.fetchall()
        print("\n--- ORDER RO‘YXATI ---")
        for item in con:
            print(f"ID: {item[0]} | Nomi: {item[1]} | Turi: {item[2]} | Sana: {item[3]}")

    def update_order(self, id, title, tipy):
        s = 'UPDATE orders SET title=%s, tipy=%s WHERE id=%s'
        self.cursor.execute(s, (title, tipy, id))
        self.connection.commit()
        print(" Order yangilandi.")

    def delete_order(self, id):
        s = '''
        DELETE FROM orders WHERE id=%s
        '''
        self.cursor.execute(s, (id,))
        self.connection.commit()
        print(" Order o‘chirildi.")

    # ---ORDER_DETAILS---
    def add_order_details(self, order_id, unit_price, quantity, discount):
        query = '''
        INSERT INTO order_details(order_id, unit_price, quantity, discount)
        VALUES(%s, %s, %s, %s)
        '''
        self.cursor.execute(query, (order_id, unit_price, quantity, discount))
        self.connection.commit()
        print(" Order detail qo‘shildi.")

    def order_detail(self, order_id):
        query = '''
        SELECT o.id, o.title, o.tipy, o.order_date,
               od.unit_price, od.quantity, od.discount
        FROM orders o
        JOIN order_details od ON o.id = od.order_id
        WHERE o.id = %s
        '''
        self.cursor.execute(query, (order_id,))
        result = self.cursor.fetchall()
        if result:
            print("\n--- ORDER DETAIL ---")
            for item in result:
                print(f"Order ID: {item[0]} | Nomi: {item[1]} | Turi: {item[2]} | Sana: {item[3]}")
                print(f"Narx: {item[4]} | Miqdor: {item[5]} | Chegirma: {item[6]}")
                print("-" * 40)
        else:
            print(" Bu ID bo‘yicha ma’lumot topilmadi.")

    def filter_orders_by_date(self, start_date, end_date):
        query = '''
        SELECT * FROM orders
        WHERE order_date BETWEEN %s AND %s
        ORDER BY order_date;
        '''
        self.cursor.execute(query, (start_date, end_date))
        rows = self.cursor.fetchall()
        if rows:
            print("\n--- SANA ORALIG‘IDAGI ORDERLAR ---")
            for item in rows:
                print(f"ID: {item[0]} | Nomi: {item[1]} | Turi: {item[2]} | Sana: {item[3]}")
        else:
            print(" Berilgan sanalar oralig‘ida hech qanday zakaz topilmadi.")

    # ----EMPLOYEE----
    def add_employee(self, name, last_name, country, departament, salary, email, phone):
        query = '''
        INSERT INTO employees(name, last_name, country, departament, salary, email, phone)
        VALUES(%s, %s, %s, %s, %s, %s, %s)
        '''
        self.cursor.execute(query, (name, last_name, country, departament, salary, email, phone))
        self.connection.commit()
        print(" Xodim qo‘shildi.")

    def view_employee(self):
        s = '''
        SELECT * FROM employees
        '''
        self.cursor.execute(s)
        con = self.cursor.fetchall()
        print("\n--- XODIMLAR RO‘YXATI ---")
        for item in con:
            print(f"ID:{item[0]} | Name:{item[1]} | Lastname:{item[2]} | Country:{item[3]} | Departament:{item[4]} | "
                  f"Salary:{item[5]} | Email:{item[6]} | Phone:{item[7]}")

    def update_employee(self, id, name, last_name, country, departament, salary, email, phone):
        s = '''
        UPDATE employees
        SET name=%s, last_name=%s, country=%s, departament=%s, salary=%s, email=%s, phone=%s
        WHERE id=%s
        '''
        self.cursor.execute(s, (name, last_name, country, departament, salary, email, phone, id))
        self.connection.commit()
        print(" Xodim ma’lumotlari yangilandi.")

    def delete_employees(self, id):
        s = '''
        DELETE FROM employees WHERE id=%s
        '''
        self.cursor.execute(s, (id,))
        self.connection.commit()
        print(" Xodim o‘chirildi.")


#  BAZAGA ULANISH
My_object = Data_connect('postgres', 'postgres', '123')


# === MENU FUNKSIYALAR ===
def customer_menu():
    while True:
        print("\n--- CUSTOMER CRUD ---")
        print("1. Qo‘shish")
        print("2. Ko‘rish")
        print("3. O‘zgartirish")
        print("4. O‘chirish")
        print("0. Chiqish")
        tanlov = input("Tanlang: ")

        if tanlov == "1":
            name = input("Customer nomi: ")
            My_object.add_customer(name)
        elif tanlov == "2":
            My_object.view_customer()
        elif tanlov == "3":
            My_object.view_customer()
            id = int(input("ID: "))
            new_title = input("Yangi nom: ")
            My_object.update_customers(id, new_title)
        elif tanlov == "4":
            My_object.view_customer()
            id = int(input("ID: "))
            My_object.delete_customers(id)
        elif tanlov == "0":
            break
        else:
            print(" Noto‘g‘ri tanlov.")


def order_menu():
    while True:
        print("\n--- ORDER CRUD ---")
        print("1. Qo‘shish")
        print("2. Ko‘rish")
        print("3. O‘zgartirish")
        print("4. O‘chirish")
        print("5. Order detail (ID bo‘yicha)")
        print("6. Sana oralig‘idagi orderlar")
        print("0. Chiqish")
        tanlov = input("Tanlang: ")

        if tanlov == "1":
            title = input("Order nomi: ")
            tipy = input("Order turi: ")
            My_object.add_order(title, tipy)
        elif tanlov == "2":
            My_object.order_view()
        elif tanlov == "3":
            My_object.order_view()
            id = int(input("ID: "))
            title = input("Yangi nom: ")
            tipy = input("Yangi turi: ")
            My_object.update_order(id, title, tipy)
        elif tanlov == "4":
            My_object.order_view()
            id = int(input("ID: "))
            My_object.delete_order(id)
        elif tanlov == "5":
            id = int(input("Order ID: "))
            My_object.order_detail(id)
        elif tanlov == "6":
            start = input("Boshlanish sanasi (YYYY-MM-DD): ")
            end = input("Tugash sanasi (YYYY-MM-DD): ")
            My_object.filter_orders_by_date(start, end)
        elif tanlov == "0":
            break
        else:
            print(" Noto‘g‘ri tanlov.")


def employee_menu():
    while True:
        print("\n--- EMPLOYEE CRUD ---")
        print("1. Qo‘shish")
        print("2. Ko‘rish")
        print("3. O‘zgartirish")
        print("4. O‘chirish")
        print("0. Chiqish")
        tanlov = input("Tanlang: ")

        if tanlov == "1":
            name = input("Ism: ")
            last_name = input("Familiya: ")
            country = input("Davlat: ")
            departament = input("Bo‘lim: ")
            salary = float(input("Maosh: "))
            email = input("Email: ")
            phone = input("Telefon: ")
            My_object.add_employee(name, last_name, country, departament, salary, email, phone)
        elif tanlov == "2":
            My_object.view_employee()
        elif tanlov == "3":
            My_object.view_employee()
            id = int(input("ID: "))
            name = input("Ism: ")
            last_name = input("Familiya: ")
            country = input("Davlat: ")
            departament = input("Bo‘lim: ")
            salary = float(input("Maosh: "))
            email = input("Email: ")
            phone = input("Telefon: ")
            My_object.update_employee(id, name, last_name, country, departament, salary, email, phone)
        elif tanlov == "4":
            My_object.view_employee()
            id = int(input("ID: "))
            My_object.delete_employees(id)
        elif tanlov == "0":
            break
        else:
            print(" Noto‘g‘ri tanlov.")


# ========== ASOSIY MENYU ==========
def main_menu():
    while True:
        print("\n--- ASOSIY MENYU ---")
        print("1. Customer CRUD")
        print("2. Order CRUD")
        print("3. Employee CRUD")
        print("0. Chiqish")
        tanlov = input("Tanlang: ")

        if tanlov == "1":
            customer_menu()
        elif tanlov == "2":
            order_menu()
        elif tanlov == "3":
            employee_menu()
        elif tanlov == "0":
            print(" Dastur yakunlandi!")
            break
        else:
            print(" Noto‘g‘ri tanlov!")

# --- Dastur ishga tushadi ---
main_menu()





