from ctypes.wintypes import PPOINT

import psycopg2

class Data_connect:
    def __init__(self, dbname, user, password, host='localhost', port=5432):
        self.connection=psycopg2.connect(
            dbname=dbname,
            user=user,
            password=password,
            host=host,
            port=port
        )
        self.cursor=self.connection.cursor()

    # ----DEPARTAMENT----

    def add_departament(self, title):
        s = '''
        insert into departament(title)
        values(%s)
        '''
        self.cursor.execute(s, (title,))
        self.connection.commit()

    def view_departament(self):
        s = 'select * from departament'
        self.cursor.execute(s)
        rows = self.cursor.fetchall()
        for item in rows:
            print(f"ID: {item[0]} | Title: {item[1]}")

    def update_departament(self, id, new_title):
        s = 'update departament set title=%s where id=%s'
        self.cursor.execute(s, (new_title, id))
        self.connection.commit()

    def delete_departament(self, id):
        s = 'delete from departament where id=%s'
        self.cursor.execute(s, (id,))
        self.connection.commit()

    # ----COUNTRY----

    def add_country(self,title,type):
        query='''
        insert into countries(title,tipy)
        values(%s,%s)
        '''
        self.cursor.execute(query,(title,type))
        self.connection.commit()

    def create_table(self):
        s='''
        create table departament(
        id serial primary key,
        title varchar(50) not null
        );
        '''
        self.cursor.execute(s)
        self.connection.commit()

    def country_view(self):
        s='''
        select * from countries;
        '''
        self.cursor.execute(s)
        con=self.cursor.fetchall()
        for item in con:
            print(item[0],item[1],item[2])

    def update_country(self, id, title, tipy):
        s = 'update countries set title=%s, tipy=%s where id=%s'
        self.cursor.execute(s, (title, tipy, id))
        self.connection.commit()

    def del_country(self,id):
        s='''
        delete from countries where id=(%s)
        '''
        self.cursor.execute(s,(id,))
        self.connection.commit()

    #----EMPLOYEE----

    def add_employee(self, name, last_name, country, departament, salary, email, phone):
        query='''
        insert into employees(name, last_name, country, departament, salary, email, phone)
        values(%s,%s,%s,%s,%s,%s,%s)
        '''
        self.cursor.execute(query,(name, last_name, country,departament,salary,email,phone))
        self.connection.commit()

    def view_employee(self):
        s='''
        select * from employees
        '''
        self.cursor.execute(s)
        con = self.cursor.fetchall()
        for item in con:
            print(f"ID:{item[0]} Name:{item[1]} Lastname:{item[2]} Country:{item[3]} Departament:{item[4]} Salary:{item[5]} Email:{item[6]} Phone:{item[7]}")

    def update_employee(self, id, name, last_name, country, departament, salary, email, phone):
        s = '''
        update employees
        set name=%s, last_name=%s, country=%s, departament=%s, salary=%s, email=%s, phone=%s
        where id=%s
        '''
        self.cursor.execute(s, (name, last_name, country, departament, salary, email, phone, id))
        self.connection.commit()

    def del_employees(self,id):
        s = '''
               delete from employees where id=(%s)
               '''
        self.cursor.execute(s, (id,))
        self.connection.commit()

    def search_employee(self, country_name, departament_name):
        s = '''
        select * from employees
        where country=%s and departament=%s
        '''
        self.cursor.execute(s, (country_name, departament_name))
        rows = self.cursor.fetchall()
        if rows:
            print(f"{country_name} davlatidagi {departament_name} bo'limidagi xodimlar:")
            for item in rows:
                print(f" - {item[1]} {item[2]} | {item[5]} so'm | {item[6]} | {item[7]}")
        else:
            print(" Bunday xodim topilmadi.")




My_object=Data_connect('postgres','postgres','123')

