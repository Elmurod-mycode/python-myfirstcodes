# Istalgancha sonlarni qabul qilib,
# ularning ko'paytmasini qaytaruvchi funksiya yozing

def sonlar1(*sonlar):
    """Istalgancha sonlarni qabul qilib, ularni
    ko'paytmansini qabul qilivchi fuksiya."""
    kopaytma = 1
    for son in sonlar:
        kopaytma=son*kopaytma
    return kopaytma
print(sonlar1(12,14,13,24))