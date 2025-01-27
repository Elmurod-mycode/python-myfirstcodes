# avtolar = ['audi', 'bmw', 'volvo', 'kia', 'hyundai']
# for avto in avtolar:# bu yerda barcha avtomobillar birin ketin yurib chiqiladi
#     print(avto.title())# ... va har birini title() funksiyasi yordamida bosh harfini katta qilib chiqadi har bir elementni
#     #### ,......lekin shuni esda chiqarmaslik kerakki 'bmw' ni barchasi katta harfda  demak bu kamchilig mavjud kod hisoblanadi
# # buni to'g'irlash uchun if modulidan foydalaniladi
# avtolar = ['audi', 'bmw', 'volvo', 'kia', 'hyundai']
# avtolar1 = sorted(avtolar)
# for avto in avtolar1: #.... avtolar ichidagi har bir avto uchun
#     if avto == 'bmw': #....agar avto bmw ga teng bo'lsa....
#         print(avto.upper()) # avto nomini hammma harflarini katta bilan yoz.
#     else: # aks holda...
#         print(avto.title()) # avot nomini faqat birinchi harfini katta bilan yoz.
#
# ism = 'Ali'
# print(ism=='Ali')#  ism == 'Ali' (ism 'Ali' ga tengmi?) deb so'raganimizda, ifoda True (Ha) degan javob qaydaradi
# print(ism=="Vali") # ism == 'Vali' (ism 'Vali' ga tengmi?) deb so'raganimizda esa, ifoda False (Yo'q) deb qiymat qaytaradi.
# ism = 'Vali'
# print(ism.lower() == 'vali')
#
#
# ism = input('Ismingiz nima?\n>>>>>>>>') # Foydalanuvchi ismini so'raymiz
# if ism.lower() != 'ali' : # Agar ims Aliga teng bo'lmasa ...
#     print(f"Uzr, {ism.title()}biz Alini kutyabmiz.")#quyidagi xabar chiqadi
# else:
#     print("Salom, Ali")
# javob = float(input("3x7 nechiga teng?\n>>>>>"))
# if javob != 21:
#     print("Javob xato!")
#
# yosh = int(input("Yoshingiz nechida?\n>>>>>"))
# if yosh >= 18: # yosh 18 dan katta yoki teng bo'lsa
#     print("Xush kelibsiz!")
# else: #aks holda
#     print('Kirish mumkin emas!')

# login = input("Yangi loign tanlang: ")
# if len(login)<=5: # Login uzunligini tekshiramiz
#     print("Login 5 harfdan ko'proq bo'lishi shart!")
# else:
#     print("Loginningiz tastiqlandi")
#
# yil = int(input("Tug'ilgan yilingizni kiriting: "))
# if 2025-yil<18: # foydalanuchining yohisni hisoblaymiz
#     print(f"Yoshingiz {2025-yil}da ekan.")
#     print("Kirish mumkin emas!")
# else:
#     print("Xush kelibsiz!")


#
# yosh = int(input("Yoshingiz nechida?\n>>>>>>"))
# if yosh>65: print("Siz COVID-19 risk guruhida ekansiz")
#
# x, y = 25, 23  # x=25 va y = 23
# print('x>y') if x>y else print('x<y')
#                               """Amaliy mashholot"""
cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia']
for car in cars: # har bir mashina uchun yurib chiqiladi
    if car == 'gm': # agar car "gm" ga teng bo'lsa
        print(car.upper())# 'gm' so'zini bosh harflar bilan yozadi
    else: # aks holda...
        print(car.title()) # har bir mashinani bosh harfin katta qil


cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia']
for car in cars: # har bir element ustidan yurib chiq
    if car!="gm": # agar car "GM" ga teng bo'lmasa
        print(car.title()) # barcha elementni faqat bosh harfini katta qil
    else: # aks holda...
        print(car.upper()) # barcha harfini katta qilasan

login = input("Loginni kiriting: ")
if login.lower() == 'admin':
    print(f"Xush kelibsiz, {login.title()}.\nFoydalanuvchilar ro'yxatini ko'rasizmi?")
else:
    print(f"Xush kelibsiz, {login.title()}!")

birinchi_son = float(input("Ixtiyoriy birinchi son kiriting: "))
ikkinchi_son = float(input("Ixtiyoriy ikkinchi sonni kiriting: "))
if birinchi_son == ikkinchi_son:
    print("Ikkala son bir biriga teng ekan")

birinchi_son = float(input("Ixtiyoriy son kiriting: "))
ikkinchi_son = float(input("Ixtiyory son kiriting: "))
if birinchi_son <=0:
    print("Manfiy son")
else:
    print("Musbat son ekan")
if ikkinchi_son<=0:
    print("Manfiy son")
else:
    print("Musbat son.")

son = float(input("Ixtiyoriy son kiriting: "))
if son>0:
    print(f"Kiritgan soningizni ildiz osti qiymati: {son**(1/2)}")
else:
    print("Musbat son kiriting")