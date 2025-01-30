# Foydanaluvchidan ismi, familiyasi, tug'ilgan yili, tug'ilgan joyi, email manzili va
# telefon raqamini qabul qilib, lug'at ko'rinishida qaytaruvchi funksiya yozing.
# Lug'atda foydalanuvchu yoshi ham bo'lsin.
# Ba'zi argumentlarni kiritishni ixtiyoriy qiling (masalan, tel.raqam, el.manzil)

def foydalanuvchi_info(ism, familiya, yoshi, t_joyi, email='',tel_n='' ):
    """"Foydalanuvchi haqida ma'lumot kirituvdchi fuksiya"""
    foydalanuvchi = {'ism': ism,
                     'familiya': familiya,
                     "yoshi": yoshi,
                     "t_joy": t_joyi,
                     'email': email,
                     'tel_n': tel_n
    }
    return foydalanuvchi
while True:
    ism = input("Ismingizni kiriting: ")
    familiya = input("Familiyangizni kiriting: ")
    yosh = input("Yoshingizni kiriting: ")
    t_joy = input("Tug'ilgan hududingizni kiriting: ")
    email = input("Email manzilingizni kiriting: ")
    tel_n = input("Telefon raqamingizni kiriting: ")
    foydalanuvchi = foydalanuvchi_info(ism, familiya, yosh, t_joy, email, tel_n)
    savol = input("Agar ma'lumotingizni to'g'ri kitigan bo'lsangiz so'rovni tugatamizmi? (yes/no): ")
    if savol == 'yes':
        break
print(foydalanuvchi)
