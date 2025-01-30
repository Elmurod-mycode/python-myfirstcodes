# Foydalanuvchidan son qabul qilib, shu son miqdoricha Fibonachchi ketma-ketligidagi
# sonlar ro'yxatni qaytaruvchi funksiya yozing. Ta’rif: Har bir hadi o’zidan oldingi
# ikkita hadning yig’indisiga teng bo’lgan ketma-ketlik
# Fibonachchi ketma-ketligi deyiladi.
# Bunda boshlang’ish had ko’pincha 1 deb olinadi. 1, 1, 2, 3, 5, 8, 13, 21, 34, 55,...

def fibonachshi(son):
    """Fibonachchi ketma-ketligi funksiyasi."""
    sonlar=[]
    for a in range(son):
        if a == 0 or a==1:
            sonlar.append(1)
        else:
            sonlar.append(sonlar[a-1]+sonlar[a-2])
    return sonlar
print(fibonachshi(10))
