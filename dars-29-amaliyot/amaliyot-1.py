# Avto degan yangi klass yarating. Unga avtomobillarga doir bo'lgan
# bir nechta xususiyatlar (model, rang, korobka, narh va hokazo) qo'shing.
# Ayrim xususiyatlarga standart qiymat bering (masalan, kilometer=0)

class Avto:
    def __init__(self, model, rang, korobka, narx):
        self.model = model
        self.rang = rang
        self.korobka = korobka
        self.narx = narx
        self.kilometr = 0
        self.kuzof = 'sedan'
    def get_model(self):
        return self.model
    def get_rang(self):
        return self.rang
    def get_korobka(self):
        return self.korobka
    def get_narx(self):
        return self.narx
    def get_info(self):
        return f"Model: {self.model.title()}, \nRangi: {self.rang}, \nKorobka: {self.korobka}, \nNarxi: {self.narx},\nYurgan masofa: {self.kilometr} km"
    def set_km(self, km):
        self.kilometr = km
        return km
    def set_model(self, model):
        self.model = model
        return model
    def set_korobka(self, korobka):
        self.korobka = korobka
        return korobka
    def set_narx(self, narx):
        self.narx = narx
        return narx
    def set_info(self):
        pass
avto1= Avto("Malibu", 'Oq', 'avto', 30000)
print(avto1.get_model())
print(avto1.get_narx())
print(avto1.set_km(2000))
print(avto1.get_korobka())
print(avto1.get_rang())
print(avto1.set_narx(26000))
print(avto1.set_model('Cobalt'))
print(avto1.set_korobka('maxanika'))
print(avto1.get_info())

