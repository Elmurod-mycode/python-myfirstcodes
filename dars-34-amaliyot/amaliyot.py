import json
data = {
    "Model":'Malibu',
    "Rang": 'Qora',
    'Yil': 2020,
    "Narx": 40000
}
# data = json.dumps(data)
# print(data)
# print(type(data))


with open("talaba_json.json", 'r') as file:
    talaba = json.load(file)
print(talaba)
print(type(talaba))
combinadet_data = {**talaba, **data}
with open("append_file.json", 'w') as file:
    json.dump(combinadet_data, file)
    print('Fayllar muvaffaqiyatli birlashtirildi.')