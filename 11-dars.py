# ### BIR NECHTA SHARTLARNI TEKSHIRISH
# #  fi-elif-else zanjiri, and, or operatorlari bilan tanshamiz
#
# yosh = int(input("Yoshingiz nechida?"))
# if yosh<=4:
#     print("Sizga kirish bepul.")
# elif yosh<=12:
#     print("Sizga kirish 5000 so'm")
# else:
#     print("Sizga kirish 10000 so'm")
# # kodni soddalashtirish
# yosh = int(input("Yoshingiz nechida? \n >>>>>"))
# if yosh<=4:
#     price=0
# elif yosh<=12:
#     price = 5000
# else:
#     price = 10000
# print(f"Sizga kirish {price} so'm")
#
# #####
#
# yosh = int(input("Yoshingiz nechida?\n>>>>"))
# if yosh<=4: # yosh bolalarga bepul
#     price =0
# elif yosh<=12: # 4 dan 12 yoshgach 5 000 so'm
#     price=5000
# elif yosh<65: # 12 dan katta va 65 dan kichiklarga narx 1 000 so'm
#     price = 10000
# else: # qariyalarga esa 8 000 som
#     price =8000
# print(f"Sizga kirish {price} so'm")
#
#
#
# #######
#
# yosh = int (input("Yoshingiz nechida? \n>>>>>"))
# if yosh<=4:
#     price = 0
# elif yosh<=12:
#     price = 5000
# elif yosh<65:
#     price = 10000
# elif yosh>= 65:
#     price = 8000
# print(f"Sizga kirish {price} so'm")
#
################

# kun = input("Bugun nima kun? >>>>")
# if kun.lower()== "shanba" or kun.lower()=="yakshanba":
#     print("Bugun dam olish kuni.")
# else:
#     print("Bugun ish kuni")

############

# kun = input("Bugun nima kun? ")
# harorat = float(input("Havo harorati qanday? "))
# if kun.lower()=="yakshanba" and harorat>=30:
#     print("Cho'milgani ketdik!")
# elif kun.lower()=="yakshanba" and harorat<30:
#     print("Uyda dam olamiz")
# elif kun.lower()=="shanba" and harorat>=30:
#     print("Bugun chomilishga boramiz!")
# elif kun.lower()=="shanba" and harorat<30:
#     print("Bugun uyda qolamiz!")


################

# kun = input("Bugun nima kun?   ")
# harorat = float(input("Havo harorati qanday?   "))
# if (kun.lower()=="shanba" or kun.lower()=="yakshanba") and harorat>=30:
#     print("Bugun chomilishga boramiz!")
# elif (kun.lower()=="shanba" or kun.lower()== "yakshanba") and harorat<30:
#     print("Budun uyda qolamiz!")


########
#
# narx = 15000 # mijoz 15 000 so'mga taom oldi.
# choy = True # mijoz choy ham oldi
# salat = False # mijoz salat olmadi
#
# if choy and salat: # agar mijoz choy ham salat ham olgn bo'lsa
#     narx = narx + 10000
# elif choy or salat: # agar choy yoki salat olgan bo'lsa
#     narx = narx + 5000 # narx 5000 so'm qo'shamiz
# print(f"Jami {narx} so'm")#yakuniy narxni chiqaramiz

#############

# narx = 15_000 # mijoz 15 000 so'mga ovqat oldi
# choy = True
# salat = False
# non = True
# kompot = False
# assorti = True
# # Quyidagi har bir shart alohida tekshiriladi va bir birga bog'liq ema
# if choy: # agar choy olsa
#     print("Mijoz choy oldi")
#     narx = narx + 3000
# if salat: # agar salat olsa
#     print("Mijoz salat oldi")
#     narx = narx + 5000
# if non : # agar non olsa
#     print("Mijoz non oldi.")
#     narx =narx + 2000
# if kompot: # agar kompot olsa
#     print("Mijoz kompot oldi.")
#     narx =narx+5000
# if assorti: # agar assorti olsa
#     print("Mijoz assorti oldi.")
#     narx = narx + 15000
# print(f"Jami {narx} so'm")

menu = ["osh", 'qazonkabob', 'shashlik', 'norin', 'somsa']
# print('manti'in menu)
# print('osh' in menu)
# ovqat = input("Nima ovqat yeysiz?")
# if ovqat.lower()in menu:
#     print("Buyurtma qabul qilindi.")
# else:
#     print("Afsuski bizda bunday ovqat yo'q")
# print("manti" not in menu)
# print("osh" not in menu)
#
# ovqat = input("Nima ovqat yeysiz?>>>")
# if ovqat.lower()not in menu:
#     print("Afsuski bizda bunday ovqat yo'q?")
# else:
#     print("Buyurtma qabul qilindi.")

