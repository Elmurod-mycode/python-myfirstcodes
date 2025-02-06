"""
2/3/2025
Muallif: Elmurod O'rinboyev
Mavzu: 30-dars.Vorislik va polimorfizm
"""
# Super klass va voris klass

class Shaxs:
    """Shaxslar haqida ma'lumot."""
    def __init__(self, ism, familiya, passport, tyil):
        self.ism = ism
        self.familiya = familiya
        self.passport = passport
        self.tyil = tyil
    def get_info(self):
        """Shaxs haqida ma'lumot."""
        info = f"{self.ism} {self.familiya}"
        info += f"Passport: {self.passport}, {self.tyil}-yilda tug'ilgan."
        return info
    def get_age(self, yil):
        """Shaxsning yoshini qaytaruvchi metod."""
        return yil - self.tyil
inson = Shaxs("Hasan", "Alimov", "AB34243234", 1999)
print(f"{inson.get_info()}. {inson.get_age(2025)} yoshda.")

### Vorislik klass yaratish
class Talaba(Shaxs):
    """Talaba klassi"""
    def __init__(self, ism, familiya, passport, tyil):
        """Talabaning xususiyatlari."""
        super().__init__(ism, familiya, passport, tyil)
## Kodimizni tahlil qilaylik:
# • 1-qatorda klass nomidan so'ng, qavs ichida super klass nomini berdik
# • 5-qatorda (def __init__ ichida) klassimiz super klassning xususiyatlarini meros olishini  ko'rsatdik.
# Yangi yaratilgan Talaba klassimiz Shaxsning barcha xususiyatlari va metodlariga ega bo'ladi.
talaba = Talaba("Ali","Valijonov", "AD38473738", 2003)
print(talaba.get_info())
print(talaba.get_age(2025))

### Voris klassga xos xususiyatlar va metodlar

class Talaba(Shaxs):
    """Talaba klassi"""
    def __init__(self, ism, familiya, passport, tyil, idraqam):
        """Talabaning xususiyatlari."""
        super().__init__(ism, familiya, passport, tyil)
        self.idraqam =idraqam
        self.bosqich = 1
    def get_id(self):
        """Talabaning ID raqami"""
        return self.idraqam
    def get_boshqich(self):
        """Talabaning o'qish bosqichi"""
        return self.bosqich
talaba = Talaba("Akbar", "Umaraliyev", "AS82838", 2004, "0000234")
print(f"{talaba.get_info()} ID raqami: {talaba.get_id()}")
print(f"{talaba.get_boshqich()}-bosqich talabasi.")

## Voris klass boshqa klass uchun super klass bo'lshimi mumikin.


## Polimorfizm - super klass metodlarini qayta yozish
# Endi get_info() metodi talabaga mos ma'lumotlar qaytarishi uchun, Talaba klassi huddi shu nomli
# metodni qayta yozamiz:
class Talaba(Shaxs):
    """Talaba klassi"""
    def __init__(self, ism, familiya, passport, tyil, idraqam):
        """Talabaning xususiyatlari."""
        super().__init__(ism, familiya, passport, tyil)
        self.idraqam = idraqam
        self.bosqich = 1
    def get_id(self):
        """Talabaning ID raqami."""
        return self.idraqam
    def get_bosqich(self):
        """Talabanig o'qish bosqichi"""
        return self.bosqich
    def get_info(self):
        """Talaba haqidagi ma'lumotlar."""
        info = f"{self.ism} {self.familiya}"
        info += f"{self.get_bosqich()}-bosqich. ID raqami: {self.idraqam}"
        return info
talaba = Talaba("Salim", "Sultonov", "AD 19393822", 1997, "020933820")
print(talaba.get_info())



### Obyekt ichida obyekt
# Bazida klassimiz xususiyatlar va ular bilan ishlaydigan metodlarga to'lib keltishi, bu esa o'z navbatida obyektga
# murojat qilishni qiyinlashtirishi mumkin. Shunday holatlarda  ba'zi xususiyatlarn alohida klass ko'rinishida yozish
# va keyinchalik bu klassdan yaratilga obyektni boshqa obyektning xususiyati sifatida foydalanish mumkin.


class Manzil:
    """Manzil saqlash uchun klass"""
    def __init__(self, uy, kocha, tuman, viloyat):
        """Manzil xususiyatlari"""
        self.uy = uy
        self.kocha = kocha
        self.tuman = tuman
        self.viloyat = viloyat
    def get_manzil(self):
        """Manzilni ko'rish"""
        manzil = f"{self.viloyat} viloyati, {self.tuman} tumani, "
        manzil +=  f"{self.kocha} ko'chasi, {self.uy}-uy"
        return manzil
class Talaba(Shaxs):
    """Talaba klassi"""
    def __init__(self, ism, familiya, passport, tyil, idraqam, manzil):
        """Talabaning xususiyati"""
        super().__init__(ism, familiya, passport, tyil)
        self.idraqam = idraqam
        self.bosqich = 1
        self.manzil = manzil
    def get_id(self):
        """Talabaning ID raqami"""
        return self.idraqam
    def get_boshqich(self):
        """Talabaning o'qish bosqichi."""
        return self.bosqich
    def get_info(self):
        """Talaba haqidagi ma'lumot."""
        info = f"{self.ism} {self.familiya}."
        info+=f"{self.get_boshqich()}-bosqich. ID raqami: {self.idraqam}"
        return info
talaba_manzil = Manzil(12, "Huvaydo", "Olmazor", "Toshkent sh.")
talaba = Talaba("Bo'ri", "Boltaboyev", "AS1823284", 1990, '0000293', talaba_manzil)
print(talaba.manzil.get_manzil())
print(talaba.manzil.tuman)
print(talaba.get_info())