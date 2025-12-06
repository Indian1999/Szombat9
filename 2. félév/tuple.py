import random
# A tuple adatszerkezet
# Ugyan az, mint a lista, DE NEM módosítható (immutable)
# (Ha már létrehoztuk, nem tudjuk átírni az elemeit, törölni/hozzáadni)
# Ettől függetlenül természetesen, újradefiniálni lehet

myTuple = (1,2,3,4,5)
print(myTuple)
print(type(myTuple)) # <class 'tuple'>

myTuple = ("Alma", 2, 3.13, True, range(1,5), [4, 2, 4, 1], (1,2,3), 4, 8)
print(myTuple)

empty_tuple = ()
print(empty_tuple)

lista = [5]
myTuple = (5) # <- aritmetikai (matematikai)kifejezésként értelmezi
print(myTuple) # 5
print(type(myTuple)) # <class 'int'>

myTuple = (5,) # <- jelöli, hogy nem aritmetikai, hanem tuple
print(myTuple) # (5,)
print(type(myTuple)) # <class 'tuple'>

myTuple = 5, 3, 1 # Olvashatóság szempontból nem javaslom
print(myTuple) # (5, 3, 1)
print(type(myTuple)) # <class 'tuple'>

# Tuple műveletek

def illegal_operations():
    # Nincs append függvénye, a tuple objektumnak
    myTuple.append(5) # AttributeError: 'tuple' object has no attribute 'append'
    myTuple.insert(0, 8) # AttributeError: 'tuple' object has no attribute 'insert'
    del myTuple[1] # TypeError: 'tuple' object doesn't support item deletion
    myTuple[1] = 8 # TypeError: 'tuple' object does not support item assignment

def indexeles():
    myTuple = (8, 1, 2, 4, 3)
    print(myTuple[3]) # 4 
    print(myTuple[1:4]) # (1, 2, 4)
    print(myTuple[1:]) # (1, 2, 4, 3)
    print(myTuple[:4]) # (8, 1, 2, 4)
    print(myTuple[:]) # (8, 1, 2, 4, 3)
    print(myTuple[:4:2]) # (8, 2)
    print(myTuple[::-1]) # megfordítja a tuplet

indexeles()

# Több elemet egy helyen akarunk tárolni, de nem nagyon akarjuk módosítani

tuple1 = (1,2,3)
tuple2 = (3,4,5)
tuple3 = (3,1,2)
tuple4 = (1,2,3)
print(tuple1 == tuple2) # False
print(tuple1 == tuple3) # False
print(tuple1 == tuple4) # True

# operátorok

print(tuple1 + tuple2) # (1, 2, 3, 3, 4, 5)
print(tuple1 * 3) # (1, 2, 3, 1, 2, 3, 1, 2, 3)

# (list) comprehension is működik (generátorral is létre lehet hozni)

myTuple = (0 for i in range(10))
print(myTuple) # <generator object <genexpr> at 0x000001B30D6205F0>

myTuple = tuple(0 for i in range(10)) # Generátort, tuple-lé konvertálunk
print(myTuple) # (0, 0, 0, 0, 0, 0, 0, 0, 0, 0)

myTuple = tuple([5, 2, 4, 2])
print(myTuple) # (5, 2, 4, 2)

myTuple = tuple(random.randint(0, 9) for i in range(10))
print(myTuple)

if 5 in myTuple:
    print("Van benne 5-ös")
    count_5 = myTuple.count(5)
    index_5 = myTuple.index(5) # Potenciális hiba: ValueError: tuple.index(x): x not in tuple
    print(f"Az első 5-ös a {index_5}. indexen található.")
    print(f"{count_5} db 5-ös van a tuple-ben.")
else:
    print("Nincs benne 5-ös")


print("A legnagyobb elem:",max(myTuple))
print("A legkisebb elem:",min(myTuple))
print("Az elemek összeg:",sum(myTuple))
print("Az elemek átlaga:",sum(myTuple)/len(myTuple))

# Adott egy tuple, írjuk át minden elemét a háromszorosára!
print(myTuple)
tempList = []
for i in range(len(myTuple)):
    #myTuple[i] *= 3 # TypeError: 'tuple' object does not support item assignment
    tempList.append(myTuple[i] * 3)
myTuple = tuple(tempList)
print(myTuple)

# Írjunk egy függvényt, ami "átírja" egy tuple elemét
def change_i_to(tuple, index, value):
    # pl.: tuple = (5, 2, 1, 6, 8, 4, 2, 6), index = 3, value = 0
    # return (5, 2, 1) + (0,) + (8, 4, 2, 6) -> (5, 2, 1, 0, 8, 4, 2, 6)
    return tuple[:index] + (value,) + tuple[index+1:]

myTuple = change_i_to(myTuple, 5, -1)
print(myTuple)

# Tegyük fel, hogy szeretnénk egy hatalmas mátrixot
matrix = [[0 for j in range(5)] for i in range(8)] # 8 sor, 5 oszlop
# 8 * 5 = 40 int objektumot lefoglalok a memóriában

# Mi A helyzet, ha akarok 50000 sort, 50000 oszloppal
# matrix = [[0 for j in range(50000)] for i in range(50000)]  Több mint 9 gigabyte ram kéne

matrix_indexek = [(3450, 780), (1230, 95), (32432, 1)]
matrix_ertekek = [990, 111, 342]
matrix_sorok = 50000
matrix_oszlopok = 50000

def get_cell_value(indeces, values, i, j):
    if (i,j) in indeces:
        index = indeces.index((i,j))
        return values[index]
    else:
        return None

print(get_cell_value(matrix_indexek, matrix_ertekek, 3450, 780)) # 990
print(get_cell_value(matrix_indexek, matrix_ertekek, 3450, 787)) # None

# egy elemhez el kell tárolni, a sort, oszlopot, értéket 
# (egy értékhez 3 int objektum kell)
# Ez azt jelenti, ha a mátrix min. 1/3 része fel van töltve értékekkel, 
# akkor már jobb a classic mátrix reprezentáció

# Ez a módszer a sparse matrix (ritka mátrix)
# Akkor érdemes használni, ha nagy a mátrix, 
# de kevesebb mint 1/3-része van fel töltve értékkel

