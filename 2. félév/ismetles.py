# 1. feladat: Olvassunk be egy számot és írjunk ki annyi #-t

#n = int(input("Adj meg egy számot: "))
n = 2
for i in range(n):
    print("#", end="")
    
print()
print("#" * n)

# 2. feladat: Olvassuk be egy háromszög 3 oldalának a hosszát és döntsük el, 
# hogy létezhet-e ilyen háromszög!
# Bármely két oldal összege legyen nagyobb a 3. oldalnál

#a = float(input("Add meg az a oldal hosszát: "))
#b = float(input("Add meg a b oldal hosszát: "))
#c = float(input("Add meg a c oldal hosszát: "))
a, b,c = 1,1,1
if a + b > c and a + c > b and b + c > a:
    print("Ilyen háromszög létezik.")
else:
    print("Nem létezik ilyen háromszög.")
    
import random
# 3. feladat: Adott egy egész számokat tartalmazó lista
lista = [random.randint(-20, 20) for i in range(15)]
print(lista)
# a, Határozzuk meg a számok átlagát
# b, Döntsük el, hogy van-e 11-el osztható szám a listában