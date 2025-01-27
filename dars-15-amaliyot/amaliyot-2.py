#Davlatlar va ularning poytaxtlari lug'atini tuzing.
# Avval lug'atdagi davlatlarni, keyin poytaxtlarni alohida-alohida,
# alifbo ketma-ketligida konsolga chiqaring.

davlatlar = {
    'Uzbekistan': 'Tashkent',
    'Tajikistan': 'Ashxabot',
    'Ukraina' : 'Kiyev',
    'Russia': 'Maskva',
    "USA": "Washington",
    "Marokas": "Tunis",
    'UK': "London",
    'Australiya' : 'Cidney'
}
print("Countres:")
for davlat in sorted(davlatlar.keys()):
    print(davlat)
print("Capitals:")
for poytaxt in sorted(davlatlar.values()):
    print(poytaxt)