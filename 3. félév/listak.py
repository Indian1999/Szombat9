import math
import random
import matplotlib.pyplot as plt # terminálba: pip install matplotlib

# Listák

lista = []

# Lista comprehension

lista = [2 for i in range(5)] # [2, 2, 2, 2, 2]
print(lista)

lista = ["kalap" for i in range(3)] # ['kalap', 'kalap', 'kalap']
print(lista)

lista = [i for i in range(1, 7)] # [1,2,3,4,5,6]
print(lista)

lista = [i**2 for i in range(1, 11)] 
print(lista) # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

lista = [random.randint(1, 99) for i in range(10)]
print(lista) # [5, 28, 40, 98, 22, 78, 39, 71, 18, 74]

lista = [round(math.sin(math.radians(i)), 2) for i in range(0, 361, 15)]
print(lista)

def f(x):
    return x**2 + x - 6

lista = [f(i) for i in range(-5, 6)]
print(lista) # [14, 6, 0, -4, -6, -6, -4, 0, 6, 14, 24]

lista = [[] for i in range(4)]
print(lista) # [[], [], [], []]

lista = [[1,2,3,4] for i in range(3)]
print(lista) # [[1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4]]

lista = [[i for j in range(6)] for i in range(5)]
print(lista) # [[0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 1], [2, 2, 2, 2, 2, 2], [3, 3, 3, 3, 3, 3], [4, 4, 4, 4, 4, 4]]

lista = [[i*j for j in range(1, 11)] for i in range(1, 11)]
for row in lista:
    print(row)

kep = [[[random.randint(0, 255) for k in range(3)] for j in range(200)] for i in range(100)]

plt.imshow(kep)
plt.axis("off")
plt.savefig("random_kep.png")
plt.close()

def is_prime(num):
    if num == 1:
        return False
    for i in range(2, num // 2 + 1):
        if num % i == 0:
            return False
    return True

lista = [i for i in range(1, 100) if is_prime(i)]
print(lista) # [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

lista = [i for i in range(1, 30) if "2" in str(i)]
print(lista) # [2, 12, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29]

kep = [[255 if j == 20 or j == 80 or i == 20 or i == 80 else 0 for j in range(100)] for i in range(100)]

plt.imshow(kep)
plt.axis("off")
plt.savefig("negyzet.png")
plt.close()

lista = [1 if i % 2 == 0 else 0 for i in range(1, 11)]
print(lista) # [0, 1, 0, 1, 0, 1, 0, 1, 0, 1]

lista = [i for i in range(12)]
print(lista)
# Listák indexelése (0-tól indexelünk)

print(lista[3]) # 1
print(lista[-1]) # A lista utolsó elemét
print(lista[-4]) # Hátulról a 4. elemet
#print(lista[12]) # IndexError: list index out of range

# Slicing-olós indexelés:
# Logikája ugyan az mint a range függvénynek
print(lista[2:7]) # 2. 3. 4. 5. 6. indexű elemeket választja ki ([0, 1, 0, 1, 0]) 7. NINCS BENNE
print(lista[:5])  # Az elejétől az 5. indexig. 5. MÁR NINCS BENNE
print(lista[7:])  # 7. indextől a legvégéig (utolsó is benne van) 
print(lista[:])   # Az elejétől a végéig

print(lista[2:8:2]) # 2-tól a 8-ig (8 NINCS BENNE), 2-eseével # [0, 0, 0]
print(lista[::2])   # Elejétől végéig, minden második
print(lista[5::3])  # 5.-től a végéig hármasával   [5, 8, 11]
print(lista[1:9:-1]) # 1-től a 9-ig hátrafelé haladva    []
print(lista[9:1:-1]) # [9, 8, 7, 6, 5, 4, 3, 2]    az 1-es index NINCS benne
print(lista[::-1])   # Megfordítja a listát



# 1. feladat: Generáljunk egy listát ami a számokat tartalmazza 4-től 15-ig
lista = [i for i in range(4, 16)]
print(lista)

# 2. feladat: Generáljunk egy listát ami a számokat tartalmazza 4-től 25-ig, de csak a párosak
lista = [i for i in range(4, 26) if i % 2 == 0]
lista = [i for i in range(4, 26, 2)]
print(lista)

# 3. feladat: Generáljunk egy listát ami a számokat tartalmazza 0, 361-ig, 45 ösével
lista = [i for i in range(0, 361) if i % 45 == 0]
lista = [i for i in range(0, 361, 45)]
print(lista)

# 4. feladat: Generáljunk egy listát ami a számokat tartalmazza, 1 és 200 között, de csak azokat
# amelyek számjegyeinek összege: 10     (pl.: 19, 118, 145)

def szamjegy_osszeg_10(num):
    osszeg = 0
    for szamjegy in str(num):
        osszeg += int(szamjegy)
    return osszeg == 10

lista = [i for i in range(1, 201) if szamjegy_osszeg_10(i)]
print(lista)

# 5. feladat: Generáljunk egy táblázatot ami 2 kockával való dobásnak a lehetséges eredményeit tartalmazza.
# (Ha 2 kockával dobunk akkor a dobás eredménye a 2 szám összege)

# 5.b: Mekkora a valószínűsége annak, hogy 9-et dobok?

# 5.c: Melyik számnak a legnagyobb a valószínűsége?