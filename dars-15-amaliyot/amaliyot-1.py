#Python izohli lug'atini yarating va lug'atga kamida 10 ta so'z qo'shing.
# Lug'atdagi har bir kalit va qiymatni for tsikli yordamida,
# alifbo ketma-ketligida chiroyli qilib konsolga chiqaring.

dictionary_python = {
    'int' : 'butun son',
    'float': "o'nlik son",
    'if' : 'agar',
    'elif' : 'agar aks holda',
    'else' : 'aks holda',
    'set' : 'takrorlanmas ro\'yxat '
}
for dictionary in sorted(dictionary_python.keys()):
    print(dictionary)
for dictionary_v in sorted(dictionary_python.values()):
    print(dictionary_v)