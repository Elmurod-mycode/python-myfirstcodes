# 1/29/2025
# Muallif: Elmurod O'rinboyev

## 20-DARS. QIYMAT QAYTARUVCHI FUNKSIYA

## FUNKSIYADAN ODDIY QIYMAT QAYTARISH

# def toliq_ism_yasa(ism, familiya):
#     """To'liq ism qaytaruvchi funksiya."""
#     toliq_ism = f"{ism} {familiya}"
#     return toliq_ism
#
# ism = toliq_ism_yasa('ali', 'bakir')
# print(ism)
# demak return funksiyasini avzaligi kiritilgan qiymatni keyinchallik ham foydalanishimiz mumkin.

## IXTIYORIY ARGUMENTLAR
#
# def toliq_ism_yasa(ism, familiya, otasining_ismi=''):
#     """To'liq ism qaytaruvchi funksiya."""
#     if otasining_ismi: # otasining_ismi mavjudligini tekshiramiz
#         toliq_ism = f"{ism} {otasining_ismi} {familiya}"
#     else:
#         toliq_ism = (f"{ism} {familiya}")
#     return toliq_ism.title()
#
# talaba1 = toliq_ism_yasa('ali', 'valiyev')
# talaba2 = toliq_ism_yasa('akbar', 'nazrullayev', 'hallilivich')
# print(f"Darsga kelmagan talabalar: {talaba1} va {talaba2}")
#
#
# ## FUNKSIYADAN LUG'AT QAYTARAMIZ
#
# def avto_info(kompaniya, model, rangi, korobka, yili, narxi=None):
#     avto = {'kompaniya': kompaniya,
#             'model': model,
#             'rangi': rangi,
#             'korobka':korobka,
#             'yil': yili,
#             'narxi': narxi}
#     return avto
# avto1 = avto_info("GM", 'cobalt', 'oq','mexanika', 2020,
#                  30000)
# avto2 = avto_info('hyundai', 'sonate', 'qora', 'avomat', 2023,
#                   )
# avtolar= [avto1, avto2]
# print("Onlayn bozordagi mavjud abtomashinalar: ")
# for avto in avtolar:
#     if avto['narxi']:
#         narx = avto['narxi']
#     else:
#         narx = "Noma'lum"
#     print(f"{avto['rangi']}, {avto['model']}. Narxi: {narx}")
#
## FUNKSIYADAN RO'YXAT QAYTARAAMIZ.

def oraliq(min, max, qadam=None):
    sonlar = [] # bo'sh ro'yxat
    while min<max:
        if qadam == None:
            sonlar.append(min)
            min +=1
        elif qadam !=None:
            sonlar.append(min)
            min+=qadam
    return sonlar
print(oraliq(0,21,2))

## FUNKSIYALARNI TSIKLDA ISHLATISH
def avto_info(kompaniya, model, rangi, korobka, yili, narhi=None):
    avto = {'kompaniya':kompaniya,
            'model':model,
            'rang':rangi,
            'korobka':korobka,
            'yil':yili,
            'narh':narhi}
    return avto
print("Saytimizdagi avtolar ro'yxatini shakllantiramiz.")
avtolar = []  # salondagi avtolar uchun bo'sh ro'yxat
while True:
    print("\nQuyidagi ma'lumotlarni kiriting")
    kompaniya = input("Ishlab chiqaruvchi: ")
    model = input("Modeli: ")
    rangi = input("Rangi: ")
    korobka = input("Korobka: ")
    yili = input("Ishlab chiqarilgan yili: ")
    narhi = input("Narhi: ")

    # Foydalanuvchi kiritdan ma'lumotlardan avto_info yordamida
    # lug'at shakllantirib, har bir lug'atni ro'yxatga qo'shamiz:
    avtolar.append(avto_info(kompaniya, model, rangi, korobka, yili, narhi))

    # Yana avto qo'shish-qo'shmaslikni so'raymiz
    javob = input("Yana avto qo'shasizmi? (yes/no): ")
    if javob == 'no':
        break

print(avtolar)