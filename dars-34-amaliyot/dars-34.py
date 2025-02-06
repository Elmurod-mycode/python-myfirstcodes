"""
2/6/2025
Muallif: Elmurod O'rinboyev
34-dars. Json
"""
import json
x = 10
x_json = json.dumps(x)
print(type(x_json))
print(x_json)
ism = "Anvar"
ism_json = json.dumps(ism)

bemor = {
    'ism': "Vali Aliyev",
    'yosh' : 150,
    'oila' : True,
    'farzandlar' : ('Jamil', "Halil"),
    'alergiya' : None,
    "dorilar" : [
        {"nomi": 'Analgin', 'miqdor': 0.25},
        {'nomi': 'Panadol', 'miqdori': 1}
    ]
}
with open('aholi_soni.json', 'r') as file:
    aholi_soni = json.load(file)
print(aholi_soni)


