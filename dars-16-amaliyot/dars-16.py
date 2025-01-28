# 1/28/2025
# Muallif: Elmurod O'rinbeyev
# 16-dars. Nesting
# Ba'zida dasturlash jarayonida lug'atning ichida ro'yxatlar yoki boshqa
# lug'atni, yoki aksincha ro'yxat ichida lug'atni saqlash ham qo'l kelishi
# mumkin. Bu ingiliz tilida Nesting deyiladi. Nesting Pythondagi foydali
# xususiyatlardan biri.

# 16.1 Lug'atlar ro'yxati.
car_0 = {
    'model':'lacetti',
    'rang': 'oq',
    'yil': 2018,
    'narh': 13000,
    'km' : 5000,
    'karobka': 'avtomat'
        }
car_1 ={
    'model': 'nexia 3',
    'rang':'qora',
    'yil': 2015,
    'narh':9000,
    'km': 89000,
    'karobka': 'mexanika'
}
car_2 ={
    'model': 'gentra',
    'rang': 'qizil',
    'yil':2019,
    'narh': 15000,
    'km': 2000,
    'karobka': 'mexanika'
}
# Agar biz lug'atga alohida murojat qilish talab etsa biz uni nomlarini yodlab qolish talab etiladi.
car = car_0
print(f"{car['model'].title()},"
      f"{car['rang']} rang,"
      f"{car['yil']}-yil, narhi: {car['narh']}$")
car = car_1
print(f"{car['model'].title()},"
      f"{car['rang']} rang,"
      f"{car['yil']}-yil, narhi: {car['narh']}$")
car = car_2
print(f"{car['model'].title()},"
      f"{car['rang']} rang,"
      f"{car['yil']}-yil, narhi: {car['narh']}$")

# Keling, barcha avtolarni bitta ro'yxatga joylaymiz, va for tsikli yordamida birma-bir konsolga chiqaramiz:
cars = [car_0,car_1, car_2]
for car in cars:
    print(f"{car['model'].title()}, {car['rang']} rang,"
          f"{car['yil']}-yil, narxi {car['narh']}$")

# Bu kodimizni qisqartish va soddalashtirishga olib keladi.

# Endi quydagicha murojat qilishimiz mumkin va ularni nomlarini yodlab olishimiz shart emas.
print(cars[0])


# for tsikli yordamida bir bo'sh lugatlar ro'yxatni ham yaratib olishimiz mumkin:
malibus = []
# Malibu mashinalari uchun bo'sh ro'yxat yaratdik
for n in range(10):
    new_car = { # har bir yangi mashina uchun lug'at yaratamiz
        'model':'malibu',
        'rang':None, # rangi noaniq
        'yil':2020,
        'narh':None, # narhi belgilanmagan
        'km':0,
        'korobka':'avto'
        }
    malibus.append(new_car) # yangi lug'atni ro'yxatga qo'shamiz
for car in malibus:
    print(car)

# yuqoridagi ro'yxatga endi 3ta mashinaga 'rang' ga qiymat beramiz.
for malibu in malibus[:3]:
    malibu['rang']='qizil'
# keyingi 3 tasiga esa qora
for malibu in malibus[3:6]:
    malibu['rang'] = 'qora'
for malibu in malibus[6:]:
    malibu['rang'] = 'oq'
    malibu['korobka'] = 'mexanika'

for car in malibus:
    print(car)
# ohirgi oqlarini endi avotodan mexanikga o'tkazamiz

# endi narx belgilaymiz korobkadan kelib chiqib

for malibu in malibus:
    if malibu['korobka'] == 'avto':
        malibu['narh'] = 40000
    else:
        malibu['narh'] = 35000
for car in malibus:
    print(car)

# 16.2 Lug'at ichida ro'yxat

dasturchilar = {
    'akbar' : ['python', 'c++'],
    'vali' : ['html', 'css', 'js'],
    'halil' : ['php', 'sql'],
    'maryam': [ 'c++', 'c#']
}
for ism, tillar in dasturchilar.items():
    print(f"\n {ism.title()} quyidagi dasturlash tillarini biladi: ", end='')
    for til in tillar:
         print(til.upper(), end= " ")

# 16.3 Lug'at ichida lug'at
# Bunday qilishtavsiya etilmasada, istisno holatlarda lug'at ichidagi qiymatlarni lug'at ko'rinishida ham saqlash mumkin. Misol uchun, ish joyingizdagi hamkasblaringiz haqidagi ma'lumotlarni saqlashda, hamkasbingizning ismi kalit, u haqidagi ma'lumotlarni esa lug'at ko'rinishida brilishi mumkin.
hamkasblar = {
    'ali' : {'familiya': 'valiyev',
             'tyil':1995,
             'malumot': 'oliy',
             'tillar': ['python', 'c++']
             },
    'vali' : {'familiya': 'aliyev',
              'tyil': 2001,
              'malumot':"o'rta-maxsus",
              'tillar': ['html', 'css', 'js']
              },
    'hasan': {'familiya': 'aliyev',
              'tyil': 1999,
              'malumot': "maxsus",
              'tillar': ['python', 'php']
              }
        }
# Hamkasblar to'g'risidagi ma'lumotlarni esa quyidagicha ko'rish mumkin:
for ism, info in hamkasblar.items():
    print(f"\n{ism.title()} {info['familiya'].title()},"
          f"{info['tyil']}-yilda tug'ilgan."
          f"Ma'lutoi: {info['malumot']}.\n"
          f"Quyidagi dasturlash tillarini biladi: ", end='')
    for til in info['tillar']:
        print(til.upper(), end=' ')