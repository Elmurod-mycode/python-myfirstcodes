#Restoran menusi lug'atini tuzing (kamida 10 ta taom-narh juftligini kiriting).
# Foydalanuvchidan 3 ta ovqat buyurtma berishni so'rang.
# Foydalanuvchi kiritgan taomlarni menu bilan solishtiring,
# agar taom menuda bo'lsa narhini ko'rsating,
# aks holda "bizda bunday taom yo'q" degan xabarni chiqaring.
taomlar = {
    'osh' : 25000,
    'xonim' : 10000,
    'shashlik' : 12000,
    'katlet' : 18000,
    'bishteks' : 25000,
    'choy' : 5000,
    'non' : 5000,
    'achima-chuchu' : 5000,
    'shorva' : 3000
         }
zakaz = []
for t in range(3):
    zakaz.append(input(f"{t+1}-buyurtmangizni bering: ").lower()) # 3ta zakaz oldim
for taom in zakaz: # va harbirini royxat bo'yicha yurib chiqdim.
    if taom in taomlar: # agar taom taomlar ichidagi lug'atda bo'lsa true
        print(f"{taom.title()}ning narxi {taomlar[f"{taom}"]} so'm.")
    else: # aks holda False
        print("Bizda bunday taom yo'q.")

