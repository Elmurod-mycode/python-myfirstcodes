## Talabalar haqidagi ma'lumotlarini lug'at ko'rinishida qaytaruvchi funkisya yozing.
# Talabaning ismi va familiyasi majburiy argument, qolgan ma'lumotlar esa
# ixtiyoriy ko'rinishda istalgancha berilishi mumkin bo'lsin.

def talaba_info(ism, familiya, **malumotlar):
    """Talabadan istalgancha ma'lumot oladigan funksiya."""
    malumotlar['ism'] = ism
    malumotlar['familiya'] = familiya
    return malumotlar
print(talaba_info('ali', 'valiyev', yoshi=21, manzili='toshkent', t_yil=2004))