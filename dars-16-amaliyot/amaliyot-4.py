#Davlatlar degan lug'at yarating, lug'at ichida bir nechta davlatlar haqida
# ma'lumotlarni lug'at ko'rinishida saqlang.
# Har bir davlat haqida ma'lumotni konsolga chiqaring.

davlatlar = {
    "o'zbekiston": {
        'poytaxt': "Toshkent",
        'maydon': 448978,
        'aholi': 33_000_000,
        'pul birligi': "so'm",
        'viloyatlar': ['Andijon', 'Buxoro', 'Farg‘ona', 'Xorazm', 'Samarqand']
    },
    "aqsh": {
        'poytaxt': "Vashington",
        'maydon': 9834000,
        'aholi': 331_000_000,
        'pul birligi': "dollar",
        'viloyatlar': ['Kaliforniya', 'Texas', 'Nyu-York', 'Florida', 'Illinois']
    },
    "rossiya": {
        'poytaxt': "Moskva",
        'maydon': 17098242,
        'aholi': 146_000_000,
        'pul birligi': "rubl",
        'viloyatlar': ['Moskva viloyati', 'Sankt-Peterburg', 'Tatariston', 'Bashqirdiston', 'Krasnodar']
    },
    "xitoy": {
        'poytaxt': "Pekin",
        'maydon': 9596961,
        'aholi': 1_400_000_000,
        'pul birligi': "yuan",
        'viloyatlar': ['Guangdong', 'Sichuan', 'Hunan', 'Jiangsu', 'Zhejiang']
    },
    "yaponiya": {
        'poytaxt': "Tokio",
        'maydon': 377975,
        'aholi': 126_000_000,
        'pul birligi': "yen",
        'viloyatlar': ['Hokkaydo', 'Aomori', 'Osaka', 'Kyoto', 'Kanagawa']
    }
}
for davlat, malumotlar in davlatlar.items():
    poytaxt = malumotlar['poytaxt']
    maydon = malumotlar['maydon']
    aholi = malumotlar['aholi']
    pul = malumotlar['pul birligi']
    viloyat = malumotlar['viloyatlar']
    print(f"\n{davlat.title()}ning poytaxti {poytaxt}. \nMaydoni: {maydon} km2.\n"
          f"Aholisi: {aholi} ta.\nPul birligi: {pul}. \n Viloyatlari: ")
    for vil in viloyat:
        print(vil)
    print('va h.')