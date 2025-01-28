# 1/28/2025
# Muallif: Elmurod O'rinboyev

# 18-dars. While, Ro'yxatlar va lug'atlar

# While tsikli yordamida ro'yxatlar bilan ishlashni o'rganamiz.
# 18.1 While yordamida ro'yxatni to'ldirish

# ismlar = []
# print("Yaqin do'stlaringiz ro'yxatini tuzamiz.")
# n=1 # ismlarni sanash uchun o'zgaruvchi
# while True:
#     savol = f"{n}-do'stingiz ismini kiriting:"
#     ism = input(savol).title()
#     ismlar.append(ism)
#     javob = input("Yana ism qo'shasizmi? (ha/yo'q) ")
#     if javob == 'ha':
#         n+=1
#         continue
#     else:
#         break
# print("Do'stlaringiz ro'yxati: ")
# for ism in ismlar:
#     print(ism.title())
#     18.2 While yordamida lug'atni to'ldirish
# print("Do'stlaringiz yoshini saqlaymiz.")
# dostlar = {}
# ishora = True
# while ishora:
#     ism = input("Do'stingiz ismini kiriting: ")
#     yosh = input(f"{ism.title()}ning yoshini kiriting: ")
#     dostlar[ism]= int(yosh) # ism kalit, yosh qiymat
#     javob = input("Yana ma'lumot qo'shasizmi? (ha/yo'q)")
#     if javob == "yo'q":
#         ishora = False
# for ism, yosh in dostlar.items():
#     print(f"{ism.title()} {yosh} yoshda")

# 18.3 Ro'yxat elementlarini o'chirish
# avvalgi ham ishlatgan medodimizdan foydalanamiz bu .remove(qiymat)
cars = ['lacetti', 'nexia', 'toyata', 'nexia', 'audi', 'malibu', 'nexia']
while 'nexia' in cars: # toki nexia cars ro'yxati ichida ekan...
    cars.remove('nexia')# nexia ni ro'yxatdan olib tashla
print(cars)

# 18.4 Ro'yxatdan ro'yxatga element ko'chirish
talabalar = ['hasan', 'husan', 'ali', 'vali'] # ichi to'la ro'yxat
baholangan_talabalar = {} # bo'sh lug'at
while talabalar: # toki ro'yxat bo'shaguncha...
    talaba = talabalar.pop() # bittalab olishni boshladi...
    baho = input(f"{talaba.title()}ning bahosini kiriting: ") # bahoga qiymat berdim
    print(f"{talaba.title()} baholandi") # buni tastiqladim
    baholangan_talabalar[talaba] = baho # bunda ham kalit ham qiymat kiritilib lug'at hosil bo'ldi ro'yhatga ohshab .append() shart emas.
print(baholangan_talabalar)