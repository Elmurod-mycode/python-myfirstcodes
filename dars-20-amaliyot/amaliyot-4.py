# Foydalanuvchidan aylaning radiusini qabul qilib olib,
# uning radiusini, diametrini, perimetri va
# yuzini lug'at ko'rinishida qaytaruvchi funksiya yozing

def aylana_info(radius):
    """Aylananing radiusi orqali uning diametri , perimetri va yuzini
     hisoblovchi funksiya."""
    diametr = radius*2
    pi = 3.14159
    aylana_uzunligi = 2*pi*radius
    yuzi = pi*(radius**2)

    aylana_params= { 'radius': radius,
                     'diametr': radius,
                     'perimetr': aylana_uzunligi,
                     'yuzi': yuzi
                     }
    return aylana_params
aylana = aylana_info(12)
print(aylana)