## 1/30/2025
## Muallif: Elmurod O'rinboyev
## 21-DARS. FUNKSIYA VA RO'YXAT
# FUNKSIYAGA RO'YXAT UZATISH

# Avvalgi kodlarda funksiyaga parametr sifatida yagona qiymat berayotga edik.
# Aslida, bu bilan cheklanmasdan, funksiyaga ro'yxat(list) ham berish mumkin.
# Bunda, funksiya ro'yxat qiymatlariga to'g'ridan-to'g'ri murojat qila olmaydi.

# Keling talabalarni baholaydigan funksiya yozamiz. Funksiyamiz talabalar
# ro'yxatini qabul qilib oladi, ro'yxatdan har bir talabani sug'irib olib . pop(),
# bahosini kiritishini so'raydi. Talaba ismi va bahosini lug'at joylab, yakuniy
# lug'atni foydalanuvchiga qaytaradi.
def bahola(ismlar):
    baholar = {}
    while ismlar:
        ism = ismlar.pop()
        baho = input(f"Talaba {ism.title()}ning bahosini kiriting: ")
        baholar[ism] = baho
    return baholar
talabalar = ['ali', 'vali', 'fontima', 'zuhro']
# baholar = bahola(talabalar)
# print(baholar)

# bunda e'tibor beradigan narsamiz talabalar[] ro'yxati bo'lib biz yaratgan funksiya
# ushbu ro'yxatdan to'g'ridan to'g'ri foydalanadi va .pop() orqali harbir elementni sug'irib olishimiz natijasida
# talabalar[] ro'yxati bosh bo'lib qoladi.
print(talabalar)

# buni oldini olish uchun nima qilish kerak chunki ro'yxatda keyinchalik ham foydalanishimiz ham mumkin
# buning uchun ro'yxatda kopiya olimiz bu oddiygina shu tartibda bo'ladi:
baholar = bahola(talabalar[:])
print(baholar)
print(talabalar)
# yani bu yerda oddiy [:] dan foydalandik u asl ro'yxatda nusxa olishga yordam beradi.
