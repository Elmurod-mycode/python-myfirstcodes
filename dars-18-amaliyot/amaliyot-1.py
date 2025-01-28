#Foydalanuvchidan buyurtma qabul qiluvchi dastur yozing.
# Mahsulotlar nomini birma-bir qabul qilib, yangi ro'yxatga joylang.

print("Foydalanuvchidan buyurtma qabul qiluvchi dastur.")
buyurtmalar = []
n=1
ishora = True
while ishora:
    taom = input(f"{n}-buyurtmangizni ayting: ")
    javob = input("Yana buyurtma qilaszmi?(ha/yo'q)")
    buyurtmalar.append(taom)
    if javob == "yo'q":
        break
    else:
        n+=1
print(f"Sizning burtmalaringiz:")
for burtma in buyurtmalar:
    print(burtma)