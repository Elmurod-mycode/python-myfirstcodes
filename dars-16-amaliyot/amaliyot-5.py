# Yuqoridagi dasturga o'zgartirish kiriting: konsolga barcha davlatlarni emas,
# foydalanuvchi so'ragan davlat haqida ma'lumot bering.
# Agar davlat sizning lug'atingizda mavjud bo'lmasa,
# "Bizda bu davlat haqida ma'lumot yo'q" degan xabarni chiqaring.

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
davlat = input("Davlat nomini kiriting: ").lower()
if davlat in davlatlar:
    info = davlatlar[davlat]
    print(f"\n{davlat.capitalize()}ning putaxti {info['poytaxt'].title()}.\n"
          f"Maydoni: {info['maydon']} km2.\n"
          f"Aholi soni: {info['aholi']} ta.\n"
          f"Pul birligi: {info['pul birligi']}"
          f"Viloyatlar: "
          )
    for a in info['viloyatlar']:
        print(a)
else:
    print("Bizda bunday ma'lumot yo'q.")
