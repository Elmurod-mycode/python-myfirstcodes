"""
2/2/2025
Muallif: Elmurod O'rinboyev
29-dars. Obyektlar bilan ishlash
"""
## Xususiyatlarga standart qiymat berish
# class Talaba:
#     """TAlaba nomli klass yaratamiz."""
#     def __init__(self, ism, familiya,  tyil):
#         """Talabaning xususiyatlari."""
#         self.ism = ism
#         self.familiya = familiya
#         self.tyil = tyil
#         self.bosqich = 1
#
#     def get_info(self):
#         return f"{self.ism} {self.familiya}. {self.bosqich}-bosqich talabasi."
# talaba1 = Talaba("ali", 'valiyev', 2000)
# print(talaba1.get_info())
# # Standart qiymatni o'zgartirish
# talaba1.bosqich=2
# print(talaba1.bosqich)
# print(talaba1.get_info()) # Bu yerda e'tibor beradiganiniz printda chiqadigan bosqichni o'zgarishiga.

# # Yana boshqa usuli, obyekt xususiyatini yangilovci metod yozish
# class Talaba:
#     """TAlaba nomli klass yaratamiz."""
#     def __init__(self, ism, familiya,  tyil):
#         """Talabaning xususiyatlari."""
#         self.ism = ism
#         self.familiya = familiya
#         self.tyil = tyil
#         self.bosqich = 1
#
#     def get_info(self):
#         return f"{self.ism} {self.familiya}. {self.bosqich}-bosqich talabasi."
#     def update_bosqich(self):
#         self.bosqich+=1
# talaba1 = Talaba("ali", 'valiyev', 2000)
# print(talaba1.get_info())
# talaba1.update_bosqich()
# print(talaba1.get_info())
#
#
# # Obyektlar o'rtasida munosabat
# # Obyektga yo'naltirilgan dasturlashning afzalligi, turli obyektlar o'rtasid o'zaro
# # munosabatlarni oson yo'lga qo'yish muminligida. Buni misolda ko'rish uchun, yangi
# # Fan degan klass yaratamiz va fanimizga talabalar qo'shish imkoniyatini ham
# # yaratamiz (add_student() metodi):
# class Fan():
#     def __init__(self,nomi):
#         self.nomi = nomi
#         self.talabalar_soni = 0
#         self.talabalar = []
#     def add_student(self, talaba):
#         """Fanga talabalar qo'shish"""
#         self.talabalar.append(talaba)
#         self.talabalar_soni +=1
#     def get_students(self):
#         return [talaba.get_info() for talaba in self.talabalar]
#
# tarix = Fan("Tarix")
# talaba1 = Talaba('Aziz', 'Ruslanov', 2003)
# talaba2 = Talaba("Oybek", 'Arslonov', 2000)
# talaba3 = Talaba("Ulug'bek", "Jumanov" ,2001)
# tarix.add_student(talaba1)
# tarix.add_student(talaba2)
# tarix.add_student(talaba3)
# print(tarix.talabalar_soni)
# print(tarix.get_students())

class Talaba:
    def __init__(self, ism, familiya, tyil):
        self.ism = ism
        self.familiya = familiya
        self.tyil = tyil
        self.bosqich = 1
        self.til = "o'zbek"
    def get_ism(self):
        return self.ism.title()
    def get_familiya(self):
        return self.familiya.title()
    def get_age(self, hozirgi_yil):
        age = hozirgi_yil - self.tyil
        return age
    def set_boshqich(self, boshqich):
        self.bosqich = boshqich
        return boshqich
    def get_fullname(self):
        return f"{self.ism.title()} {self.familiya.title()}"
    def set_name(self, ism):
        self.ism = ism
        return ism
    def set_lastname(self, familiya):
        self.familiya = familiya
        return familiya.title()


talaba1 = Talaba('olim', 'alimov', 2003)
print(talaba1.set_boshqich(2))
print(talaba1.set_lastname("hakimov"))

# dir() Funksiyasi
#
# print(dir(Talaba))

def see_methods(klass):
    return [method for method in dir(klass) if method.startswith('__') is False]
print(see_methods(Talaba))