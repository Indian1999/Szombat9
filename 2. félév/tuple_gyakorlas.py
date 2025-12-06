import random

# 1. feladat: Osztályzatokkal
# Adott egy osztály matek dolgozatainak eredménye egy listában (%-ban megadva)
# a, Generáljunk egy 30 elemű listát (0-100) közötti értékekkel
szazalekok = [random.randint(0, 100) for i in range(30)]

# b, Készítsünk egy listát ami százalék-osztályzat párokat tárol (tuple)
# pl.: [(32, 1), (75, 4), (56, 3), ...]
# Az osztályzat a %-os eredmény alapján van meghatározva:
# 1:  0-39
# 2: 40-54
# 3: 55-69
# 4: 71-88
# 5: 89-100
eredmenyek = []
for item in szazalekok:
    if item >= 89:
        eredmenyek.append((item, 5))
    elif item >= 71:
        eredmenyek.append((item, 4))
    elif item >= 55:
        eredmenyek.append((item, 3))
    elif item >= 40:
        eredmenyek.append((item, 2))
    else:
        eredmenyek.append((item, 1))
print(eredmenyek)