# Darsimiz davomida yozgan bahola funksiyasini
# .pop() metodidan foydalanmasdan va asl
# ro'yxatga o'zgartirish kiritmasdan
# faqat lug'at qaytaradigan qilib yozing.

def bahola(royxat):
    """Talabalarga baho qoyuvchi funksiya."""
    talabalar = {}
    for x in royxat:
        talabalar[x] = int(input(f"{x.title()}ning bahosini kiriting: "))
    return talabalar

talabalar = ['ali', 'vali', 'gani', 'sattor']
baholar = bahola(talabalar)
print(baholar)