# buyurtmalar = ["osh", "somsa", "manti", "shashlik"]
#
# for taom in buyurtmalar:
#     if taom in menu:
#         print(f"Menuda {taom} bor.")
#     else:
#         print(f"Kechirasiz, menuda {taom} yo'q.")
#
# if buyurtmalar: # ro'yxatda biror elemet bo'lsa bu ifoda True qaytaradi
#     for taom in buyurtmalar:
#         if taom in menu:
#             print(f"Menuda {taom} bor.")
#         else:
#             print(f"Kechirasiz, menuda {taom} yo'q.")
# else: # agar ro'yxat bo'sh bo'lsa
#     print("Savatchangiz bo'sh!")


###################

# 1.  Foydalanuvchidan juft son kiritishni so'rang. Agar foydalanuchdi juft son kiritsa "Rahmat!, agar toq son kritsa "Bu son juft emas" dega xabarni chiqaring.

# son = float(input("Ixtiyoriy son kiriting?\n>>>>>"))
# juft_son = son%2
# if juft_son==0:
#     print("Rahmat!")
# else:
#     print("Bu son juft emas!")

# Foydalanuvchi yoshini so'rang, va muzeyga kirish uchun chipta narhini quyidagicha chiqaring:
#
# Agar foydalanuvchi 4 yoshdan kichkina yoki 60 dan katta bo'lsa bepul
# Agar foydalanuvchi 18 dan kichik bo'lsa 10000 so'm
# Agar foydalanuvchi 18 dan katta bo'lsa 20000 so'm

# yosh = int(input("Yoshingiz nechida?>>>>>"))
# if yosh<=4 or yosh>=60:
#     narx = 0
# elif yosh<18:
#     narx = 10000
# elif yosh>=18:
#     narx = 20000
# print(f"Muzeyga kirish narxi {narx} so'm.")
# Foydalanuvchidan ikita son kiritishni so'rang, sonlarni solishtiring va ularning teng yoki katta/kichikligi haqida xabarni chiqaring
# birinchi_son = float(input("Birinchi ixtiyoriy soningizni kiriting: "))
# ikkinchi_son = float(input("Ikkinchi ixtiyoriy soningizni kiriting:  "))
# if birinchi_son == ikkinchi_son:
#     print("Sonlar bir-biriga teng ekan.")
# elif birinchi_son < ikkinchi_son:
#     print("Ikkinchi son katta ekan.")
# elif birinchi_son > ikkinchi_son:
#     print("Birinchi son katta ekan.")


###############

# mahsulotlar degan ro'yxat yarating va kamida 10 ta turli mahsulotni kiriting.
# Yangi, savat degan bo'sh ro'yxat yarating va foydalanuvchidan savatga kamida 5 ta mahsulot kiritishni so'rang.
# Savatdagi elementlarni, mahsulotlar ro'yxati bilan solishtiring va qaysi biri ro'yxatda bo'lsa,
# "Mahsulot do'konimizda bor" aks holda, "Mahsulot do'konimizda yo'q" degan xabarlarni chiqaring.

# mahsulotlar = ['sovun', 'shanpun', 'pichoq', 'olma',
#                'banan', 'shapka', 'zelin', 'gilos',
#                'sharbat', 'makaron'   ] # Dokondagi bor 10 ta mahsulot
# savat = [] # Foydalanuvchining bo'sh savati.
# for n in range(5): # 5 talik tsik qilib oldim yani 5 marta mahsulot kiritish uchun
#     savat.append(input(f"{n+1}- mahsulot: ")) # va uni savatga.append qildim bunining
#                                               # uchun input orqali ma'lumotni kiritishini
#                                               # soradim n+1 bir esa pythonda sanash 0 dan
#                                               # boshlangani sababli n+1(0+1) esa bir dan
#                                               # boshlanishiga sabab bo'ladi
# print(savat) # barchasi listga tushganini tekshirib oldik
# for mahsulot in savat: # savatni birma bir yurib chiqib
#                        # olamiz mahsulot degan yangi o'zgaruvchi orqali
#     if mahsulot in mahsulotlar: # va o'sha harbir yurib chiqqanda savat ichidagi elementni
#                                 # vaqtinchalik o'z xotirasida saqlab mahsulotlar degan royhatimizda
#                                 # bor yoki yo'qligini tekshirib chiqadi. bunda mexanizm True va False ga
#                                 # asoslangan
#         print(f"Do'konimizda {mahsulot} bor") # agar bor bo'lsa ha degani yani
#                                               # .... agar mahsolot bo'lsa True.... qaytaradi
#     else: ### ... aks holda
#         print(f"Afsuski,bizda  {mahsulot} yo'q")#....False... qaytaradi

