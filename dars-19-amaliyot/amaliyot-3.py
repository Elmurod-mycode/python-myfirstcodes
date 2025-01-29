# Foydalanuvchidan son olib, son juft yoki toqligini konsolga chiqaruvchi funksiya yozing.
def soni_turini_aniqla(son):
    """Sonning juft yoki toq son ekanini aniqlavchi funksiya."""
    if son%2==0:
        print(f"Siz kiritgan son juft son")
    else:
        print("Siz kiritgan son toq son.")
soni_turini_aniqla(22)