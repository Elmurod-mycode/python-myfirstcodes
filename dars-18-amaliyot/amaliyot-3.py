#Yuqoridagi ikki dasturni jamlaymiz. Foydalanuvchi buyurtmasi ro'yxatidagi
# har bir mahsulotni e-bozordagi mahsulotlar bilan solishitiring (tayyor ro'yxat ishlatishingiz mumkin).
# Agar mahsuot e-bozorda mavjud bo'lsa mahuslot narhini chiqaring,
# aks holda "Bizda bu mahsulot yo'q" degan xabarni kor'sating.
# e_bozor mahsulotlari
e_bozor = {}
n = 1
ishora = True
while ishora:
    mahsulot = input(f"{n}-mahsulotingizni elektron do'konimizga kirting: ")
    narx = input("Mahsulot narxini kiriting: ")
    savol = input("Yana mahsulot qo'shishni istaysizni? (ha/yo'q)")
    savol=savol.strip()
    n+=1
    e_bozor[mahsulot]= narx
    if savol == "yo'q":
        ishora = False
# buyurtmani qabul qilish
buyurtmalar = []
a = 1
ishora_1 = True
while ishora_1:
    buyurtma = input(f"{a}-buyurtmangizni yozing: ")
    a+=1
    savol_1 = input("Yana buyurtma qilasizmi? (ha/yo'q): ")
    savol_1 = savol_1.strip()
    buyurtmalar.append(buyurtma)
    if savol_1 == "yo'q":
        ishora_1 = False

# Buyurtma va e_bozor mahsulotlarni solishtiramiz.
e_bozor_mahsulotlari = e_bozor.keys()
e_bozor_narxlari = e_bozor.values()
for mahsulot_z in buyurtmalar:
    if mahsulot_z in e_bozor_mahsulotlari:
        print(f"{mahsulot_z.title()}ning narxi: {e_bozor[mahsulot_z]}")
    else:
        print("Uzur, Bizda bunday mahsulot yo'q.")

