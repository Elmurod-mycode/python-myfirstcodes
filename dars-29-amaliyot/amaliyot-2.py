#Yangi, Avtosalon degan klass yarating va kerakli xususiyatlar bilan to'ldiring
# (salon nomi, manzili, sotuvdagi avtomobillar va hokazo)
# Avtosalonga yangi avtomobillar qo'shish uchun metod yozing
# Avtosalondagi avtomobillar haqida ma'lumot qaytaruvchi metod yozing
# Yuqoridagi obyektlar va ularga tegishli metodlarni tekshirib ko'ring
# dir() funksyasi va __dict__ metodi yordamida o'zingiz yozgan va
# Pythondagi turli klass va obyektlarning xususiyatlari va metodlarini toping (dir(str), dir(int) va hokazo)

class Avtosalon:
    def __init__(self, salon_nomi, manzili, *sotuvdagi_avtolar , **narxlari):
        self.salon_nomi = salon_nomi
        self.manzili = manzili
        self.sutuvdagi_avtolar = list(sotuvdagi_avtolar)
        self.narxlari = narxlari
    def get_salon_nomi(self):
        return self.salon_nomi
    def get_manzili(self):
        return self.manzili
    def get_sutuvdagi_avtolar(self):
        sotuvdagi_avtolar = self.sutuvdagi_avtolar
        return sotuvdagi_avtolar
    def set_sotuvdagi_avtolar(self,*avtolar):
        self.sutuvdagi_avtolar.extend(avtolar)
        # yangi narxlar lug'atini yaratish
        return self.sutuvdagi_avtolar

avtosalon1 = Avtosalon("Bek avto", "Sergeli A1", "malibu", 'cobalt', 'gentra', 'matiz', 'damas', 'captiva' , )

print(avtosalon1.set_sotuvdagi_avtolar('captiva', 'trecker', 'ferrari', 'bugatti'))

avt = dir(Avtosalon)
for a in avt:
    print(a)
# def see_methods(klass):
#     return[method for method in dir(klass) if method.startswith('__') is False]
# print(see_methods(Avtosalon))
# dir(int)
# print(dir(int))

def dict(dicts):
    return [dict for dict in dicts.__dict__.values()]
print(dict(avtosalon1))

print(avtosalon1.__dict__)
print(Avtosalon.__dict__)

