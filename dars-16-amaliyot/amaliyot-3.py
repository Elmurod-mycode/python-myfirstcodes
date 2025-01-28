# Oila a'zolaringiz (do'stlaringiz) dan 3 ta sevimli kino-seriali haqida so'rang.
# Do'stingiz ismi kalit, uning sevimli kinolarini esa ro'yxat ko'rinishida lug'artga saqlang.
# Natijani konsolga chiqaring.

dostlarim = {
    'anvar':['Avatar', 'Titanik', 'Dengiz qaroqchilari', 'Rabunzel va uning po\'lat qilichi'],
    'sadulla': ['Farsaj 7', 'Astral', 'Havli burilish', 'Osmondagi bollar'],
    'botir': ['Ekskalibur', 'Taxtlar o\'yini', 'Ajdar uyi', 'Lusiy','Ota mehri']
     }
for dostim, sevimli_kinolari in dostlarim.items():
    print(f"\n{dostim.title()}ning yoqtirgan kinolari: ")
    for kino in sevimli_kinolari:
        print(kino)