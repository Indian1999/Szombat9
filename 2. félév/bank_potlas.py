# Mátrix: AZ egy olyan lista ami listákat tárol

mtx = [
    [9, 3, 5, 8, 5],
    [1, 9, 3, 5, 3],
    [1, 2, 3, 4, 5]
]

#print(mtx)
for item in mtx:
    print(item)

# indexelés:
print("mtx[2] =", mtx[2])
print("mtx[2][3] =", mtx[2][3])

# Sor-oszlop vagy Oszlop-sor bejárást alkalmazunk
# len(mtx) = 3  -   sorok száma
# len(mtx[0]) = 5   oszlop száma

# Határozzuk meg a mátrix elemeinek összegét!
összeg = 0
for i in range(len(mtx)): # i = 0, 1, 2
    for j in range(len(mtx[i])): # j = 0, 1, 2, 3, 4
        összeg += mtx[i][j]
print("összeg:", összeg)

#Melyik a legnagyobb szám a mátrixban?
maximum = mtx[0][0]
for i in range(len(mtx)):
    for j in range(len(mtx[i])):
        if maximum < mtx[i][j]:
            maximum = mtx[i][j]
print("maximum:", maximum)

# List comprehension
lista = [0 for i in range(5)]
print(lista) # [0, 0, 0, 0, 0]
lista = [i for i in range(3, 8)]
print(lista) # [3, 4, 5, 6, 7]
lista = [i**2 for i in range(1, 6)]
print(lista) # [1, 4, 9, 16, 25]
lista = [[] for i in range(4)]
print(lista) # [[], [], [], []]
lista = [[1, 2, 3] for i in range(4)]
print(lista) # [[1, 2, 3], [1, 2, 3], [1, 2, 3], [1, 2, 3]]
lista = [[i*5 + j for j in range(5)] for i in range(4)]
for item in lista:
    print(item)
