# Foydalanuvchidan ikkita son olib, ulardan kattasini konsolga chiqaruvchi funksiya yozing.
# Agar sonlar teng bo'lsa "Sonlar teng" degan xabarni chiqaring.

def maxNum(a, b):
    """Foydalanuvchidan ikkita son qabul qilib (a=12, b=13),
    ularni o'zaro taqqoslovchi funksiya."""
    if a<b:
        print(b)
    elif a>b:
        print(a)
    else:
        print("Teng qiymatli sonlar!")
maxNum(12,12)