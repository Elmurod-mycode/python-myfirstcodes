sinfdoshlar = ["Ali", "Vali", "Malika", "Zarina"]
for mehmon in sinfdoshlar:
    print(f"Salom, {mehmon}")
    print("Hushko'rdik!")
print(sinfdoshlar)

sonlar = list(range(1, 11))
kvadrat = []
for son in sonlar:
    kvadrat.append(son**2)
print(sonlar)
print(kvadrat)

# dostlar = []
# print("4 ta eng yaqin do'stingiz kim?")
# for n in range(5):
#     dostlar.append(input(f"{n+1}-dostinizning ismini kiriting: "))
# print(dostlar)




### Amaliy mashg'ulot
ism = ["Malika", "Umida", "Ali", "Vali", "Bilmasvoy"]
for n in ism:
    print(f"Salom, {n}")
print(f"kod {len(ism)} marta takrorlandi")

toq_sonlar = list(range(1,100,2))
print(toq_sonlar)
for n in toq_sonlar:
    print(f"{n} sonning kubi{n**3} ga teng")
sevimli_kino = []
for n in range(5):
    sevimli_kino.append(input(f"{n+1}-sevimli kinoyingiz nomini kiriting: "))
print(sevimli_kino)

suhbatlashgan_odamlar = []
ularning_soni = int(input("Nechta odam bilan bugun suhbatlashdingiz"))
for n in range(ularning_soni):
    suhbatlashgan_odamlar.append(input(f"{n+1} suhbatlashgan odamning usmini kiriting: "))
print(suhbatlashgan_odamlar)