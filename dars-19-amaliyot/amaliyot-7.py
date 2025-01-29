# Foydalanuvchidan son qabul qilib, sonni 2 dan 10 gacha bo'lgan sonlarga qoldiqsiz
# bo'linishini tekshiruvchi funksiya yozing.
# Natijalarni konsolga chiqaring.

def qoldiqsiz_bolin(son):
    """Foydalanuvchidan ixtiyoriy son olib  2 dan 10 gacha bo'lgan sonlarga qoldiqsiz
    bo'linishini tekshiruvchi funksiya."""
    for a in range(2,11):
        if son%a==0:
            print(f"{son} soni {a}ga qoldiqsiz bo'linadi.")

qoldiqsiz_bolin(15)