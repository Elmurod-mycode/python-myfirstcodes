# Yuqoridagi funksiyani while yordamida bir necha bor chaqiring,
# va mijozlar degan ro'yxatni shakllantiring.
# Ro'yxatdagi mijozlar haqidagi ma'lumotni konsolga chiqaring.


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
mijozlar = []
while True:
    ism = input("Ismingizni kiriting: ")
    familiya = input("Familiyangizni kiriting: ")
    yosh = input("Yoshingizni kiriting: ")
    t_joy = input("Tug'ilgan hududingizni kiriting: ")
    email = input("Email manzilingizni kiriting: ")
    tel_n = input("Telefon raqamingizni kiriting: ")
    mijozlar.append( foydalanuvchi_info(ism, familiya, yosh, t_joy, email, tel_n))
    savol = input("So'rovni tugatishni hohlaysizmi? (yes/no): ")
    if savol == 'yes':
        break
for mijoz in mijozlar:
    print(f"{mijoz['ism'].title()} {mijoz['familiya'].title()} {mijoz['yoshi']} yoshda."
          f"Telefon raqami: {mijoz['tel_n']}.")