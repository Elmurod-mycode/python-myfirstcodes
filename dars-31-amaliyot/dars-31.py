"""
2/4/2025
Muallif: Elmurod O'rinboyev
Mavzu: 31-dars. Inkapsulyatsia, klassning xususiyat va metdolari

"""
# Inkapsulyatsiya
# from uuid import uuid4
# class Avto:
#     def __init__(self, make, model, rang, yil, narx, km = 0):
#         """Avtomobilning xususiyatlari."""
#         self.make = make
#         self.model = model
#         self.rang = rang
#         self.yil = yil
#         self.narx = narx
#         self.__km = km
#         self.__id = uuid4()
#     def get_km(self):
#         return self.__km
#     def get_id(self):
#         return self.__id
# avto1 = Avto("GM", 'Malibu', 'Qora', 2025, 30000, 100000)
# print(avto1.get_km())
# print(avto1.get_id())

# Bunday yopiq xususiyatlarni o'zgartirish
# from uuid import uuid4
# class Avto:
#     def __init__(self, make, model, rang, yil, narx, km = 0):
#         """Avtomobilning xususiyatlari."""
#         self.make = make
#         self.model = model
#         self.rang = rang
#         self.yil = yil
#         self.narx = narx
#         self.__km = km
#         self.__id = uuid4()
#     def get_km(self):
#         return self.__km
#     def get_id(self):
#         return self.__id
#     def add_km(self, km):
#         """Mashinaning km ga yana km qo'shish."""
#         if km>= 0 :
#             self.__km +=km
#         else:
#             print("Mashinani km kamaytirib bo'lmaydi.")
# avto1 = Avto("GM", 'Malibu', 'Qora', 2025, 30000, 100000)
# avto1.add_km(3000)
# print(avto1.get_km())

## Klassning xususiyatlari va metodlari.

from uuid import uuid4
# class Avto:
#     num_avto = 0
#     def __init__(self, make, model, rang, yil, narx, km = 0):
#         """Avtomobilning xususiyatlari."""
#         self.make = make
#         self.model = model
#         self.rang = rang
#         self.yil = yil
#         self.narx = narx
#         self.__km = km
#         self.__id = uuid4()
#         Avto.num_avto +=1
# avto1 = Avto("GM", "Lacetti", "Oq", 2025, 40000)
# avto2 = Avto("GM", 'Cobalt', "qora", 2025, 15000)
# print(avto1.num_avto)

# Klassning xususiyatlarini inkapsulyatsiya qilish

class Avto:
    __num_avto = 0
    def __init__(self, make, model, rang, yil, narx, km = 0):
        """Avtomobilning xususiyatlari."""
        self.make = make
        self.model = model
        self.rang = rang
        self.yil = yil
        self.narx = narx
        self.__km = km
        self.__id = uuid4()
        Avto.__num_avto +=1
    @classmethod
    def get_avto_num(cls):
        return cls.__num_avto

avto1 = Avto("GM", "Lacetti", "Oq", 2025, 40000)
avto2 = Avto("GM", 'Cobalt', "qora", 2025, 15000)
# Klass metodlarga klassining nomi orqali murojat qilinadi:
print(Avto.get_avto_num())


## 
