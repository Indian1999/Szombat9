import random
# 1. feladat: Töltsünk fel egy listát 1-100-ig 3-mal osztható számokkal
lista = []
for i in range(1, 101):
    if i % 3 == 0:
        lista.append(i)
print(lista)

# 2. feladat: Töltsünk fel egy listát 1-1000-ig olyan számokkal, amik 19-re végződnek
lista = []
for i in range(19, 1001, 100):
    lista.append(i)
print(lista)

# 3. feladat: Tölstünk fel egy listát 20 random számmal (1-100)
lista = []
for i in range(20):
    lista.append(random.randint(1,100))
print(lista)
print(len(lista))
# 4. feladat: a 3. feladatban elkészített listában határozzuk meg az elemek összegét!
összeg = 0
for i in range(len(lista)):
    összeg += lista[i]
print("A lista elemeinek az összege:", összeg)

# 5. feladat: határozzuk meg az elemek átlagát!
print("Átlag:", round(összeg / len(lista), 2)) 
# 6. feladat: Melyik szám a legnagyobb/legkisebb a listában?
maximum = lista[0]
for i in range(len(lista)):
    if lista[i] > maximum:
        maximum = lista[i]
print("A legnagyobb szám:", maximum)

minimum = lista[0]
for i in range(len(lista)):
    if lista[i] < minimum:
        minimum = lista[i]
print("A legkisebb szám:", minimum)

# 7. feladat: Számoljuk meg, hogy hány egyjegyű szám van a listában
számláló = 0
for i in range(len(lista)):
    if lista[i] >= 0 and lista[i] <= 9:
        számláló += 1
print(f"{számláló} db egyjegyű szám van a listában.")

# 8. feladat: Határozzuk meg a páros számok összegét
# 9. feladat: Ha elkezdem számolgatni a listában lévő számokat, olyan módon, hogyha 2-vel osztható a szám, akkor hozzáadom az összértékhez, ha nem osztható 2-vel, akkor kivonom, mennyi lesz a végeredmény?
#pl.: [1,2,3,4, 8, 1, 9, 23, 22] -> -1 + 2 -3 + 4 + 8 -1 -9 - 23 + 22 = -1
paros_osszeg = 0
paros_paratlan_osszeg = 0
for i in range(len(lista)):
    if lista[i] % 2 == 0:
        paros_osszeg += lista[i]
        paros_paratlan_osszeg += lista[i]
    else:
        paros_paratlan_osszeg -= lista[i]

print("A páros számok összege:", paros_osszeg)
print("Páros-Páratlan összeg:", paros_paratlan_osszeg)
# 10. feladat: Szedjük szét a listát 3 különböző listára:
# a, 3-mal osztva: 0-t adnak maradékul
# b, 3-mal osztva: 1-t adnak maradékul
# c, 3-mal osztva: 2-t adnak maradékul
lista_a = []
lista_b = []
lista_c = []
for i in range(len(lista)):
    if lista[i] % 3 == 0:
        lista_a.append(lista[i])
    elif lista[i] % 3 == 1:
        lista_b.append(lista[i])
    else:
        lista_c.append(lista[i])
print(lista_a)
print(lista_b)
print(lista_c)