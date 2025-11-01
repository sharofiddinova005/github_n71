# Python’da getter va setter — bu obyekt ichidagi o‘zgaruvchilarga (atributlarga) to‘g‘ridan-to‘g‘ri emas, nazorat bilan kirish
# imkonini beradigan maxsus metodlar.
# Getter — qiymatni olish uchun
#
# Getter yordamida obyektdagi qiymatni o‘qish (ko‘rish) mumkin.
#
# Setter — qiymatni o‘rnatish uchun
#
# Setter yordamida obyektdagi qiymatni o‘zgartirish mumkin, lekin kerak bo‘lsa, uni tekshirib yoki cheklab o‘rnatamiz.
class Student:
    def __init__(self, name, age):
        self.name = name
        self._age = age   # _age — bu maxfiy (private) o‘zgaruvchi

    # GETTER — qiymatni olish
    def get_age(self):
        return self._age

    # SETTER — qiymatni o‘rnatish
    def set_age(self, new_age):
        if new_age > 0:
            self._age = new_age
        else:
            print("Yosh manfiy bo‘lishi mumkin emas!")

# Obyekt yaratamiz
s = Student("Marjona", 20)

print(s.get_age())   # 20
s.set_age(25)        # yoshni o‘zgartiradi
print(s.get_age())   # 25
s.set_age(-3)        # xato

# property — bu getter va setterni oddiy atribut ko‘rinishida ishlatish uchun qisqaroq va chiroyli usul.
# Yani get_age() o‘rniga shunchaki student.age deb yozish mumkin bo‘ladi.

class Student:
    def __init__(self, name, age):
        self.name = name
        self._age = age

    @property
    def age(self):
        return self._age       # getter

    @age.setter
    def age(self, new_age):
        if new_age > 0:
            self._age = new_age
        else:
            print("Yosh manfiy bo‘lishi mumkin emas!")

# Obyekt
s = Student("Marjona", 20)

print(s.age)     # bu get_age() ga teng → 20
s.age = 25       # bu set_age() ga teng
print(s.age)     # 25
s.age = -5       # xato chiqadi

# getter — qiymatni olish uchun.
#
# setter — qiymatni o‘rnatish uchun.
#
# property — ikkalasini chiroyli va xavfsiz ishlatish uchun.

# Ma’lumotni himoya qilish
# Noto‘g‘ri o‘zgartirishdan saqlash
# Faqat ruxsat berilgan yo‘l bilan kirish