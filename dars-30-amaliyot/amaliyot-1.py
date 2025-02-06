# 1.Talaba klassiga yana bir, fanlar degan xususiyat qo'shing.
# Bu xususiyat parametr sifatida uzatilmasin va obyekt
# yaratilganida bo'sh ro'yxatdan iborat bo'lsin (self.fanlar=[])

#2.Fan degan yangi klass yarating va bu klassdan turli fanlar uchun alohida obyektlar yarating.
#
# 3.Talaba klassiga fanga_yozil() degan yangi metod yozing. Bu metod parametr sifatida
# Fan klassiga tegishli obyektlarni qabul qilib olsin va talabaning fanlar ro'yxatiga qo'shib qo'ysin.
#
# 4. Talabaning fanlari ro'yxatidan biror fanni o'chirib tashlash uchun remove_fan() metodini yozing.
# Agar bu metodga ro'yxatda yo'q fan uzatilsa "Siz bu fanga yozilmagansiz" xabarini qaytarsin.

class Fanlar:
    """Fanlar saqlash uchun klass"""
    def __init__(self, tarix, matematika, kimyo, biologiya):
        self.tarix = tarix
        self.matematika = matematika
        self.kimyo = kimyo
        self.biologiya = biologiya
    def add_tarix(self):
        return self.tarix
    def add_matematika(self):
        return self.matematika
    def add_kimyo(self):
        return self.matematika
    def add_kimyo(self):
        return self.kimyo
    def add_biolagiya(self):
        return self.biologiya
class Talaba:
    def __init__(self, ism, familiya, tyil, fan):
        self.ism = ism
        self.familiya = familiya
        self.tyil = tyil
        self.bosqich = 1
        self.fan = fan
        self.fanlar = []
    def get_name(self):
        """Talabaning ismi"""
        return self.ism
    def get_lastname(self):
        """Talabaning ismi"""
        return self.familiya
    def get_info(self):
        """Talaba haqida ma'lumot"""
        info = f"{self.ism} {self.familiya}."
        info += f"{self.bosqich}-boshqich talabasi."
        return info
    def fan_yozil(self, fan_nomi):
        """Fan qo'shish funksiyasi"""
        if hasattr(self.fan, fan_nomi):  # Agar Fanlar klassida metod bo'lsa
            fan_qiymati = getattr(self.fan, fan_nomi)()  # Dinamik metod chaqirish
            self.fanlar.append(fan_qiymati)
            return self.fanlar
        else:
            return "Bunday fan mavjud emas"
    def get_fanlar(self):
        return self.fanlar
fanlar1 = Fanlar("Yangi O'zbekiston tarixi", 'Oliy matematika', 'Organik kimyo', 'Odam anatomiyasi')
talaba = Talaba('Ali', "Valiyev", 2000 , fanlar1)
print(talaba.fan_yozil('add_ona_tili'))



