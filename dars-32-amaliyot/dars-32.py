"""
2/4/2025
Muallif: Elmurod O'rinboyev
32-dars. Dunder metodlari
"""
# Maxsus Metodlar

# class Avto:
#     __num_avto = 0
#     def __init__(self, make, model, rang, yil, narx):
#         """Avtomobilning xususiyatlari."""
#         self.make = make
#         self.model = model
#         self.rang = rang
#         self.yil = yil
#         self.narx = narx
#         Avto.__num_avto +=1
# for a in dir(Avto):
#     print(a)

# Obyekt haqida ma'lumot
# class Avto:
#     __num_avto = 0
#     """Avtomobil klassi"""
#     def __init__(self,make,model,rang,yil,narh):
#         """Avtomobilning xususiyatlari"""
#         self.make = make
#         self.model = model
#         self.rang = rang
#         self.yil = yil
#         self.narh = narh
#         Avto.__num_avto += 1
#     def __repr__(self):
#         """Obyekt haqida ma'lumot."""
#         return f"Avto: {self.make}, {self.model}, {self.rang}"
# avto1 = Avto('GM', "Malibu", "Qora", 2025, 30000)
# print(avto1)

# Obyektlarni taqqoslash
#
# class Avto:
#     __num_avto = 0
#     """Avtomobil klassi"""
#     def __init__(self,make,model,rang,yil,narx):
#         """Avtomobilning xususiyatlari"""
#         self.make = make
#         self.model = model
#         self.rang = rang
#         self.yil = yil
#         self.narx = narx
#         Avto.__num_avto += 1
#     def __repr__(self):
#         """Obyekt haqida ma'lumot."""
#         return f"Avto: {self.make}, {self.model}, {self.rang}"
#     def __eq__(self, boshqa_avto):
#         """Tenglik"""
#         return self.narx == boshqa_avto.narx
#     def __lt__(self, boshqa_avto):
#         """Kichik"""
#         return self.narx<boshqa_avto.narx
#     def __le__(self, boshqa_avto):
#         """Kichik yoki teng"""
#         return self.narx<=boshqa_avto.narx
# avto1 = Avto('GM', "Malibu", "Qora", 2025, 30000)
# print(avto1)
# avto2 = Avto("GM", "Lacetti", "Oq", 2022, 20000)
# print(avto1>avto2)
#
# # Obyektning uzunligi
# class AvtoSalon:
#     """Avtosalon klassi"""
#     def __init__(self, name):
#         self.name = name
#         self.avtolar = []
#     def __repr__(self):
#         return f"{self.name} avtosaloni"
#     def add_avto(self, avto):
#         if isinstance(avto, Avto): # agar avto Avto klassidan bo'lsa
#             self.avtolar.append(avto)
#         else:
#             print("Avto obyektini kiriting")
#
#     def __len__(self):
#         return len(self.avtolar)
#
# salon1= AvtoSalon("MusurAvto")
# # Avto obyektlarni yaratamiz
# avto1 = Avto('GM', "Malibu", "Qora", 2025, 30000)
# avto2 = Avto("GM", "Lacetti", "Oq", 2022, 20000)
# avto3 = Avto("Hyndai", "Soneto", "pushti", 1777, 15)
# for avto in [avto1, avto2,avto3]:
#     print(salon1.add_avto(avto))
# print(len(salon1))
# # print(avto1>avto2)
# # print(salon1)
# # print(isinstance('salom', str))
# # print(isinstance(12, float))
# # print(isinstance(salon1, AvtoSalon))
#
# class AvtoSalon:
#     """Avtosalon klassi"""
#
#     def __init__(self, name):
#         self.name = name
#         self.avtolar = []
#
#     def add_avto(self, avto):
#         if isinstance(avto, Avto):  # agar avto Avto klassidan bo'lsa
#             self.avtolar.append(avto)
#         else:
#             print("Avto obyketini kiriting")
#
#     def __repr__(self):
#         return f"{self.name} avtosaloni"
#
#     def __len__(self):
#         return len(self.avtolar)
#
#     def __getitem__(self, idex):
#         return self.avtolar[idex]
#     def __setitem__(self, index, qiymat):
#         if isinstance(qiymat, Avto):
#             self.avtolar[index]=qiymat
# salon1 = AvtoSalon("MusurSalon")
# avto1 = Avto("m", "aaaadk", 'kulrang', 293, 1323)
# avto2 = Avto("Gm", "damas", 'yashil', 2002, 2343)
# avto3 = Avto('dk', "sdld", "ko'k", 2090, 2883293)
# [salon1.add_avto(avto) for avto in [avto1, avto2, avto3]]
# print(len(salon1))
# print(salon1[0])
# print(salon1[1])
# print(salon1[:])
# avto4 = Avto("Kia", "K5", "Sariq", 2025, 30000)
# salon1[0] = avto4
# print(salon1[0])
# class Avto:
#     __num_avto = 0
#     def __init__(self, make, model, rangi, yili, narxi):
#         self.make = make
#         self.model = model
#         self.rangi = rangi
#         self.yili = yili
#         self.narxi = narxi
#         Avto.__num_avto +=1
#     @classmethod
#     def get_avto_num(cls):
#         return cls.__num_avto
#     def __repr__(self):
#         return f"Avto {self.make} {self.model} {self.rangi}"
# class AvtoSalon:
#     """Avtosalon klassi"""
#     def __init__(self, name):
#         self.name = name
#         self.avtolar = []
#     def __repr__(self):
#         return f"{self.name} avtosaloni"
#     def __len__(self):
#         return len(self.avtolar)
#     def __getitem__(self, index):
#         return self.avtolar[index]
#     def __setitem__(self, index, value):
#         if isinstance(value, Avto):
#             self.avtolar[index] = value
#
#     def add_avto(self, *qiymat):
#         for avto in qiymat:
#             if isinstance(avto, Avto):
#                 self.avtolar.append(avto)
#             else:
#                 print("Avto obyektini kiriting.")
#     def __add__(self, qiymat):
#         if isinstance(qiymat, AvtoSalon):
#             yangi_salon = AvtoSalon(f"{self.name} {qiymat.name}")
#             yangi_salon.avtolar = self.avtolar + qiymat.avtolar
#             return yangi_salon
# salon1 = AvtoSalon("MusurAvto")
# salon2 = AvtoSalon("QimatAvto")
# # 6 ta avto obyektini yaratamiz
# avto1 = Avto("GM", "Cobalt", "Oq", 2023, 10000)
# avto2 = Avto("GM","Lacetti","Oq",2020,20000)
# avto3 = Avto("Toyota",'Carolla',"Silver",2018, 45000)
# avto4 = Avto("Mazda", "6", 'Qizil',2015,35000)
# avto5 = Avto("Volkswagen","Polo",'Qora',2015,30000)
# avto6 = Avto("Honda","Accord","Oq",2017,42000)
# salon1.add_avto(avto1, avto2, avto3)
# salon2.add_avto(avto4, avto5, avto6)
# salon3 = salon2 +salon1
# print(salon3)
# print(salon3[:])

