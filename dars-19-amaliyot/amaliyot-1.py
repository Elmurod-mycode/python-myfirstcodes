#Foydalanuvchi ismi va yoshini so'rab, uning tug'ilgan yilini hisoblaydigan funksiya yozing.
def yoshini_hisobla(ism, t_yil):
    """Foydalanuvchi ismi va yoshini hisoblav aniqlab  beruvchi funksiya."""
    print(f"Foydalanuvchi ismi: {ism.title()}\n"
          f"Foydalanuvchining yoshi: {2025-t_yil} da")
yoshini_hisobla('akbar', 2009)