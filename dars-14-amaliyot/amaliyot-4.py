# Foydalanuvchidan biror so'z kiritishni so'rang va
# so'zning tarjimasini yuqoridagi lug'atdan chiqarib bering.
# Agar so'z lu'gatda mavjud bo'lmasa,
# "Bunda so'z mavjud emas" degan xabarni chiqaring.

en_uz = {'apple': 'olma',
         'bottom': 'pastki qism',
         'agree':'rozi bo\'lmoq',
         'alone':'o\'zga sayyoralik',
         'smell': 'hidlamoq',
         'goal': 'maqsad'}
soz = input("Ixtiyoriy so'z kiriting: ").lower()
soz = en_uz.get(soz, "Bunday so'z mavjud emas.")
print(soz)

