# 1. feladat: Írjuk ki 1436-től 2347- ig azokat a számokat amelyek 7-tel és 5-gyel is oszhatók
for i in range(1436, 2348):
    if i % 7 == 0 and i % 4 == 0:
        print(i)
        
# 2. feladat: Állítsuk elő az összes lehetséges vezetéknév + keresztnév kombinációt
keresztnevek = ["James", "Amy", "Charles", "Gabriel"]
vezeteknevek = ["Smith", "Boyle", "Novak", "Doe"]

for kereszt in keresztnevek:
    for vezetek in vezeteknevek:
        print(kereszt, vezetek)
        
# 3. feladat: Írjunk ki * karaktereket félpiramis alakban
#    *
#    **
#    ***
#    ****
#    *****

for i in range(1, 11):
    print("*" * i)
    
# 4. feladat: Találjuk meg és írjuk ki az összes lehetséges párt
nevek = ["Ádám", "Béla", "Cecil", "Dénes", "Elemér", "Ferenc", "Gábor", "Hugó"]
# Ádám Béla
# Cecil Dénes (Dénes Cecil ne legyen)
for i in range(len(nevek)):
    for j in range(i + 1, len(nevek)):
        print(nevek[i], nevek[j])

# 5. feladat: Keressük meg egy adott pozitív egész szám prímtényezőit
num = int(input("Adj meg egy pozitív egész számot!\n"))
primtenyezok = []
oszto = num
while oszto != 1:
    for i in range(2, oszto+1):
        if oszto % i == 0:
            primtenyezok.append(i)
            oszto //= i # // eredménye mindig egész típusú lesz
            break # kilépünk a for ciklusból (NEM a while-ból!)
print(f"A {num} prímtényezős felbontása: {primtenyezok}")

# 6. feladat: Toljunk el egy listát x értékkel jobbra/balra
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# balra toljuk 3-mal -> [4, 5, 6, 7, 8, 9, 10, 1, 2, 3]
# jobbra 2-vel -> [9, 10, 1, 2, 3, 4, 5, 6, 7, 8]
# jobbra 15-tel -> [6, 7, 8, 9, 10, 1, 2, 3, 4, 5] (5-tel jobbra)
amount = 26 # Mennyivel toljuk el?
direction = "balra" # jobbra/balra
amount = amount % len(lista)
if direction == "jobbra":
    lista = lista[-amount:] + lista[:-amount]
else:
    lista = lista[amount:] + lista[:amount]
print(lista)
    
# 7. feladat: 
lista = [34, 32, 2, 1, 4, 43, -23, -12, 32, 32, 0, 74, 12, 23, -12]
print(lista)
# Határozzuk meg a lista elemeinek az átlagát
összeg = 0
for item in lista:
    összeg += item
print(f"A lista elemeinek az átlaga: {round(összeg / len(lista), 2)}")

# Határozzuk meg a legnagyobb számot a listában
maximum = lista[0]
for item in lista:
    if item > maximum:
        maximum = item
print(f"A listában a {maximum} a legnyagyobb szám.")

# Hány negatív szám van a listában?
neg_számláló = 0
for item in lista:
    if item < 0:
        neg_számláló += 1
        
print(f"A negatív számok száma a listában: {neg_számláló}.")



