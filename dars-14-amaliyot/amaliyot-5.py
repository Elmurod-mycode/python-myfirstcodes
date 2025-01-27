# Foydalanuvchidan biror so'z kiritishni so'rang va
# so'zning tarjimasini yuqoridagi lug'atdan chiqarib bering.
# Agar so'z lu'gatda mavjud bo'lmasa,
# "Bunda so'z mavjud emas" degan xabarni chiqaring.
#################
# 4- vazifani endi.  if-else yordamida qiling va natijani ham foydalanuvchiga tushunarli ko'rinishda chiqaring.

en_uz = {'apple': 'olma',
         'bottom': 'pastki qism',
         'agree':'rozi bo\'lmoq',
         'alone':'o\'zga sayyoralik',
         'smell': 'hidlamoq',
         'goal': 'maqsad'}
soz = input("Ixtiyoriy so'z kiriting: ").lower()
natija = en_uz.get(soz)
if natija == None:
    print("Bunday so'z mavjud emas")
else:
    print(f"{soz.title()} so'zi {natija} deb tarjima qilinadi")
