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
# a, Határozzuk meg a számok átlagát (for)
összeg = 0
for i in range(len(lista)):
    összeg += lista[i]
print(f"A számok átlaga: {round(összeg / len(lista), 2)}")

# b, Döntsük el, hogy van-e 11-el osztható szám a listában (while)
found_divisible = False
i = 0
while not found_divisible and i < len(lista):
    if lista[i] % 11 == 0:
        found_divisible = True
    i += 1

if found_divisible:
    print("Tartalmaz 11-el osztható számot.")
else:
    print("Nem tartalmaz 11-el osztható számot.")
    
    
def say_hi():
    print("Szia!")
    
say_hi()

def say_hi_to(name): # name paraméter definiáláskor PARAMÉTER-nek hívjuk
    print(f"Szia {name}!")

say_hi_to("András") # "András" a say_hi_to függvényhívás ARGUMENTUM-a
say_hi_to("Béla")
say_hi_to("Cecil")
say_hi_to("Dénes")

def say_time_hi_to(time, name):
    if time == 1:
        print(f"Jó reggelt {name}!")
    elif time == 2:
        print(f"Jó napot {name}!")
    elif time == 3:
        print(f"Jó estét {name}!")
    else:
        print(f"Szia {name}!")
        
say_time_hi_to(1, "András")
say_time_hi_to(2, "Béla")
say_time_hi_to(3, "Cecil")
say_time_hi_to([], "Dénes")
say_time_hi_to("cica", "Elemér")

# Írjunk egy függvényt ami paraméterben megkap egy állatot és kiírja, hogy:
# Olyan jó simogatni ezt a(z) <állat neve>-t!
def pet_animal(animal):
    vowels = "öüóűúőoiueaéáí"
    if animal[0] in vowels:
        print(f"Olyan jó simogatni ezt az {animal}-t!")
    else:
        print(f"Olyan jó simogatni ezt a {animal}-t!")
        
pet_animal("oroszlán")
pet_animal("kutya")
pet_animal("kígyó")

# Írjunk egy függvényt ami paraméterben megkap 1 számot és egy stringet és a függvény
# annyi alkalommal kiírja a stringet amennyi a szám értéke.

def print_n(n, string):
    for i in range(n):
        print(string)
        
print_n(5, "cica")
print_n(2, "A kutya fálmászott a fára a cica után.")