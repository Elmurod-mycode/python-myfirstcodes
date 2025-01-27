# 1/27/2025
# Muallif: Elmurod O'rinboyev

# 15-dars. Lug'at elementlari bilan ishlash.


# 15.1 .item() metodi
dostim = {
    'ism': 'Anvar',
    'familiya' : 'Tursonov',
    'yosh' : 22
    }
print(dostim.items())
# tsikl orqali tushunarli chiqarish
for kalit, qiymat in dostim.items():
    print(f"Kalit: {kalit}")
    print(f"Qiymat: {qiymat}\n")

# tsikl orqali tushunarli va chiroyli qiliig f"{}" orqali ham ikkita o'zgaruvchi kiritib ishlatsak ham bo'ladi.
telefonlar = {
    'ali':'iphone x',
    'vali':'galaxy s9',
    'olim':'mi 10 pro',
    'orif':'nokia 3310'
    }
for kalit , qiymat in telefonlar.items():
    print(f"{kalit.title()}nint telefoni {qiymat}.")

# 15.2 .keys() metodi
# Agar lug'atdagi kalit so'zlarni ko'rish talab qilinsa, .keys() metodidan foydallanishimiz mumkin.
mahsulotlar = { # Do'kondagi mahsulotlar
    'olma':10000,
    'anor':20000,
    'uzum':40000,
    'anjir':25000,
    'shaftoli':30000
    }
print(mahsulotlar.keys())
print("Do'kondagi mahsulotlar:")
for m in mahsulotlar.keys():
    print(m.title())

# Yuqoridagi kodimizda, for tsiklida .keys() metodini ishlatmasak ham huddi shu natija chiqadi.
bozorlik = ['olma', 'uzum', 'anor', 'non']
for mahsulot in mahsulotlar:
    if mahsulot in bozorlik:
        print(f"{mahsulot.title()} {mahsulotlar[mahsulot]} so'm")
for buyum in bozorlik:
    if buyum not in mahsulotlar:
        print(f"Iltimos, do'koningizga {buyum} ham olib keling.")

# 15.3 Lug'at elementlarini tartib bilan chiqarish
print("Do'konimizdagi mahsulotlar: ")
for mahsulot in sorted(mahsulotlar):
    print(mahsulot.title())

# 15.4 .values() metodi
# Agar lug'atdagi qiymatlarni chiqarish talab qilinsa .values() metodidan foydalanishim mumkin.
print(telefonlar.values())
print("Foydalanuvchilar quyidagi telefonlarni ishlatishadi:")
for tel in telefonlar.values():
    print(tel)

# Yuqoridagi metodda bitta kamchilik bolib bir hil qiymatlilarn ham chiqarishi mumkin bu bir muncha noqulayliklar keltiradi
telefonlar = {
    'ali':'iphone x',
    'vali':'galaxy s9',
    'olim':'mi 10 pro',
    'orif':'nokia 3310',
    'hamida':'galaxy s9',
    'maryam':'huawei p30',
    'tohir':'iphone x',
    'umar':'iphone x'
    }

print('Foydalanuvchilar quyidagi telefonlarni ishlatishadi:')
for tel in telefonlar.values():
    print(tel)
# Buning uchun set() funktsiyasidan foydalanishimiz mumkin.
print('Foydalanuvchilar quyidagi telefonlarni ishlatishadi:')
for tel in set(telefonlar.values()):
    print(tel)

# Pythonda set yana vir ma'lumot turi bo'lib, ro'yaxt va lug'at kabibir nechta
# elementlarni saqlashga mo'ljallangan. Lug'at va ro'yxatda farqli ravishda,
# set ichidagi elementlar birior tartibda saqlanmaydi, va ularga indeks
# orqali murojat qilib bo'lmaydi. Shuningdek, set ichida bir hil elementlar bo'lmaydi.
