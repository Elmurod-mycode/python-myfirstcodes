"""
1/30/2025
muallif: Elmurod O'rinboyev
24-dars. FUNKSIYALAR.SO'NGI SO'Z.
"""
# lambda yohud nomsiz funksiya
# Pythonning o'ziga xon xususiyaetlaridan biri, nomsiz funksiyalar yaratish imkoniyati.
# Bunday funksiyalarni yaratishda def operatori o'rniga lambda operatori ishlatilgani uchun
# ham lambda funksiyalar deb ataladi.

# nomsiz funksiyalar quyidagicha yaratiladi:
# | lambda argument:ifoda
# lambda funksiyalari istalgan miqdordagi argumentlarga ega bo'lishi mumkin, ammo
# funksiya badanidan faqat bitta ifoda mavjud bo'ladi. Ifoda bafariladi va qaytariladi(return operatori shart emas.)

# Nomsiz funksiyalar biror ifodani tezda hioblab olishda qulay. Misol uchun
# quyidagi lambda funksiya ikkita argument qabul qiladi(), va aylana uzunligini qaytaradi:
import math
uzunlik = lambda pi, r : 2*pi*r
print(uzunlik(math.pi, 10))

product = lambda x,y:x**y
print(product(3,3))

def daraja(n):
    return lambda x:x**n
kvadrat = daraja(2)
kub = daraja(3)
print(f"3-ning kvadrati{kvadrat(3)} ga , kubi {kub(3)} ga teng.")

def daraja1(y):
    return lambda x:x**y
son_4chi_darajasi = daraja1(4)
son_5chi_darajasi = daraja1(5)
print(f"6 ning 5-darajasi {son_5chi_darajasi(6)} ga teng, 7 ning 4-darajasi {son_4chi_darajasi(7)} ga teng.")

# map() funksiyasi

from math import sqrt
sonlar = list(range(11)) # 0 dan 10 gacha sonlar ro'yxati
ildiz = list(map(sqrt, sonlar))
print(ildiz)

sonlar = list(range(11)) # 0 dan 10 gacha sonalr ro'yxati
def daraja2(x):
    """Berilgan sonning kvadratini qaytaruvci funksiya."""
    return x*x
print(list(map(daraja2, sonlar))) # sonlarning kvadratini hisoblaymiz

def kub(x):
    """Sonning kubini hisoblaydigan funksiya"""
    return x**3
print(list(map(kub, sonlar)))

kub = list(map(lambda x: x**3, sonlar))
print(kub)

# map() funksiyasi bo'lmaganda biz bunday dasturlarni for yordamida yozishimiz kerak bo'lar edi:
kvadrat = []
for son in sonlar:
    kvadrat.append(son*son)

a = [4, 2, 9]
b =[3,4,6]
a_plus_b = list(map(lambda x,y:x*y, a, b))
print(a_plus_b)

x = [3, 4, 5, 6, 7, 8]
y = [2, 54, 54, 46, 46, 78]
x_multiply_y = list(map(lambda a,b: a*b,x,y))
print(x_multiply_y)

# map() istalgan ko'rinishdagi ma'lumot turlari bilan ishlaydi:
ismlar = ['hasan', 'husan', 'olimm', 'sattor']
print(list(map(lambda matn: matn.upper(), ismlar)))

# filter() funksiyasi

# bu fuksiya ham argument sifatida ro'yxat va boshqa funksiyani qabul qili boladi va berilgan ro'yxxat elemntlarini
# berilgan funksiya yordamida saralaydi. Bunda argument sifatida uzatilgan funksiya mantiqiy qiymat qaytarishi kerak (True va False)

# import random as r
# sonlar = r.sample(range(100), 10) # 0-99 oralig'ida 10 ta tasodifiy sonlar
# def juftmi(x):
#     """x juft bo'lsa True , aks holda False qaytaruvchi funksiya."""
#     return x%2==0
# juft_sonlar = list(filter(juftmi, sonlar))
# print(sonlar)
# print(juft_sonlar)

# Keling endi shu dasturni lambda yordamida yozamiz:
import random as r
sonlar = r.sample(range(100), 10) # 0-99 oralig'ida 10 ta tasodifiy sonlaar
juft_sonlar = list(filter(lambda son: son%2==0, sonlar))
print(sonlar)
print(juft_sonlar)

# Kelish endi filter() funksiyasi yordamida matnlarni saralashga ham misollar ko'raylik

mevalar = ['olma', 'anjir', 'gilos', 'ananas', 'behi', 'kivi', 'banan', 'shaftoli']
mevalar_a = list(filter(lambda meva: meva.startswith('a'), mevalar))
print(mevalar_a)

# Quyidagi dastur esa mevalar ro'yxatidan nomi 5 yoki undan kam harfdan iborat  mevalarni saralab oladi.
mevalar2 = list(filter(lambda meva:len(meva)<=5, mevalar))
print(mevalar2)

mevalar3=list (filter(lambda meva: (meva.startswith('g') and meva.endswith('s')), mevalar))
print(mevalar3)