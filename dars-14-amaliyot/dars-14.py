# 14-dars. Lug'at bilan tanishuv
# 1/27/2025
# Mualif: O'rinboyev Elmurod

# 14.1 Lug'at bilan ishlash
car_0 = {'model':'cobalt',
         'color':'white',
         'year':'2020',
         'weight':"1 200 t"}
print(car_0['model'])
print(f"Men kecha {car_0['model']} sotib oldim.\n"
      f"Uning rangi {car_0['color']}.\n"
      f"Yili esa {car_0['year']} ekan.\n"
      f"Og'irligi-{car_0['weight']}"
      )

# 14.2 Yangi juftlik qo'shish
car_0['ishlab chiqaruvchi'] = 'GM'
car_0['mator'] = '1.6 l'
print(car_0)

# 14.3 Bo'sh lug'at
talaba_0 = {}
talaba_0['ism'] = 'Ohunjoniva Nasiba'
talaba_0['kurs'] = 1
talaba_0['yili'] = 2005
talaba_0['manzili'] = "Abu-Dabi"
print(talaba_0)

# 14.4 Kalit so'z-qiymat juftligini o'chirish
davlat_0 = {"nomi":'Uzbekistan','maydoni': 448.978,'aholisi' : 37_000_000,'viloyatlar': 12,'tumanlar': 208}
print(davlat_0)
del davlat_0['aholisi']
del davlat_0['tumanlar']
print(davlat_0)

# 14.5 Lug'atni qatorlarga bo'lib yozish

davlat_0 = {"nomi":'Uzbekistan',
            'maydoni': 448.978,
            'aholisi' : 37_000_000,
            'viloyatlar': 12,
            'tumanlar': 208}

# 14.6 .get() metodi

davlat_poytaxtlari = {"O'zbekiston" : "Toshkent",
                      'AQSh' : 'Washington',
                      'Xitoy' : 'Pekin',
                      'Janubiy Koreya' : 'Seul',
                      'Hindiston' : 'Dehli'
                      }
davlat = davlat_poytaxtlari.get("Rossiya", "Bunday ma'lumot mavjud emas.")
print(davlat)
davlat = davlat_poytaxtlari.get("Rossiya")
print(davlat)
