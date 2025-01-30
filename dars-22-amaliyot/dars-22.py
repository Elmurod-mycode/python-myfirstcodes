## 1/30/2025
## Muallif: Elmurod O'rinboyev
## 22-DARS. MOSLASHUVCHAN FUNKSIYA(*args, **kwargs)

## Moshlashuvcah funksiya

# agar funksiyangiz bir nechta argument qabul qilishiingiz kerak bo'lsa-yu,
# lekin siz argumentlar sonini aniq bilmasangiz,
# Pythonda istalgancha qiymat qabul qiluvchi funksiya yaratish imkoniyati bor.

## *args USULI

# Agar funksiya qabul qiladigan parametrlar soni noaniq bo'lsa, va parametrlar yagona
# qiymatlar ko'rinishida uzatilsa, funksiya yaratishda argumentdan avval yulduzcha qo'yiladi(*arguments).
# Quyidagi misolni ko'raylik. summa() nomli funksiyamiz istalgancha sonlarni qabul qilib oladi
# va ularning yig'indisi hisoblaydi:

def summa(*sonlar):
    """Kiritilgan sonlar yig'indisini hisoblaydigan funksiya."""
    yigindi = 0
    for son in sonlar:
        yigindi+= son
    return yigindi
# Bu funksiyani istalgan parametr bilan chiqarish mumkin:
print(summa(12,12,24,4,24,2,42,2,42,34,535,3))

# *args usulida, barcha uzatilgan parapetrlar (bir dona bo'lsa ham) funksiya ichida o'zgarmas ro'yxatga (tuple) joylanadi.
# bundan kelib chiqib, yuqoridagi funksiyamizni yanada soddalashtirib yozishimiz mumkin:

# Agar funksiya bir nechta argument qabul qilsa, * args argument doim oxirida yoziladi:

def summa1(x,y,*sonlar):
    """Kiritilgan sonlar yig'indisini hisoblaydigan funksiya"""
    return (x+y+sum(sonlar))
print(summa1(1,2,12,124,134,123334))

### **kwargs USULI
# agar funksiyaga kelit so'z - qiymat ko'rinishidagi argumentlarni uzatish talab qilinsa,
# va bunday parametrlar soni noma'lum bo'lsa, argument oldidan ikkita yulduzcha qo'yiladi(**kwargs.)

##   | ** kwargs-keyword arguments (kalit so'zli argumentlar)

def avto_info(kompaniya, model, **malumotlar):
    """Avto haqidagi ma'lumotlarni lug'at ko'rinishidagi qaytaruvchi funksiya."""
    malumotlar['kompaniya'] = kompaniya
    malumotlar['model'] = model
    return malumotlar
avto1 = avto_info("GM", "malibu", rangi='qora', km = 12000, narxi=13000)
avto2 = avto_info("Kia", 'Soneto', rangi='oq', km=2000, narxi=40000, korobka='avto')
print(avto1)
print(avto2)