class Avto:
    __num_avto = 0
    def __init__(self, make, model, rangi, yili, narxi):
        self.make = make
        self.model = model
        self.rangi = rangi
        self.yili = yili
        self.narxi = narxi
        Avto.__num_avto +=1
    @classmethod
    def get_avto_num(cls):
        return cls.__num_avto
    def __repr__(self):
        return f"Avto {self.make} {self.model} {self.rangi}"
# class AvtoSalon:
#     """Avtosalon klassi"""
#     def __init__(self, name):
#         self.name = name
#         self.avtolar = []
#     def __repr__(self):
#         return f"{self.name} avtosaloni"
#     def __len__(self):
#         return len(self.avtolar)
#     def __getitem__(self, index):
#         return self.avtolar[index]
#     def __setitem__(self, index, value):
#         if isinstance(value, Avto):
#             self.avtolar[index] = value
#
#     def add_avto(self, *qiymat):
#         for avto in qiymat:
#             if isinstance(avto, Avto):
#                 self.avtolar.append(avto)
#             else:
#                 print("Avto obyektini kiriting.")
#     def __add__(self, qiymat):
#         if isinstance(qiymat, AvtoSalon):
#             yangi_salon = AvtoSalon(f"{self.name} {qiymat.name}")
#             yangi_salon.avtolar = self.avtolar + qiymat.avtolar
#             return yangi_salon
#         elif isinstance(qiymat, Avto):
#             self.add_avto(qiymat)
#         else:
#             print(f"AvtoSalon ga {type(qiymat)} qo'shib bo'lmaydi.")
# salon1 = AvtoSalon("MusurAvto")
# salon2 = AvtoSalon("QimatAvto")
# # 6 ta avto obyektini yaratamiz
# avto1 = Avto("GM", "Cobalt", "Oq", 2023, 10000)
# avto2 = Avto("GM","Lacetti","Oq",2020,20000)
# avto3 = Avto("Toyota",'Carolla',"Silver",2018, 45000)
# avto4 = Avto("Mazda", "6", 'Qizil',2015,35000)
# avto5 = Avto("Volkswagen","Polo",'Qora',2015,30000)
# avto6 = Avto("Honda","Accord","Oq",2017,42000)
# salon1.add_avto(avto1, avto2, avto3)
# salon2.add_avto(avto4, avto5, avto6)
# salon3 = salon2 +salon1
#
# print(salon3)
# print(salon3[:])
# salon1_1 = AvtoSalon("MaxAvto")
# salon1_1.add_avto(avto1, avto2, avto3)
# newAvto = Avto("BMW", 'X7', "Qora", 2019, 70000)
# salon1_1 + newAvto
# print(salon1_1)


