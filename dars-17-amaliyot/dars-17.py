# 1/28/2025
# Muallif: Elmurod O'rinboyev
# 17-dars. while Tsikli
# ism = input("Izmingiz nima?")
# print(ism)
# savol = f"Salom, {ism.title()}. Yoshingiz nechida? "
# yosh = input(savol)
# print(yosh)
#
# # 17.1 Sonlar va input()
#
# ism = input("Ismingiz nima?")
# savol = (f"Salom, {ism.title()}. Yoshingiz nechida?")
# yosh = input(savol)
# yosh = int(yosh) # yosh ni butun songa o'tkazamiz
# height = input("Bo'yingi nechida metr?")
# height = float(height) # bo'yni o'nlik songa o'tkazamiz.
# print(yosh)
# print(height)

# 17.2 while Tsikli bilan tanishamiz
# while so'zi ingiliz tilidan "toki" yoki "-gacha" deb tarjima qilinadi.
# son = 1 # son ga qiymatini beramiz
# while son<=5: # toki son 5 dan kichik yoki teng ekan....
#     print(son, end=" ") # son ni konsolga chiqaramiz,
#     son = son+1 # songa 1 qo'shamiz
# while va input()
# Shu paytgacha yozgan dasturlarimiz faqatgina bir martta bajarilayotgan edi.
# while tsikli yordamida dasturni to'xtatish imkoniyatini foydalanuvchiga berishimiz mumkin.
# print("Sonni kvadratini qaytaruvchi dastur.")
# savol = "Istalgan sonningizni kiriting "
# savol += "(dasturdan chiqish uchun 'exit' qiymatini kiriting.): \n>>>>"
# qiymat = ''
# while qiymat != 'exit':
#     qiymat = input(savol)
#     if qiymat != 'exit':
#         print(float(qiymat)**2)

## 17.3 Ishora(flag)
# print("Kiritilgan sonni kvadratinii qaytaruvchi dastur. ")
# savol = "Istalgan sonni kiriting "
# savol += "(dasturni to'xtatish uchun 'exit' dab yozing): "
# ishora = True
# while ishora:
#     qiymat = input(savol)
#     if qiymat == 'exit':
#         ishora = False
#     else:
#         print(float(qiymat)**2)
# # 17.4 Preak operatori
# print("Kirtiogansonning kvadratini qaytaruvchi dastur.")
# savol = "Istalgan son kiriting "
# savol+= "(dasturni to'xtatish uchun 'exit' deb yozing: \n>>>"
# while True: # abadiy tshikl
#     qiymat = input(savol)
#     if qiymat== 'exit':
#         break # tsiklni to'xtatish
#     else:
#         print(float(qiymat)**2)

# Break operatori for tsiklini to'xtatish uchun ham ishlatiladi.
sonlar = list(range(1,11))
for son in sonlar:
    if son==5: # son 5 ga teng bo'lsa kod to'xtaydi
        break
    print(f"{son}ning kvaddrati {son**2} ga teng.")
# 17.5 Continue operatori
sonlar = list (range(1,11))
for son in sonlar:
    if son == 5 : # son 5 ga teng bo'lsa tsikl boshiga qaytadi.
        continue
    print(f"{son} ning kvadrati {son**2} ga teng. ")

son = 0
while son<10:
    son +=1
    if son%2!=0:
        continue
    else:
        print(son)