def departament_menu():
    while True:
        print("\n--- DEPARTAMENT CRUD ---")
        print("1. Qo‘shish")
        print("2. Ko‘rish")
        print("3. O‘zgartirish")
        print("4. O‘chirish")
        print("0. Chiqish")
        tanlov = input("Tanlang: ")

        if tanlov == "1":
            title = input("Departament nomi: ")
            My_object.add_departament(title)
        elif tanlov == "2":
            My_object.view_departament()
        elif tanlov == "3":
            My_object.view_departament()
            id = int(input("ID: "))
            new_title = input("Yangi nom: ")
            My_object.update_departament(id, new_title)
        elif tanlov == "4":
            My_object.view_departament()
            id = int(input("ID: "))
            My_object.delete_departament(id)
        elif tanlov == "0":
            break
        else:
            print("Noto‘g‘ri tanlov.")


def country_menu():
    while True:
        print("\n--- COUNTRY CRUD ---")
        print("1. Qo‘shish")
        print("2. Ko‘rish")
        print("3. O‘zgartirish")
        print("4. O‘chirish")
        print("0. Chiqish")
        tanlov = input("Tanlang: ")

        if tanlov == "1":
            title = input("Country nomi: ")
            tipy = input("Country turi: ")
            My_object.add_country(title, tipy)
        elif tanlov == "2":
            My_object.view_country()
        elif tanlov == "3":
            My_object.view_country()
            id = int(input("ID: "))
            title = input("Yangi nom: ")
            tipy = input("Yangi turi: ")
            My_object.update_country(id, title, tipy)
        elif tanlov == "4":
            My_object.view_country()
            id = int(input("ID: "))
            My_object.delete_country(id)
        elif tanlov == "0":
            break
        else:
            print("Noto‘g‘ri tanlov.")


def employee_menu():
    while True:
        print("\n--- EMPLOYEE CRUD ---")
        print("1. Qo‘shish")
        print("2. Ko‘rish")
        print("3. O‘zgartirish")
        print("4. O‘chirish")
        print("5. Qidirish (country + departament)")
        print("0. Chiqish")
        tanlov = input("Tanlang: ")

        if tanlov == "1":
            name = input("Ism: ")
            last_name = input("Familiya: ")
            country = input("Davlat nomi: ")
            departament = input("Departament: ")
            salary = float(input("Maosh: "))
            email = input("Email: ")
            phone = input("Telefon: ")
            My_object.add_employee(name, last_name, country, departament, salary, email, phone)
        elif tanlov == "2":
            My_object.view_employees()
        elif tanlov == "3":
            My_object.view_employees()
            id = int(input("ID: "))
            name = input("Ism: ")
            last_name = input("Familiya: ")
            country = input("Davlat nomi: ")
            departament = input("Departament: ")
            salary = float(input("Maosh: "))
            email = input("Email: ")
            phone = input("Telefon: ")
            My_object.update_employee(id, name, last_name, country, departament, salary, email, phone)
        elif tanlov == "4":
            My_object.view_employees()
            id = int(input("ID: "))
            My_object.delete_employee(id)
        elif tanlov == "5":
            country = input("Qaysi davlat: ")
            departament = input("Qaysi departament: ")
            My_object.search_employee(country, departament)
        elif tanlov == "0":
            break
        else:
            print("Noto‘g‘ri tanlov.")


# ========== ASOSIY MENYU ==========
def main_menu():
    while True:
        print("\n--- ASOSIY MENYU ---")
        print("1. Departament CRUD")
        print("2. Country CRUD")
        print("3. Employee CRUD")
        print("0. CHIQISH")
        tanlov = input("Tanlang: ")

        if tanlov == "1":
            departament_menu()
        elif tanlov == "2":
            country_menu()
        elif tanlov == "3":
            employee_menu()
        elif tanlov == "0":
            print("Dastur yakunlandi!")
            break
        else:
            print("Noto‘g‘ri tanlov!")

main_menu()



