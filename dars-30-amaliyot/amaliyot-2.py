# 1.Yuqoridagi Shaxs klassidan boshqa turli voris klasslar yaratib ko'ring
# (masalan Professor, Foydalanuvchi, Sotuvchi, Mijoz va hokazo)
#
# 2.Har bir klassga o'ziga hoz xususiyatlar va metodlar yuklang.
#
# 3.Barcha yangi klasslar uchun get_info() metodini qayta yozib chiqing.
#
# 4.Voris klasslardan yana boshqa voris klass yaratib ko'ring.
# Misol uchun Foydalanuvchi klassidan Admin klassini yarating.
#
# 5.Admin klassiga foydalanuvchida yo'q yangi metodlar yozing,
# masalan, ban_user() metodi konsolga "Foydalanuvchi bloklandi" degan matn chiqarsin.

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
class Professor(Shaxs):
    def __init__(self, ism, familiya, passport, tyil, kasbi, ilmiy_darajasi):
        super().__init__(ism, familiya, passport, tyil)
        self.kasbi = kasbi
        self.ilmiy_darajasi = ilmiy_darajasi
    def get_info(self):
        pass
class Foydalanuvchi(Shaxs):
    def __init__(self, ism, familiya, passport, tyil, kerakli_xizmat, manzil_f):
        super().__init__(self, ism , familiya, passport, tyil)
        self.kerakli_xizmat = kerakli_xizmat
        self.manzil = manzil_f
    def get_info(self):
        info = f"{self.ism} {self.familiya}."
        info += f"Passport: {self.passport}. Tug'ilgan yil: {self.tyil}"
        info += f"Kerakli xizmat turi: {self.kerakli_xizmat}."
        info += f"Manzili: {self.manzil}"
        return info
class Admin(Foydalanuvchi):
    def __init__(self, ism, familiya, passport, tyil, kerakli_xizmatlar, manzil_f, serves_xizmatlar, mahsulotlar, manzil):
        super().__init__(self, ism, familiya, passport, tyil, kerakli_xizmatlar, manzil_f )
        self.serves_xizmatlar = serves_xizmatlar
        self.mahsulotlar = mahsulotlar
        self.manzil = manzil
    def ban_user(self):
        return f"Foydalanuvchi bloklandi"


        