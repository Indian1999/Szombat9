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

# c, Írjuk ki a legjobb és legrosszabb eredményeket (százalékos)
mini = 0
maxi = 0
for i in range(1, len(eredmenyek)):
    if eredmenyek[i][0] > eredmenyek[maxi][0]:
        maxi = i
    if eredmenyek[i][0] < eredmenyek[mini][0]:
        mini = i
print(f"A legjobb százalékos eredmény: {eredmenyek[maxi][0]}")
print(f"A legrosszabb százalékos eredmény: {eredmenyek[mini][0]}")

# d, Írjuk ki az átlag százalékos eredményt, és az átlag osztályzatot
szazalek_sum = 0
osztalyzat_sum = 0
for item in eredmenyek:
    szazalek_sum += item[0]
    osztalyzat_sum += item[1]
print(f'A százalékos eredmények átlaga: {round(szazalek_sum/len(eredmenyek),2)}')
print(f'Az osztályzatok átlaga: {round(osztalyzat_sum/len(eredmenyek),2)}')

# e, Írjuk ki a legtöbbször és legkevesebbszer előforduó osztályzatokat
osztalyzat_szamlalo = ["buffer", 0, 0, 0, 0, 0]
for item in eredmenyek:
    osztalyzat_szamlalo[item[1]] += 1
mini = 1
maxi = 1
for i in range(2, len(osztalyzat_szamlalo)):
    if osztalyzat_szamlalo[i] > osztalyzat_szamlalo[maxi]:
        maxi = i
    if osztalyzat_szamlalo[i] < osztalyzat_szamlalo[mini]:
        mini = i

print(f"A legtöbbször előforduló osztályzat: {maxi} ({osztalyzat_szamlalo[maxi]} db)")
print(f"A legkevesebbszer előforduló osztályzat: {mini} ({osztalyzat_szamlalo[mini]} db)")

# f, A tanulók hány százaléka bukott meg (1-est)
szazalek_egyes = osztalyzat_szamlalo[1] / len(eredmenyek) * 100
print(f"A tanulók {round(szazalek_egyes, 1)} %-a bukott meg.")


# Adott: 2 elemű tuple-ök listája
# Ebben a listában egy koordinátarendszer pontjait tároljuk
pontok = [
    (12, -7), (-34, 22), (49, -18), (-25, 50), (7, 7),
    (-11, -46), (3, 29), (41, -9), (-50, -12), (18, 33),
    (27, -22), (-8, 44), (0, -35), (-39, 6), (25, 17),
    (-20, -4), (8, -50), (33, 12), (-47, 31), (14, -27),
    (5, 49), (-23, -33), (50, 0), (-14, 18), (29, -11),
    (-5, 8), (38, 40), (-32, -19), (11, -1), (6, -44),
    (-27, 25), (19, 3), (-48, -7), (44, -32), (-16, 14),
    (30, -29), (-9, 50), (2, -13), (-35, 39), (47, 4),
    (-6, -28), (20, 45), (-31, 9), (13, -36), (0, 22),
    (-22, 48), (36, -5), (-12, -17), (50, -50), (-29, 27)
]

# a, Melyik pont van legközelebb az origóhoz?

# b, Kérjünk be egy pontot, adjuk meg, a hozzá legközelebbi pontot