########################
#Yuqoridagi dasturni quyidagicha o'zgartiring: foydalanuvchidan 5 ta mahsulot kiritishni so'rang.
#Foydalanuvchi so'ragan va do'konda bor mahsulotlarni yangi bor_mahsulotlar degan ro'yxatga,
# do'konda yo'q mahsulotlarni esa mavjud_emas degan ro'yxatga qo'shing.
# Agar mavjud_emas ro'yxati bo'sh bo'lsa, "Siz so'ragan barcha mahsulotlar do'konimizda bor" degan xabarni,
# aks holda esa "Quyidagi mahsulotlar do'konimizda yo'q: ....." degan xabarni chiqaring.

# mahsulotlar = ['sovun', 'shanpun', 'pichoq', 'olma',
#                'banan', 'shapka', 'zelin', 'gilos',
#                'sharbat', 'makaron'   ] # Dokondagi bor 10 ta mahsulot
# savat = [] # Foydalanuvchining bo'sh savati.
# for n in range(5): # 5 talik tsik qilib oldim yani 5 marta mahsulot kiritish uchun
#     savat.append(input(f"{n+1}- mahsulot: ")) # va uni savatga.append qildim bunining
#                                               # uchun input orqali ma'lumotni kiritishini
#                                               # soradim n+1 bir esa pythonda sanash 0 dan
#                                               # boshlangani sababli n+1(0+1) esa bir dan
#                                               # boshlanishiga sabab bo'ladi
# print(savat) # barchasi listga tushganini tekshirib oldik
# bor_mahsulotlar = []
# yoq_mahsulotlar = []
# for mahsulot in savat: # tsiklni birma bir yurib chiqamiz.
#     if mahsulot in mahsulotlar: # ... agar mahsulot mahsulotlar ichida bor bo'lsa.....
#         bor_mahsulotlar.append(mahsulot) #....bor_mahsulotlar ichiga append ("qo'shing") qiling.....
#     else: # ....aks holda....
#         yoq_mahsulotlar.append(mahsulot)# .... yo'q mahsulotlar ichiga append ("qo'shing") qiling.....
# print(bor_mahsulotlar)# tekshirib ko'ramiz
# print(yoq_mahsulotlar)# tekshirib ko'ramiz
# if len(yoq_mahsulotlar) == 0: # ....agar list uzunligi 0 ga teng bo'lsa
#     print("Siz so'ragan barcha mahsulotlar do'konmizda bor.") # ...< shu javob chiqishi kerak.
# else:#... aks holda
#     print("Siz so'ragan quyidagi mahsulotlar do'konimizda yo'q: ")
#     for n in yoq_mahsulotlar:# .... quyidagi mahsulotlar yuqoridagi javob asnosida ro'yxat bo'lib chiqadi yo'q mahsulotlar.
#         print(n)


##############
#foydalanuvchilar degan ro'yxat tuzing, va kamida 5 ta login qo'shing.
# Foydalanuvchidan yangi login tanlashni so'rang va foydalanuvchi kiritgan loginni foydalanuvchilar degan ro'yxatning tarkibi bilan solishtiring.
# Agar ro'yxatda bunday login mavjud bo'lsa, "Login band, yangi login tanlang!" aks holda "Xush kelibsiz, foydalanuvchi!" xabarini chiqaring.

# foydalanuvchilar = ["ali", "bakir", "salim","malohat", "anvar"]
# foydalanuvchi = input("Yangi login kiriting: ")
# foydalanuvchi= foydalanuvchi.lower()
# if foydalanuvchi in foydalanuvchilar:
#     print("Login band, yangi login tanlang!")
# else:
#     print(f"Xush kelibsiz, {foydalanuvchi.title()}!")

# Foydalanuvchidan biror butun son kiritishni so'rang.
# Foydalanuvchi kiritgan sonni 2 da 10 gacha bo'lgan sonlardan qay biriga qoldiqsiz bo'linishini konsolga chiqaring.
# son = int(input("Ixtiyoriy butun son kiriting: \n>>>>>>>>>>>>"))
# for n in range(2,11):
#     if son%n == 0:
#         print(f"{son} soni quydagi songa qoldiqsiz bo'linadi: {n}")
son = int(input("Istalgan butun son kiriting: "))

for n in range(2,11):
    if not (son%n):
        print(f"{son} soni {n} ga qoldiqsiz bo'linadi")











