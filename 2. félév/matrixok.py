# Mátrixok
import random
import numpy as np         # Terminálba: pip install numpy
import matplotlib.pyplot   # pip install matplotlib

# Mátrix: Egy lista ami listákat tárol
mtx = [
#    0  1  2  3  4  5  6  7
    [9, 3, 2, 9, 3, 8, 2, 3],   # 0    
    [2, 7, 11, 3, 5, 5, 1, 2],  # 1 
    [3, 6, 48, 2, 2, 8, 2, 7],  # 2 
    [9, 1, 4, 0, 8, 9, 9, 3],   # 3
    [8, 0, 44, 1, 2, 5, 2, 8]   # 4
]

# lista = [69984, ...]
print(mtx)
for row in mtx:
    print(row)

print("indexelés:")
print("mtx[2] =", mtx[2])
print("mtx[2][3] =", mtx[2][3])

# Programozási tételek mátrixokra:
# Sor-oszlop vagy oszlop-sor bejárást alkalmazunk
# len(mtx) - sorok száma
# len(mtx[i]) - oszlopok száma

# Összegzés tétele:
összeg = 0
for i in range(len(mtx)): # A sorokon megyünk végig
    for j in range(len(mtx[i])): # Az oszlopok megy végig
        összeg += mtx[i][j]
print("Az elemek összege:", összeg)

# Maximum kiválasztás:
maximum = mtx[0][0]
for i in range(len(mtx)):
    for j in range(len(mtx[i])):
        if mtx[i][j] > maximum:
            maximum = mtx[i][j]
print("A legnagyobb szám a mátrixban:", maximum)

# Eldöntés tétele:
# Tartalmaz-e 7-tel osztható számot a mátrix?
feltétel = False
számláló = 0    # Összehasonlításokat számoljuk (Hányszor fut le az if)
for i in range(len(mtx)):
    for j in range(len(mtx[i])):
        számláló += 1
        if mtx[i][j] % 7 == 0:
            feltétel = True
            break # kilép az aktuális ciklusból
    if feltétel:
        break

print(f"Összesen {számláló} elemet ellenőriztünk.") # 40 -> 24 -> 10
if feltétel:
    print("Van 7-tel osztható szám.")
else:
    print("Nincs 7-tel osztható szám")

# Megszámlálás tétele:
# Hány elem van a mátrixban ami 3-mal osztható (De nem 0!)
számláló = 0
for i in range(len(mtx)):
    for j in range(len(mtx[i])):
        if mtx[i][j] % 3 == 0 and mtx[i][j] != 0:
            számláló += 1
print(számláló," db 3-mal tényleges osztható szám szerepel a mátrixban.")

# Feltételes összegzés:
# Határozzuk meg a páratlan számok összegét
ptlan_összeg = 0
for i in range(len(mtx)):
    for j in range(len(mtx[i])):
        if mtx[i][j] % 2 == 1:
            ptlan_összeg += mtx[i][j]
print("A páratlan elemek összege:", ptlan_összeg)

# Bónusz:
# Hozzunk létre egy új listát, ennek a listának az elemei a mtx sorainak a szorzatai
lista = []
for i in range(len(mtx)):
    szorzat = 1
    for j in range(len(mtx[i])):
        if mtx[i][j] == 0:
            szorzat = 0
            break
        szorzat *= mtx[i][j]
    lista.append(szorzat)

print("A számok szorzata soronként:", lista)

# List comprehension
lista = [0 for i in range(10)]
print(lista) # [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
lista = [i**2 for i in range(1, 10)]
print(lista) # [1, 4, 9, 16, 25, 36, 49, 64, 81]
lista = [[] for i in range(6)]
print(lista) # [[], [], [], [], [], []]
lista = [[i*6 + j for j in range(6)] for i in range(4)]
print(lista) # [[0, 1, 2, 3, 4, 5], ..., [18, 19, 20, 21, 22, 23]]
mtx3d = [[[random.randint(-20,20) for k in range(3)] for j in range(4)] for i in range(3)]
print(mtx3d) #[[[6, -8, 12], ..., [-7, -6, 6]],..., [[12, -8, 12], ..., [-11, 10, -2]]]
print(mtx3d[0][1][2])

# Összegzés tétele 3d mátrixra
# Annyi ciklus kell, ahány dimenziós a mátrix
összeg = 0
for i in range(len(mtx3d)):
    for j in range(len(mtx3d[i])):
        for k in range(len(mtx3d[i][j])):
            összeg += mtx3d[i][j][k]
print("Összeg =", összeg)