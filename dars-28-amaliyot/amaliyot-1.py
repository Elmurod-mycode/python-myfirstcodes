# Web sahifangiz uchun foydalanuvchi (user) klassini tuzing. Klassning xususiyatlari sifatida
# odatda ijtimoiy tarmoqlar talab qiladigan ma'lumotlarni kiriting (ism, foydalanuvchi ismi, email, va hokazo)
class User:
    """Foydalanuvchi haqidagi ma'lumotlarni chiqaruvchi klass."""
    def __init__(self, name, username, email, number):
        self.name = name
        self.user_n = username
        self.email = email
        self.number = number
    def name(self):
        return self.name
    def username(self):
        return self.user_n
    def email(self):
        return self.email
    def number(self):
        return self.number
    def user_info(self):

        return  f"Foydalanuvchining ismi:{self.name}\nFoydanlanuvchining 'foydalanuvchi ismi': {self.username} \nFoydalanuvchining Email manzili: {self.email} \nFoydalanuvching telefon raqami: {self.number}"

foydalanuvchi = User("Xasan", "xasan1261", 'xasanoripib@', 991234567)
print(foydalanuvchi.email)
print(foydalanuvchi.name)
class Avto:
    def __init__(self, model, color, age, pice ):
        self.model = model
        self.rangi = color
        self.yili = age
        self.narxi = pice
    def model(self):
        return self.model
    def color(self):
        return self.rangi
    def age(self, hozr_yil):
        return hozr_yil - self.yili
    def narxi(self):
        return self.narxi
avto1 = Avto('Malibu', 'oq', '2010', 30000)
print(avto1.rangi)
print(avto1.narxi)