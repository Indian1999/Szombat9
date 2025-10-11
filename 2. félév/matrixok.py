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