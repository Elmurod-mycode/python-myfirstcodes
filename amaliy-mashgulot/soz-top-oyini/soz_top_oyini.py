"""So'z top oyini."""

import random
from uzwords import uzbek_words as words

def get_word():
    word = random.choice(words)
    while "'" in word or ' ' in word:
        word = random.choice(words)
    return word.lower()
def display(user_latters, word):
    display_letter = ""
    for letter in word:
        if letter in user_latters.lower():
            display_letter += letter
        else:
            display_letter += "_"
    return display_letter

def play():
    word = get_word() # so'zdagi harflar
    word_letters = set(word) # foydalanuvchi kiritgan harfalar
    user_letters = ""
    print(f"Men {len(word)} xonali son o'yladim. Topa olasizmi?")
    while len(word_letters)>0:
        print(display(user_letters, word))
        if len(user_letters)>0:
            print(f"Shu vaqtgacha kiritgan harflaringiz: {user_letters}")
        letter = input("Harf kiriting: ").lower()
        if letter in user_letters:
            print("\nBu harfni avval kiritgansiz. Boshqa harf kiriting.\n")
            continue
        elif letter in word:
            word_letters.remove((letter))
            print(f"{letter} harfi to'g'ri.")
        else:
            print("Bunday harf yo'q,")
        user_letters+=letter
    print(f"\nTABRIKLAYMAN! \"{word}\" so'zini {len(user_letters)} ta urinishda topdingiz.")

print(play())
