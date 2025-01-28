#Adabiyot (ilm-fan, san'at, internet) olamidagi
# 4 ta mashxur shaxlar haqidagi ma'lumotlarni lug'at ko'rinishida saqlang.
# Lug'atlarni bitta ro'yxatga joylang, va har bir shaxs haqidagi ma'lumotni konsolga chiqaring.

mashxur_sh_1 = {'ism': 'elon',
                'familiya': 'Musk',
                'tyil': 1971,
                'davlat': 'aqsh',
                'kasbi':['tadbirkor', 'muhandis', 'ixtirochi', 'investor']
                    }
mashxur_sh_2 = {'ism': 'mark',
                'familiya': 'zuckerberg',
                'tyil':1984,
                'davlat': 'aqsh',
                'kasbi': ['dasturchi', 'tadbirkor', 'meta-texnologiya rahbari']
                }
mashxur_sh_3 = {'ism': 'adel',
                'familiya': 'adkins',
                'tyil': 1988,
                'davlat': 'angiliya',
                'kasbi': ["qo'shiqchi"]
    }
mashxur_sh_4 = {'ism':'cristiano ranaldo',
                'familiya': 'Aveiro',
                'tyil': 1985,
                'davlat': 'portugaliya',
                'kasbi': ['futbolchi']
                }
mashxur_shaxslar = [mashxur_sh_1,mashxur_sh_2,mashxur_sh_3,mashxur_sh_4]

for mashxur_sh in mashxur_shaxslar:
    print(f"\n{mashxur_sh['ism'].title()} {mashxur_sh['familiya'].title()}, "
          f"{mashxur_sh['tyil']}-yilda {mashxur_sh['davlat']}da tug'ilgan."
          f"Kasbi: ")
    for a in mashxur_sh['kasbi']:
        print(a)