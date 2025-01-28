# Muzeyga chipta narhi foydalanuvchining yoshiga bog'liq: 7 dan yoshlarga - 2000 so'm,
# 7-18 gacha 3000 so'm, 18-65 gacha 10000 so'm, 65 dan kattalarga bepul.
# Shunday while tsikl yozingki, dastur foydalanuvchi yoshini so'rasin va chipta narhini chiqarsin.
# Foydalanuvchi exit yoki quit deb yozganda dastur to'xtasin (ikkita shartni ham tekshiring).
# • Yuqoridagi dasturni turli usullarda yozib ko'ring (break, ishora, yoki shart tekshirish)
# 1-variant
print("Chipta sotuvchi dastur. ")
savol = "Yoshingizni kiriting "
savol += "(dasturdan chiqmoqchi bo'lsangiz 'exit' yoki 'quit' deb yozing): \n>>>>>"
yosh = ''
while yosh != 'exit' :
    yosh = input(savol)
    if yosh == 'exit' or yosh=='quit':
        break
    yosh = int(yosh)
    if yosh < 7 :
        print(f"Sizning yoshingiz {yosh} da ekan. Sizning chiptangizni narxi 2 000 so'm.")
    elif yosh <=18:
        print(f"Sizning yoshiniz {yosh} da ekan. Sizning chiptangizni narxi 3 000 so'm.")
    elif yosh <=65:
        print(f"Sizning yoshiniz {yosh} da ekan. Sizning chiptangizni narxi 10 000 so'm.")
    elif yosh <65:
        print(f"Sizning yoshingiz {yosh} da ekan. Sizga chipta bepul.")

# 2-variant
savol = 'Yoshingizni kiriting (\'exit\' yoki \'quit\' ni kiritsangiz dastur to\'xtaydi.)\n>>>'
ishora = True
while ishora:
    yosh = input(savol)
    if yosh == 'exit' or yosh=='quit':
        ishora = False
    else:
        yosh = int(yosh)
        if yosh < 7 :
            print(f"Sizning yoshingiz {yosh} da ekan. Sizning chiptangizni narxi 2 000 so'm.")
        elif yosh <=18:
            print(f"Sizning yoshiniz {yosh} da ekan. Sizning chiptangizni narxi 3 000 so'm.")
        elif yosh <=65:
            print(f"Sizning yoshiniz {yosh} da ekan. Sizning chiptangizni narxi 10 000 so'm.")
        elif yosh <65:
            print(f"Sizning yoshingiz {yosh} da ekan. Sizga chipta bepul.")
