"""
sana: 1/30/2025
Muallif: Elmurod O'rinboyev
mavzu: Modul nima?
"""
# # Dasturni modullarga bo'lishni o'rganamiz
# # Funksiyaning qulayliklaridan biri, ko'p takrorlanadigan kodlarni funksiya ichida yashirishimiz va kerak bo'lganda
# # murojat qilishimi muminligigada. Maqsadimiz dasturimizni ixcham va tushunarli qilib, kelajakda o'zimiz yoki
# # boshqalar uchun ham "toza" kod qoldirish. Bu yo'nalsihida yana bir qadam qo'yib, dasturimizni modullarga
# # ajratishimiz mumkin.
#
# # Modul bu loyihamiz ichidagi alohida fayl bo'lib, dasturimiz davomida ishlatiladigan funksyalarni (va o'zgaruvchilarni)
# # mana shu faylga joylab, ko'zdan yashirib qo'yishimiz mumkin. Bu bizga asosiy dasturimizdan
# # chalg'imasdan kod yozish imkoniyatini beradi.
#
# # Modul va ining ichidagi fuksiyularni istalgan pat asoisy dasturimizga yuklab olishimiz, modullarni boshqa
# # dastuchilar bilan ulushishimiz yoki kelajakda o'zimizning boshqa loyihalarimizda foydalanishimiz mumkin.
#
# # Umuman olganda katta dasturlar bir necha o'nlab modullardan iborat bo'lishi tabiiy hol.
#
#
# """Modul yaratamiz"""
#
# # Modul yaratish uchun asosiy dasturimizdagi funksiyalarni yangi faylga ko'chiramiz xolos. Modulga oson murojat
# # qilishimiz uchun, faylimiz asosiy dasturimiz bilan bitta papkada bo'lgani afzal. Bunda adashib ketmaslik uchun,
# # loyihangizning(dasturining) asosoy faylini main.py deb nomlash o'rinli.
#
# # Kelisn, biz ham avto_info_mod.py degan fayl yaratamiz va ichiga quridagi 3 ta funksiyalarni joylaymiz:
#
# # avto_info_mod.py creat file
#
# """Modulni chaqirib olish"""
#
# import avto_info_mod # avto_info_mod faylini (modulini) chaqiriamiz
#
# avto1 = avto_info_mod.avto_info('Gm', "Malibu", "Qora", "avtomat", 2020, 30000)
# avto_info_mod.info_print(avto1)
#
# """Modulga qisqa nom berish"""
#
# import avto_info_mod as aim # avto_info_mod ni qisqa nom iam bila chaqiramiz
# avto1 = aim.avto_info("GM", "Malibu", "Qora", "Avtomat", 2020, 30000)
# aim.info_print(avto1)
#
#
# #    | Modulga qisqanom berganingizda bunday nomli boshqa o'zgaruvchi yoki funksiya yo'qligiga amin bo'ling,
# #    | Shuningdek, dastur davomida bu nomni boshqa o'zgaruvchilarga yoki funksiyalarga berib yubormang.
# """Modul ichidan ma'lum funksiyalarni ko'chirib olish"""
# # Agar katta modullardan faqatgina ba'zi funksiyalarga murojat qilish talab qilinsa, kerakli funksiyalarni from modul_nomi import funksiya1, funksiya2
# # komandasi yordamida o'zimizning dasturimizga ko'chirib olishimiz mumkin. Bu uslulni gulayligi, endi funksiyalarga to'g'ridan-to'g'ri murojat qilish mumkin
# # (modulni ismini yozmagan holda).
#
# # Misol uchun avvalgi kodimizda biz faqatgina avto_info va info_print funksiyalaridan foydalandik.
# # Shu funksiyalarni asosiy kodimizga ko'chirib olaylik:
#
# from avto_info_mod import avto_info, info_print
# avto1 = avto_info("GM", "Malibu", "qora", "avtomat", 2020, 30000)
# info_print(avto1)
#
# """Funksiyalarga qisqa nom berish"""
#
# # Huddi avvaldidek, ko'chirib olgan funksiyamizga ham qisqa nom berishimiz mumkin.
# from avto_info_mod import avto_info as ainfo, info_print as iprint
# avto1 = ainfo("Gm", "malibu", 'qora', 'avtomat', 2020, 30000)
# iprint(avto1)
#
# """Moful ichidagi barcha funksiyalarni ko'chirib olish"""
# # Modul ichidagi barcha funksiyalarni asosiy dasturga ko'chirib olish uchun from modul_nomi import * komandasidan foydalanamiz.
# from avto_info_mod import *
# avto1 = avto_info("gm", 'malibu', 'qora', 'avtomat', 2000, 23000 )
# info_print(avto1)
#
# ##   | Diqqat! bir necha sabablarga ko'ra bu usulda foydalanish tavsiya qilinmaydi. Katta modullarda yuzlab funksiyalar
# # bo'lishi mumkin, va funksiya nomi sizning dasturingizdagi boshqa funksiya yoki o'zgaruvchi bilan bir hil nomga ega bo'lsa, dastur xato ishlashiga olib keladi.
#
# """Modulda o'zgaruvchi saqlash"""
# # modulni ichida nafaqat funksiyalar, balki turli o'zgaruvchilarni ham saqlash mumkin.
# # Modul ichidagi o'zgaruvchilarga ham huddi yuqoridagi usullar bilan murojat qilish mumkin.

""" Python modullari"""

# math MODULi
# sqrt()- qavs ichida berilgan qiymatning kvadrat ildizini qaytaradi

import math
x = 400
print(math.sqrt(x))
y = 300
a = 34
print(math.sqrt(a))

print(math.sqrt(y))
# pow(x,y) - x ning y-darajasini qaytaradi
print(math.pow(5,5))

# pi-ning qiymatini saqlovchi o'zgaruvchi
from math import pi
print(pi)

print(math.log2(8))
print(math.log10(100))

"""         random MODULI           """
# random moduli tasodifiy sonlar iblan ishlash uchun qulay funksiyalarga boy. Keling ularda ayrimlari bilan tanishamiz.
# | randint(a,b)
# bu fuksiya a va b oralig'idagi tasodifiy butun son qaytaradi.

import random as r # random modulini r deb chaqirayapmiz
son = r.randint(0, 100) # 0 va 100 oralig'ida tasodifiy son
print(son)

# choice(x)
# x ning ichidan tasodifiy qiymatni qaytaruvchi funksiya. Bunda x bir necha elementdan
# iborat o'zgaruvchi (matn, ro'yxat) bo'lishi kerak.
ismlar = ['olim', 'ali', 'vali', 'alish', 'xasan', 'husan', 'jabbor', 'salim', 'hakim',
          'malik', 'shamsiddin', "g'abbor", 'akbar']
ism = r.choice(ismlar)
print(ism)
print(r.choice(ism)) # ismdan tasodifiy harf tanlaymiz

x = list(range(0, 51, 5))
print(x)
print(r.choice(x))
# shuffle(x)
# x ichidagi elementlarni tasodifiy tartibda qaytaruvchi funksiya. Bunda x bir necha
# elementdan iborat o'zgaruvchi (matn, ro'yxat) bo'lishi kerak.
x = list(range(12))
print(x)
r.shuffle(x)
print(x)