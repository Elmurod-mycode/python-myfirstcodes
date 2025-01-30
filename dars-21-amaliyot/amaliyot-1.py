# Matnlardan iborat ro'yxat qabul qilib, ro'yxatdagi
# har bir matnning birinchi harfini katta harfga
# o'zgatiruvchi funksiya yozing.

def bosh_harf(royxat):
    sozlar=[]
    for a in royxat:
        sozlar.append(a.title())
    return sozlar



soz = ['olma', 'salom', 'meva', 'tong', 'tushlik','sayyora', 'dengiz']
soz.pop()
print(bosh_harf(soz))
