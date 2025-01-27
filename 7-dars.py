# List (ro'yxat) bilan tanishamiz
daryolar = ["Nil", "Amazanka", "Amudaryo", "Sirdaryo"]
daryolar.append("Dnepir")
daryolar.append("Chirchiq")
print(daryolar[2].upper())
print(daryolar[3].lower())
print(daryolar[1].title())
print(daryolar)


cars = []
cars.append("Lacetti")
cars.append("Nexia")
cars.append("Tracker")
cars.append("Maliba")
print(cars)
cars.insert(0, "Lada")
cars.insert(2,"Bugatti")
print(cars)
del cars[1]
print(cars)
del cars[-1]
print(cars)
regions = ["Toshkent", "Sirdaryo","Toshkent", "Samarqand", "Buxoro", "Qoraqalbog\'iston Respublikasi"]
regions.remove("Toshkent")
print(regions)

yovvoyi_hayvonlar = ["sher", "buybul", "zebra", "tuyaqush", "yo'lbars", "sirtlon"]
hayvonlar_qiroli = yovvoyi_hayvonlar.pop(0)
yovvoyi_hayvonlar[0] = "dinazavor"
print(yovvoyi_hayvonlar)
print(f"Yovvoyi hayvonlar qiroli {hayvonlar_qiroli}")



# A(maliyot
# 1
ism = []
ism.append("Sunnat")
ism.append("Javohir")
ism.append("Avaz")
ism.append("Sherzot")
print(ism)
print(f"Salom {ism[1]} dostim bugun Dubayga uchamizmi?")
print(f"{ism[0]} qaleysan")
print(f"{ism[2]} bugun yerni o'z o'qidan chiqarib yuboramizmi?:)")
print(f"{ism[3]} Salom, damlar qaaaandey  bo'votiii?")



numbers = []
numbers.append(12)
numbers.append(-45)
numbers.append(77)
numbers.append(99.2)
numbers[0] = numbers[0]*12
print(numbers)


t_shaxslar = []
t_shaxslar.insert(0, "Al-Xorazmiy")
t_shaxslar.append("Beruniy")
t_shaxslar.insert(2, "Aristotel")
z_shaxslar = []
z_shaxslar.insert(0, "Ilon Musk")
z_shaxslar.insert(2, "Jamshidxon Ziyoxonov")
z_shaxslar.insert(-1, "Abdulloh domla")
z_shaxslar.insert(-1, "GGG")

print(z_shaxslar)
print(t_shaxslar)

print(f"Men tarixiy shaxslardan {t_shaxslar[0]} bilan suhbatlashishni hohlar edim")
print(f"Men zamonaviy shaxslardan {z_shaxslar[1]} bilan birga iftorlik qilishi hohlar edim")

friends = []
friends.append("Jons")
friends.append("Ali")
friends.append("Vali")
friends.append("Harry")
friends.append("Diyor")
friends.remove("Diyor")
friends.remove("Jons")
friends.insert(0, "Malik")
friends.insert(2, "Charli")
friends.insert(-1, "Henry")


print(friends)





















