# • Avvalga darslarda yaratilgan obyektlarga (Shaxs, Talaba) turli dunder metodlarni qo'shishni mashq qiling.
# • Obyekt haqida ma'lumot (__rerp__)
# • Talabalarni bosqichi bo'yicha solishtirish (__lt__, __eg__ va hokazo)
# • Fan degan yangi klass yarating. Fan obyetklari tarkibida shu fanga yozilgan talabalarning ro'yxati saqlansin.
# Buning uchun Fanga add_student(), __getitem__, __setitem__, __len__ kabi metodlarni qo'shing.
# • Fanga qo'shish + operatori yordamida talaba qo'shish metodini yozing
# • Minus (-) operatori yordamida fandan talaba olib tashlash metodini yozing (bunda talabaning passport raqami yoki ID raqami bo'yicha topib, olib tashlash mumkin)
# • Fan obyektlarini chaqiriladigan qiling (masalan, fizika(), yoki fizika(talaba1)). Bu metodlarni o'zingiz istagandek talqin qiling.

class Shaxs:
    """Shaxslar haqida ma'lumot."""
    def __init__(self, ism, familiya, passport, tyil):
        self.ism = ism
        self.familiya = familiya
        self.passport = passport
        self.tyil = tyil
    def __repr__(self):
        return f"Shaxs: {self.ism} {self.familiya}. Passport: {self.passport}. Yil: {self.tyil}"

shaxs = Shaxs("Ali", "Valiyev", "AB934839", 2000)
print(shaxs)
class Talaba(Shaxs):
    def __init__(self, ism , familiya, passport, tyil, bosqich):
        super().__init__(ism, familiya, passport, tyil)
        self.bosqich = bosqich
    def __repr__(self):
        return f"{self.ism} {self.familiya}.{self.bosqich}-bosqich talabasi."
    def __lt__(self, boshqa):
        return self.bosqich<boshqa.bosqich
    def __eq__(self, boshqa):
        return self.bosqich == boshqa.bosqich
    def __le__(self, boshqa):
        return self.bosqich>boshqa.bosqich

# talaba1 = Talaba("Vali", 'Akbarov', 'AD28329222',  2000, 1 )
# talaba2 = Talaba("Hakim", "Jabborov", "AH2984290", 1998, 2)
# print(talaba1>talaba2)
class Fan:
    def __init__(self, fan):
        self.fan = fan
        self.talabalar = []
    def __repr__(self):
        return self.fan
    def add_student(self, *talabalar):
        for talaba in talabalar:
            if isinstance(talaba, Talaba):
                self.talabalar.append(talaba)
            else:
                print("Talaba obyektini kiriting.")
    def __getitem__(self, index):
        return self.talabalar[index]
    def __setitem__(self, index, qiymat):
        if isinstance(qiymat, Talaba):
            self.talabalar[index] = qiymat
    def __len__(self):
        return len(self.talabalar)

    def __call__(self, talaba=None):
        if talaba:
            self.add_student(talaba)
        else:
            return self.talabalar

    def __add__(self, talaba):
        """+ operatori yordamida talaba qo'shish"""
        self.add_student(talaba)
        return self

    def __sub__(self, talaba):
        """- operatori yordamida talaba olib tashlash (passport orqali)"""
        self.talabalar = [t for t in self.talabalar if t.passport != talaba.passport]
        return self

talaba1 = Talaba("Sulton", "Xasanov", "AB288242", 2001, 1)
talaba2 = Talaba("Vali", 'Akbarov', 'AD28329222',  2000, 1 )
talaba3 = Talaba("Hakim", "Jabborov", "AH2342344", 1998, 2)
talaba4 = Talaba("Sunnat", "Niyozov", "AB2882345", 2001, 4)
talaba5 = Talaba("Yusuf", 'Qahhorov', 'AD28234345',  2000, 3 )
talaba6 = Talaba("Javohir", "Mamadaliyev", "AH29823424", 1998, 3)
talaba7 = Talaba("Bolatvoy", "Bo'riyev", "AB28452345", 2001, 4)
talaba8 = Talaba("Jamol", 'Inoyatov', 'AD2345455',  2000, 2 )
talaba9 = Talaba("Bakir", "Kamolov", "AH23434543", 1998, 3)
fan1 = Fan("Oliy matematika")
fan1.add_student(talaba1,talaba2,talaba3,talaba4,talaba5,talaba6, talaba7,talaba8,talaba9)
print(fan1.talabalar)
print(fan1[7])
talaba10 = Talaba("Munavar", "Muzzafarova", "AB929304934", 1996, 4)
fan1[0] = talaba10
print(len(fan1))
fan1+talaba10
print(fan1())