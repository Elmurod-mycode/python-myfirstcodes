"""
2/1/2025
Muallif : Elmurod O'rinboyev
28- DARS. KLASSLAR
"""

x = 10
print(type(x))

matn = 'hello'
print(type(matn))

class Talaba:
    """Talaba nomli klass yaratamiz."""
    def __init__(self, ism, familiya, tyil):
        """Talabaning xususiyatlari.(properties)"""
        self.ism = ism
        self.familiya = familiya
        self.tyil = tyil
    def tanishtir(self):
        return f"Ism {self.ism} {self.familiya}. {self.tyil} yilda tug'ilganman."
    def get_ism(self):
        return self.ism
    def get_lastname(self):
        return self.familiya
    def get_yosh(self, HozirgiYil):
        self.hozir = HozirgiYil
        a = HozirgiYil - self.tyil
        return a
talaba1 = Talaba("Ali", "Valiyev", 2000)
print(talaba1.get_yosh(2025))
print(talaba1.get_ism())

# pass Operatori

class User:
    def __init__(self, name, username, email):
        self.name = name
        self. username = username
        self.email = email
    def describe():
        pass
    def get_email():
        pass
user = User('ali', "valiyev", 'skghd')

print(user.name)
