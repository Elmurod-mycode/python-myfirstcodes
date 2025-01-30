# Yuqoridagi funksiyani asl ro'yxatni o'zgartirmaydigan
# va yangi ro'yxat qaytaradigan qilib o'zgartiring

def bosh_harf(royxat):
    sozlar=[]
    for a in royxat[:]:
        sozlar.append(a.title())
    return sozlar



soz = ['olma', 'salom', 'meva', 'tong', 'tushlik','sayyora', 'dengiz']

print(bosh_harf(soz))
print(soz)
