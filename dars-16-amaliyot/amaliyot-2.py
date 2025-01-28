#Yuqoridagi lug'atlarga har bir shaxsning mashxur asarlari ro'yxatini ham qo'shing.
# For tsikli yordamida muallifning ismi va uning asarlarini konsolga chiqaring.
buxoriy = {'ism':'Abu Abdulloh Muhammad ibn Ismoil',
           'tyil':810,
           'vyil':870,
           'tjoy':'Buxoro',
           'asar': ['Al-Jome as-Sahih']
           }

qodiriy = {'ism':'Abdulla Qodiriy',
           'tyil':1894,
           'vyil':1938,
           'tjoy':'Toshkent',
           'asar': ["O‘tkan kunlar', 'Mehrobdan chayon"]
           }

vohidov = {'ism':'Erkin Vohidov',
           'tyil':1936,
           'vyil':2016,
           'tjoy':"Farg'ona",
           'asar' : ['Tong nafasi', 'Qo‘shiqlarim sizga', 'Ruxsor']
           }

navoiy = {'ism':'Alisher Navoiy',
           'tyil':1441,
           'vyil':1501,
           'tjoy':"Xirot",
           'asar': ['Xamsa', 'Layli va Majnun', 'Farhod va Shirin', 'Sab’ai Sayyor']
           }

shaxslar = [buxoriy, qodiriy, vohidov, navoiy]

for shaxs in shaxslar:
    print(f"\n{shaxs['ism'].title()}ning mashxur asarlari: ")
    for asar in shaxs['asar']:
        print(asar)
