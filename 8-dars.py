# List bilan ish
davlatlar = ["O'zbekiston", "Indiya", "Malaziya", "Qirg'iziston", "Eron", "AQSh", "Britaniya" ]
davlatlar.sort()
print(davlatlar)
shakl = ["tortburchat", "uchburchak", "aylana", "konus", "Slindir"]
shakl.sort(reverse=True)
print(shakl)
# .sorte() medodidan foydalansak u to'g'ridan to'g'ri
# o'zgaruvchiga ta'sir qilib list ichidagi elementlar
# joylashuviga tasir qiladi
bino = ["Minevartour", "Trilard", "Nestone", "Akaysity"]
Bino1 = sorted(bino)
print(Bino1)
bino.reverse()
print(bino)
len(bino)
print(len(bino))

sonlar = list(range(0,11))
print(sonlar)
juft_sonlar = list(range(0,20,2))
print(juft_sonlar)
toq_sonlar = list(range(1, 20,2))
print(toq_sonlar)

narxlar = [2455, 54658, 5466365, 466426, 455,6654]
arzon = min(narxlar)
qimmat = max(narxlar)
jami = sum(narxlar)
print(f"aqzon:{arzon},\nqimmat: {qimmat},\nJammi summa: {jami}")

daraxtlar = ["Chinor", "Qarag'ay", "Terak", "Qayin", "Archa", "Saksavol", "Olcha"]
mening_daraxtlarim = daraxtlar[2:5]# orsidagi elementlarni kesadi
print(mening_daraxtlarim)
qoshnimning_daraxtlari = daraxtlar[:3] # 3 gacha bo'lagan elementlarni kesadi
print(qoshnimning_daraxtlari)
davlatni_daraxtalari = daraxtlar[2:]
print(davlatni_daraxtalari)
tabiatni_daraxtlari = daraxtlar[:]
print(tabiatni_daraxtlari)
meva= ["olma", "olcha", "o'rik", "gilos", "behi", "anjir"]
meva1 = meva
meva1.append("shaftoli")
print(meva1)
print(meva)# Bunday nusxalashda dastlabki listdagi elementlar tarkibi o'zgarib ketadi
# shuning uchun bunday tartibda qilish kerek
meva= ["olma", "olcha", "o'rik", "gilos", "behi", "anjir"]
meva1  = meva[:]
meva1.append("uzum")
print(meva1)
print(meva)


### TUPLES - o'zgarmas ro'yxat
tomonlar = (12, 45, 45)
tomonlar[1]
print(tomonlar[1])
tomonlar = list(tomonlar)
print(tomonlar)
tomonlar.append(112)
print(tomonlar)
tomonlar = tuple(tomonlar)
print(tomonlar)



### Amaliy Mashg'ulot

davlatlar = ["Ukrayina", "Rossiya", "Belarusiya", "Amerika", "Belgiya", "Ispaniya"]
print(davlatlar)

print(len(davlatlar))
dav = sorted(davlatlar)
print(dav)
print(sorted(davlatlar, reverse=True))
print(davlatlar)
davlatlar.reverse()
print(davlatlar)
davlatlar.sort()
print(davlatlar)
juft_sonlar = list(range(120,1200,2))
summa = sum(juft_sonlar)
print(juft_sonlar)
print(summa)
kichik = min(juft_sonlar)
katta = max(juft_sonlar)
ayirma = katta - kichik
print(ayirma)
print(len(juft_sonlar))
print(juft_sonlar[0:21])
print(len(juft_sonlar[270:290]))
print(len(juft_sonlar[520:540]))
j_s = list(range(0,15,2))
print(j_s)
print(j_s[1:3])
print(len(j_s))
taomlar = ["osh", "dimlama", "manti", "kabob", "ko'zasho'rva"]
nonushta = taomlar[:2]
nonushta.append("blinchik")
nonushta.append("kasha")
print(nonushta)
print(taomlar)
nonushta = tuple(nonushta)
print(nonushta)
nonushta[0] = "non"
print(nonushta)



