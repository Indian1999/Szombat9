nevek = ["András", "Béla", "Cecil", "Dénes", "Elemér", "Ferenc"]
print(nevek)
print(type(nevek))
print("A nevek lista elemeinek a száma:", len(nevek))

print(nevek[4]) # Elemér
print(nevek[0]) # András
print(nevek[len(nevek) - 1]) # Ferenc
# Pythonban egyedülállóan tudunk negatív indexet megadni
print(nevek[-1]) # Hátulról az első elem (Ferenc)
print(nevek[-4]) # Cecil

# Van lehetőségünk intervallum indexelésre is

print(nevek[2:5]) # ['Cecil', 'Dénes', 'Elemér'] 
#2-es indextől az 5-ös indexig (Az 5. már nincs benne az intervallumban)
print(nevek[:3]) # Ha : elé nem írok semmit, akkor az elejétől vesszük az elemeket
# András, Béla, Cecil
print(nevek[2:]) # a 2.-tól a legvégéig    [Cecil, Dénes, Elemér, Ferenc]
print(nevek[:]) # Legelejétől a legvégéig

print(nevek[1:4:-1]) # [] 1-től 4-ig -1-esével
print(nevek[4:1:-1]) # [Elemér, Dénes, Cecil]
print(nevek[::2])    # ['András', 'Cecil', 'Elemér']

# Készítsünk egy másolatot a nevekről:
names = nevek
names[0] = "Andrew"

print("names:", names)
print("nevek:", nevek)

names[0] = "András"
# Tapasztalat: A nevek lista is változott. Mert a két változó ugyan arra a memóriacímre mutat.
# Listák másolásánál a mutató fog lemosolódni. Ha ezt szeretnénk elkerülni, akkor van több lehetőség.

names = nevek[:]
names[0] = "Andrew"
print("names:", names)
print("nevek:", nevek)

# 2. megoldás
names = []
for i in range(len(nevek)):
    names.append(nevek[i])
names[0] = "Andrew"
print("names:", names)
print("nevek:", nevek)

# copy függvény
names = nevek.copy() #Átmásolja egy memória helyre az elemeket
names[0] = "Andrew"
print("names:", names)
print("nevek:", nevek)

# Milyen lehetőségeink vannak egy lista bejárására?

# Klasszik: Elől tesztelős (while) ciklus

i = 0
while i < len(nevek):
    print(nevek[i], end = " ")
    i += 1
print()

# Számlálós ciklus (for)

for i in range(len(nevek)):
    print(nevek[i], end = " ")
print()

# foreach ciklus (for)
# Az item sorjában felveszi a nevek lista elemeit
for item in nevek: # item = András, Béla, ...
    print(item, end= " ")
print()

# Vegyíthetjük a két for ciklus
for index, value in enumerate(nevek): # index = 0, 1, 2, 3, 4, 5 value = András, Béla, Cecil, ..
    print(f"{index}: {value}", end = " ")
print()

# range() függvény

for i in range(5): # i = 0, 1, 2, 3, 4
    print(i, end = " ")
print()

for i in range(5, 10): # i = 5, 6, 7, 8, 9 
    print(i, end = " ")
print()

for i in range(10, 100, 20): # i = 10, 30, 50, 70, 90
    print(i, end = " ")
print()

for i in range(5, 2, -1): # i = 5, 4, 3
    print(nevek[i], end= " ")
print()

# Generáljunk listákat

lista = []
for i in range(10):
    lista.append(i)
print(lista)
print()
print("#" * 50)
print()
# 1. feladat: Generáljunk egy listát ami a számokat tartalmazza 0-20-ig
print("1. feladat:")
lista = []
for i in range(21):
    lista.append(i)
print(lista)

# 2. feladat: 5-15-ig a számok egy listában
print("2. feladat:")
lista = []
for i in range(5, 16):
    lista.append(i)
print(lista)

# 3. feladat: [15, 30, 45, 60, ..., 150]
print("3. feladat:")
lista = []
for i in range(15, 151, 15):
    lista.append(i)
print(lista)

# 4. feladat: [80, 79, 78, ..., 56, 55, 54]
print("4. feladat:")
lista = []
for i in range(80, 53, -1):
    lista.append(i)
print(lista)

# 5. feladat: [1, 4, 9, 16, 25, 36, ..., 400] (négyzetszámok)
print("5. feladat:")
lista = []
for i in range(1, 21):
    lista.append(i*i)
print(lista)

# 6. feladat: [1, 1, 2, 3, 5, 8, 13, 21, 34, ...] (fibonacci) Összesen mondjuk 20 elem
print("6. feladat:")
lista = [1, 1]
while len(lista) < 20:
    lista.append(lista[-1] + lista[-2])
print(lista)

# 7. feladat: [1, -2, 3, -4, 5, -6, .... 9, -10]
print("7. feladat:")
lista = []
for i in range(1, 11):
    if i % 2 == 0:
        lista.append(-i)
    else:
        lista.append(i)
print(lista)

# 8. feladat: [1, -1, 2, -2, 3, -3, .... 9, -9, 10, -10]
print("8. feladat:")
lista = []
for i in range(1, 11):
    lista.append(i)
    lista.append(-i)
print(lista)

# 9. feladat: Az első 20 prímszámot tartalmazza
""" Kövi órán beszéljük meg!"""
print("9. feladat:")
lista = []
num = 2
while len(lista) < 20:
    isPrime = True
    for i in range(2, num):
        if num % i == 0:
            isPrime = False
    if isPrime:
        lista.append(num)
    num += 1
print(lista)

# 10. feladat: [100-999, azok a számok, amelyekben szerepel a 13] (132, 813)
print("10. feladat:")
lista = []
for i in range(100, 1000):
    if "13" in str(i):
        lista.append(i)
print(lista)