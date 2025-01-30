#Uchta son qabul qilib,
# ulardan eng kattasini qaytaruvchi funksiya yozing
def maxNum(a, b, c):
    max = a
    if b>=max:
        max=b
    if c>=max:
        max=c
    return max


max = maxNum(12,15,45)
print(max)