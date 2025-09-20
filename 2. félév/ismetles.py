# 1. feladat: Olvassunk be egy számot és írjunk ki annyi #-t

n = int(input("Adj meg egy számot: "))

for i in range(n):
    print("#", end="")
    
print()
print("#" * n)

# 2. feladat: Olvassuk be egy háromszög 3 oldalának a hosszát és döntsük el, 
# hogy létezhet-e ilyen háromszög!
# Bármely két oldal összege legyen nagyobb a 3. oldalnál

a = float(input("Add meg az a oldal hosszát: "))
b = float(input("Add meg a b oldal hosszát: "))
c = float(input("Add meg a c oldal hosszát: "))

if a + b > c and a + c > b and b + c > a:
    print("Ilyen háromszög létezik.")
else:
    print("Nem létezik ilyen háromszög.")
    