# Parametrsiz chaqirish

class AvtoSalon:
    def __init__(self, name):
        self.name = name
        self.avtolar = []
    def __repr__(self):
        return f"{self.name} avtosaloni"
    def __len__(self):
        return len(self.avtolar)
    def __getitem__(self, index):
        return self.avtolar[index]
    def __setitem__(self, index, value):
        if isinstance(value, Avto):
            self.avtolar[index] = value
    def add_avto(self, *qiymat):
        for avto in qiymat:
            if isinstance(avto, Avto):
                self.avtolar.append(avto)
            else:
                print("Avto obyektini kiriting")
    def __add__(self, qiymat):
            if isinstance(qiymat, AvtoSalon):
                yangi_salon = AvtoSalon(f"{self.name} {qiymat.name}")
                yangi_salon.avtolar = self.avtolar + qiymat.avtolar
                return yangi_salon
            elif isinstance(qiymat, Avto):
                self.add_avto(qiymat)
            else:
                print(f"AvtoSalon ga {type(qiymat)} qo'shib bo'lmaydi.")

#     def __call__(self):
#         return [avto for avto in self.avtolar]
# avto1 = Avto("GM", "Cobalt", "Oq", 2023, 10000)
# avto2 = Avto("GM","Lacetti","Oq",2020,20000)
# avto3 = Avto("Toyota",'Carolla',"Silver",2018, 45000)
# salon1= AvtoSalon("MusurAvto")
# salon1.add_avto(avto1, avto2, avto3)
# print(salon1())

# Parapetr bilan chaqirish
    def __call__(self, *param):
        if param: # agar parametr bo'lsa
            for avto in param:
                self.add_avto(avto)
        else: # agar parapetr bo'lmasa
            return [avto for avto in self.avtolar]

# avto1 = Avto("GM", "Cobalt", "Oq", 2023, 10000)
# avto2 = Avto("GM","Lacetti","Oq",2020,20000)
# avto3 = Avto("Toyota",'Carolla',"Silver",2018, 45000)
salon1= AvtoSalon("MusurAvto")
avto_new = Avto("Mercedes-Benz" , "E200", "Silver", 2020, 80000)
# Obyektni chaqiramiz.
salon1(avto_new) # Yangi avto qo'shamiz
print(salon1()) # salondagi mashinalarni ko'ramiz
