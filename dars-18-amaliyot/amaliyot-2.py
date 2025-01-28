#e-bozor uchun mahsulotlar va ularning narhlari lug'atini shakllantiruvchi dastur yozing.
# Foydalanuvchidan lug'atga bir nechta elementlar (mahsulot va uning narhi) kiritishni so'rang.

print("E-bozor uchun mahsulotlar va ularning narxlari lug'atini shaklantiruvchi dastur.")
e_bozor = {}
n=1
ishora = True
while ishora:
    mahsulot = input(f"{n}-Mahsulotningizni kiriting: ")
    narx = input("Uning narxi qancha bo'ladi: ")
    e_bozor[mahsulot]=narx
    savol = input("Yana mahsulot kiritishni ishtaysizmi? (ha/yo'q)")
    n+=1
    if savol == "yo'q":
        ishora = False

print(e_bozor)