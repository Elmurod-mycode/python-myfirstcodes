# Bugun o'rgangan narsalaringizni matnga yozing va matnni Python yordamida oching
# Quyidagi pi_million_digits.txt faylini yuklab oling (faylda π soni nuqtadan so'ng million xona aniqlik bilan yozilgan).
# Sizning tug'ilgan kuningiz π soni tarkibida uchraydimi yoki yo'q ekanligini aniqlovchi funksiya yozing.
# Misol uchun, tug'ilgan sanangiz 25 Fevral, 2000-yil bo'lsa, 25022000 ketma-ketligi yuqoridagi matnda uchraydimi yo'q toping.
# Fayl ichidagi matnni float ma'lumot turiga o'tkazing va pickle yordamida yangi faylga saqlang.
# Foydalanuvchidan turli hil ma'lumotlarni so'rab, har bir kiritilgan ma'lumotni yangi qatordan faylga yozib boruvchi dastur tuzing.
# Dastur qayta chaqirilganida yangi ma'lumotlar fayl oxiridan qo'shilib borsin (yangi faylga emas).

with open('pi_million_digits.txt') as file:
    pi = file.read()
## bunda .txt fayl ichidagi ma'lumot matn ko'rinishida bo'lib u son bo'lsa ham endi uni matndan songa o'tkazishni ko'raylik
pi = pi.rstrip() # qator ohiridagi bo'shliqlarni olib tashlaymiz.
pi = pi.replace('\n', '') # qator tashlash belgisini alamashtiramiz
pi = pi.replace(' ', '') # qator orasidagi bo'shliqni olib tashlaydi

def tugilgan_kun(sana):
    if sana in str(pi):
        print("bor")
    else:
        print("Yo'q")
print(tugilgan_kun('02082001'))

# ism = input("Ismingizni kiriting: \n>>>")
# familiya = input("Familiyangizni kiriting: \n>>>")
# t_yil = input("Tug'ilgan yilingizni kiriting: \n>>>")
def malumot_kirit():
    with open('info_user', 'a+') as file:
        while True:
            malumot = input("Ma'lumot kiriting (yoki 'exit' deb yozib chiqib keting): ")
            if malumot.lower() == 'exit':
                print("Ma'lmotlar faylga yozildi.")
                break
            file.write(malumot + '\n')
malumot_kirit()