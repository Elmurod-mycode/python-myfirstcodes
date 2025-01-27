# Foydalanuvchidan istalgan davlatni kiritishni so'rang
# va shu davlatning poytaxtini konsolga chiqaring.
# Agar foydalanuvchi lug'atda yo'q davlatni kiritsa,
# "Bizda bunday ma'lumot yo'q" degan xabarni chiqaring.

davlatlar = {
    'o\'zbekiston': 'toshkent',
    'tojikistan': 'ashxabot',
    'ukraina' : 'kiyev',
    'rossiya': 'maskiva',
    "aqsh": "vashington",
    "marokas": "tunis",
    'buyuk britaniya': "london",
    'australiya' : 'sidney'
}
davlat = input("Istalgan davlatingizni kiriting: ").lower()

if davlat in davlatlar.keys():
    print(davlatlar[f"{davlat}"])
else:
    print("Bizda bunday ma'lumot yo'q")
country = input("Ixtiyor davlat kiriting: ").lower()
capital = davlatlar.get(country)
if capital ==None:
    print("Bizda bunday ma'lumot mavjud emas!")
else:
    print(f"{country.upper()}ning poytaxti {capital.title()}")
