"""
2/5/2025
Muallif:Elmurod O'rinboyev
33-dars. Fayllar bilan ishlash
"""
## Faylni to'liqligicha o'qish
with open('pi.txt') as fayl:
    pi = fayl.read()
    print(pi)

# ## 2-usul
# fayl = open('pi.txt')
# PI = fayl.read()
# print(PI)
# fayl.close()

## bunda .txt fayl ichidagi ma'lumot matn ko'rinishida bo'lib u son bo'lsa ham endi uni matndan songa o'tkazishni ko'raylik
pi = pi.rstrip() # qator ohiridagi bo'shliqlarni olib tashlaymiz.
pi = pi.replace('\n', '') # qator tashlash belgisini alamashtiramiz
pi = float(pi) # matnni float songa o'tkazamiz.
print(pi)

with open('data/talabalar.txt') as file:
    for line in file:
        print(line)
with open('data/talabalar.txt') as file:
    talabalar = file.readlines()
print(talabalar)
talabalar = [talaba.rstrip() for talaba in talabalar]
print(talabalar)

## Faylga yozish

# Yangi faylda yozish

faylnomi = 'data/ustozlar.txt' # ochilayotgan(yaratilayotgan) fayl nomi
with open(faylnomi, 'w') as fayl:
    fayl.write('Hoshim Niyozov')
    fayl.write('\nYoshi: 24 da.')


## pickle faylga yozish
import pickle

talaba1 = {'ism':'hasan', 'familiya':'husanov', 'tyil':2003, 'kurs': 2}
talaba2 = {'ism':'alijon', 'familiya':'valiyev', 'tyil':2004, 'kurs': 1}

with open('info','wb') as file:
    pickle.dump(talaba1,file)
    pickle.dump(talaba2,file)
with open('info','rb') as file:
    talaba1 = pickle.load(file)
    talaba2 = pickle.load(file)
print(talaba1)
print(talaba2)