# Avvalgi darslarimizda yaratgan Shaxs va Talaba klasslariga yopiq xususiyatlar
# qo'shing va ularning qiymatini ko'rsatuvchi va o'zgartiruvchi metodlar yozing.
# Yuqoridagi klasslarga talabalar_soni va odamlar_soni degan klassga oid xususiyatlar qo'shing.
# Klassga oid xususiyatlar bilan ishlash uchun maxsus @classmethod lar yozing

class Shaxs:
    __num_person = 0
    def __init__(self, name, lastname, year, location):
        self.name = name
        self.lastname = lastname
        self.year = year
        self.location = location
        Shaxs.__num_person +=1

    @classmethod
    def get_num_person(cls):
        return cls.__num_person

    def get_info(self):
        info = f"{self.name} {self.lastname}."
        info+= f"{self.year}da tug'ilgan. {self.location}lik."
        return info
person1 = Shaxs('Ali', "Valiliyev", 1999, "Toshkent shahar")
person2 = Shaxs('Akbar', "Salimov", 1978, 'Samarqand')
person3 = Shaxs("Sultan", "Hakimov", 1998, 'Sirdaryo')
print(Shaxs.get_num_person())
print(person1.get_info())

class Talaba(Shaxs):
    __num_talaba = 0
    def __init__(self, name, lastname, year, location, yonalish):
        super().__init__( name, lastname, year, location)
        self.yonalish = yonalish
        self.__bosqich = 1
        Talaba.__num_talaba +=1
    @classmethod
    def get_num_talba(cls):
        return cls.__num_talaba
    def boshqich(self):
        return self.__bosqich

    def get_info(self, talabalik_olindi):
        if talabalik_olindi == "talabalikka olindi":
            talaba = f"{self.name} {self.lastname}."
            talaba+= f"Talabalar safiga qo'shildi."
            return talaba
        else:
            talaba_emas = f"{self.name} {self.lastname}."
            talaba_emas += f"Afsus. Talabalikka olinmadi."
            return talaba_emas
talaba1 = Talaba("Karim", 'Abdullayev', 2000, 'Toshkent', 'Iqtisodiyot')
talaba2 =  Talaba("Abdumannob", 'Jumaniyozov', 1997, "Samarqand", 'Marketing')
print(talaba1.boshqich())
print(Talaba.get_num_talba())