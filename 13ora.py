import random
# 1. feladat: Adott 2 lista, szedjük ki egy 3. listába azokat az értékeket, amik mind a 2 listában benne vannak

lista1 = [random.randrange(1, 100) for i in range(28)]
lista2 = [random.randrange(1, 100) for i in range(32)]
print(lista1)
print(lista2)
kozos_lista = []
for item in lista1:
    if item in lista2 and item not in kozos_lista:
        kozos_lista.append(item)
print(kozos_lista)

# 2. feladat: adott egy egész számokból álló lista. Fűzzük össze az elemeit egy számmá
lista = [3, 12, 32, 8] # 312328
number = ""
for item in lista:
    number += str(item)
number = int(number)
print(number)


# 3. feladat: Rendezett-e a lista?
lista = [43, 54, 62, 84, 90, 91, 99, 103, 109]
lista = lista[::-1] # Megfordítja a listát
növekvő = True
csökkenő = True
for i in range(0, len(lista) - 1):
    if lista[i] > lista[i+1]:
        növekvő = False
for i in range(0, len(lista) - 1):
    if lista[i] < lista[i+1]:
        csökkenő = False
if növekvő:
    print("A lista növekvő sorrendbe rendezett.")
elif csökkenő:
    print("A lista csökkenő sorrendbe rendezett.")
else:
    print("A lista nincs rendezve.")        

# 4. feladat: Két listát alakítsunk ugyan olyanra. Mindkét listát egészítsük azokkal az
# elemekkel amik a másikban is megvannak, rendezzük őket
lista1 = [random.randrange(1, 41) for i in range(15)]
lista2 = [random.randrange(1, 41) for i in range(12)]
# Minden elem csak egyszer szerepeljen: (ne legyen 2 vagy több 6-os)
lista1 = list(set(lista1))
lista2 = list(set(lista2))
print(lista1)
print(lista2)
""" for ciklus listákra:
for item in lista1: 
    print(item, end = " ")
print()
for i in range(0, len(lista1)):
    print(i, end=" ")
print()
"""
for item in lista1:
    if item not in lista2:
        lista2.append(item)
for item in lista2:
    if item not in lista1:
        lista1.append(item)
lista1.sort()
lista2.sort()
print(lista1)
print(lista2)

# 5. feladat: Írjuk ki azokat a termékeket amik kevesebb mint 100 forintba kerülnek
termékek = ["alma", "csoki", "kenyér", "tej", "könyv", "ceruza", "fánk", "zokni", "fogkefe", "csirkemell"]
árak = [210, 600, 1100, 450, 3000, 1200, 200, 2000, 390, 2500]
print("Az 1000 Ft-nál olcsóbb termékek:")
for i in range(len(árak)):
    if árak[i] < 1000:
        print(f"{termékek[i]} - {árak[i]} Ft")
        #print(termékek[i] + " - " + str(árak[i]) + " Ft")

num = 7
print("A num változó értéke: " + str(num) + ".")
print(f"A num változó értéke: {num}.")
print("A num változó értéke: {num}.")

# 6. feladat: Melyik termék a legdrágább és mennyibe kerül?

# 7. feladat: Átlagosan mennyibe kerülnek a termékek?

# 8. feladat: Mennyibe kerül 2 alma, 4 tej, 3 csoki, 1 könyv és 2 zokni

