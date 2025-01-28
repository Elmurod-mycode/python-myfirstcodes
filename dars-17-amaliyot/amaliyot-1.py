# Foydalanuvchidan yaxshi ko'rgan kitoblarini kiritishni so'rang.
# Foydalanuvchi stop so'zini yozishi bilan dasturni to'xtating
# 1-versiya
savol = "Yaxshi ko'rgan kitobingizni kiriting "
savol += "(agar ro'yxat tugagan bo'lsa 'stop' deb yozing): \n>>>>"
kitob = ''
while kitob != 'stop':
    kitob = input(savol)
    if kitob!='stop':
        print(kitob.upper())
## 2- versiya
savol = "Yaxshi ko'rgan kitobingizni kiriting "
savol += "(agar ro'yxat tugagan bo'lsa 'stop' deb yozing): \n>>>>"
qiymat = True
while qiymat:
    kitob = input(savol)
    if kitob == 'stop':
        break
    else:
        print(kitob.upper())
