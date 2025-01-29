# 1/29/2025
# Muallif: Elmurod O'rinboyev
## 19-DARS. FUNKSIYA
## FUNKSIYA NIMA?
# Funksiya ma'lum bir vazifani bajarishga mo'ljallangan kodlar yig'indisi.
# Biz shu paytgacha bir cheta tayyor funksiyalardan foydalanib keldik.
# Misol uchun print() funksiyasi konsolga matn chiqarish uchun, range()
# funksiyasi esa ma'lum oraliqdagi sonlarni yaratish uchun ishlatiladi.
# FUNKSIYA YARATAMIZ
# def salom_ber():
#     """Salom beruvchi funksiya"""
#     print("Assalomu alaykum!")
# salom_ber()

# FUNKSIYAGA QIYMAT UZATISH
def salom_ber(ism):
    """"Foydallanuvchi ismini qabul qilib, unga salom beruvchi funksiya."""
    print(f"Assalomu alaykum, hurmatli {ism.title()}!")
salom_ber('ali')
# DOCSTRING
# bu uning qanday ishlashi haqida qisqacha ma'lumot chiqaradi.
# Masalan:
print(salom_ber.__doc__)

# ARGUMENT VA PARAMETER
# Funksiya yaratishda, qavs ichida berilgam, funksiya to'g'ri ishlashi uchun
# uzatiladigan qiymat parametr deb ataladi.
# Yuqoridagi misolda ism bu salom_ber funksiyasining parametri.

# Foydalanuvchi funksiyaga murojat qilishida funksiyaga uzatgan qiymat esa argument deb ataladi.
# salom_ber('ali') kodida 'ali' bu argument


# FUNKSIYAGA BIR NECHTA ARGUMENT UZATISH
# def toliq_ism(ism, familiya):
#     """Foydalanuvchi ismi va familiyasini jamlab chiqaruvchi funksiya."""
#     print(f"Foydalanuvchining ismi: {ism.title()}\n"
#           f"Foydalanuvchining familiyasi: {familiya.title()}")
# toliq_ism('ali', 'valliyev')
#
# def yosh_hisobla(ism, t_yil):
#     """Foydalanuvchini avval ismini aniqlab,
#      keyin yoshini hisoblab beruvchi funksiya."""
#     print(f"{ism.title()} {2025-t_yil} yoshda")
# yosh_hisobla('ali', 2003)
#
# # Kalit so'z bilan uzatish
# yosh_hisobla(t_yil=2004, ism='vali')
# SANDART QIYMAT
def yosh_hisobla(tugilgan_yil, joriy_yil=2025): # joriy yil uchun st.qiymat 2025
    """Foydalanuvchi tug'ilgan yilidan uni yoshini aniqlash"""
    print(f"Siz {joriy_yil-tugilgan_yil} yoshdasiz.")
yosh_hisobla(2006)