#Operátorok (Műveletek) + - * >= = == and not or
#aritmetikai operátorok (+ - * /)

print(1 + 1)
print(7 - 2)
print(4 * 3)
print(12 / 5) # 2.4
print(2 ** 10) # hatványozás    2^10 = 1024
print(12 // 5) # maradék nélküli osztás, mindig egész számot eredményez -> 12 // 5 = 2
print(13 % 10) # maradékos osztás, megadja, hogy mennyi az osztás után a maradék (3)

# értékadó operátor

num = 10 # = egy operátor
print(num)
num += 5 # num értéhez hozzáad 5-öt
print(num)
num *= 2 # numot megszorozza 2-vel
print(num)
num **= 3 # a numot emeljük a 3. hatványra
print(num)
num //= 10
print(num)
num /= 10
print(num)

# Összehasonlító operátorok (==, !=,  >, <, >=, <=)
if (10 == 5 + 5):
    print("igaz 1")
if (60 != 6 + 0):
    print("igaz 2")
if (70 > 11):
    print("igaz 3")
    
# Logikai operátorok (and, or, not)
esik_az_eso = False
fuj_a_szel = True
sut_a_nap = True
if (not esik_az_eso):
    print("Száraz az idő")

if fuj_a_szel and sut_a_nap:
    print("Fúj a szél és süt is a nap")
    
if esik_az_eso or fuj_a_szel:
    print("Hűvös van")
    
# for ciklus
# pythonban a for ciklus foreach működik (a ciklus változó egy lista elemeit veszi fel)
lista = [9, 10, 7, 3]
for i in lista:
    print(i, end = " ")
print() # ugyanúgy rak egy entert a végére

lista = [0,1,2,3,4,5,6,7,8,9]
for i in lista:
    print(i, end = " ")
print()

for i in range(10): # i = 0, 1, 2, ..., 7, 8, 9    A 10 MÁR NINCS BENNE! range(10) = [0,1,2,3,4,5,6,7,8,9] 
    print(i, end = " ")
print()

for i in range(23, 40): # i = 23, 24, 25, ..., 38, 39       A 40 már nincs benne
    print(i, end = " ")
print()

for i in range(40, 2080, 120): # i = 40, 160, 280, ..., 1840, 1960
    print(i, end = " ")
print()

# 1. feladat: Írjuk ki a számokat 0-tól 15-ig
for i in range(16):
    print(i, end = " ")
print()

# 2. feladat: Írjuk ki a számokat -20-tól -5-ig
for i in range(-20, -4):
    print(i, end = " ")
print()

# 3. feladat: Írjuk ki az alábbi sorozatot: 10, 15, 20, 25, ..., 55
for i in range(10, 60, 5):
    print(i, end = " ")
print()

# 4. feladat: Írjuk ki a számokat 22-től, 4-ig:  22, 21, 20, ..., 6, 5, 4
for i in range(22, 3, -1):
    print(i, end = " ")
print()

# Elől tesztelős ciklus (while ciklus)
# Addig ismétel, amíg a feltétele igaz

i = 0
while i < 10:
    print(i, end = " ")
    i += 1
print()


lista = []
bemenet = "kilép"
while bemenet != "kilép":
    bemenet = input("Írj valamit: ")
    lista.append(bemenet)
print(lista)


num = 5
while num != 1:
    num -= 1
    print(num, end=" ")
print()
# 1. feladat: Olvassunk be egy számot és írjuk ki annyiszot, hogy "banán", amennyit beírt a felhasználó
num = int(input("Adj meg egy egész számot: "))
for i in range(num):
    print("banán", end = " ")
print()

print("banán " * num)
# 2. feladat: Olvassunk be folyamatosan számokat, és tároljuk el egy listába, egészen addig, amíg
# a felhasználó egy 10-el osztható számot ad meg
num = 5
lista = []
while (num % 10 != 0):
    num = int(input("Adj meg egy egész számot: "))
    lista.append(num)
print(lista)

# 3. feladat: Olvassunk be egy számot és határozzuk meg az osztóit
num = int(input("Adj meg egy egész számot!\n"))
print(num, "osztói:", end= " ")
for i in range(1, num + 1):
    if num % i == 0:
        print(i, end = " ")
        
# feladat: prímszám-e

num = int(input("Adj meg egy egész számot!\n"))
isPrime = True
for i in range(2, num):
    if num % i == 0:
        isPrime = False
print(isPrime)