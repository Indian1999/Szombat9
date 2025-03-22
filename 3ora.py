my_name = "Miklos"
print("My name is " + my_name)

#TypeError: can only concatenate str (not "int") to str
#(stringhez, csak stringet tudunk hozzáadni)
my_age = 26
print("I am " + str(my_age) + " years old.")
print("I am", my_age, "years old.")
print(f"I am {my_age} years old.")

pet_name = "Bundás"
pet_age = 11
pet_species = "dog"

print("My first dog was named " + pet_name + " he was " +
      str(pet_age) + " old. And he was a " + pet_species)

print("My name is %s" %my_name)
print("I am %d years old." %my_age)
print("Hello! My name is %s. I am %d years old. I have a %s named %s. He is %d years old."
      %(my_name, my_age, pet_species, pet_name, pet_age) )


player_name = "Marduk"
player_level = 53
player_class = "Monk"
player_isPvpEnabled = False
player_isOnline = True

if player_isOnline:
    print("The player is online.")
else:
    print("The player is offline.")

if player_isPvpEnabled:
    print("Attack Pistike...")

if player_level >= 60:
    print("You can equip a new sword.")
else:
    print("Your level is too low for this sword.")

if player_class == "Monk":
    print("You can enter the temple.")
else:
    print("You shall not pass!")


első_szám = 8
második_szám = 9
if első_szám > második_szám:
    print("Az első szám a nagyobb")
elif második_szám > első_szám:
    print("A második szám a nagyobb")
else:
    print("A két szám egyenlő")

# 91-100: 5
# 77-90:  4
# 63-76:  3
# 50-62:  2
#  0-49:  1
pontszám = int(input("Add meg a dolgozatod pontszámát!\n"))
if pontszám >= 91:
    print("5-ös!")
elif pontszám >= 77:
    print("4-es!")
elif pontszám >= 63:
    print("3-as!")
elif pontszám >= 50:
    print("2-es!")
else:
    print("1-es!")

if 5 > pontszám and 3 < pontszám:
    pass

if 5 > pontszám or 3 < pontszám:
    pass

if not 5 > pontszám:
    pass
# Legyen adott 3 szám (a,b,c) ez a három szám egy háromszög oldalainak a hossza
# (and, or, not)
a = 4
b = 4
c = 4
# 1. feladat: Létezik a háromszög?
# Akkor létezik, ha bármely 2 oldal hosszának összege nagyobb a harmadik
# oldal hosszánál
if a + b > c and a + c > b and b + c > a:
    print("Létezik a háromszög")
else:
    print("Nem létezik a háromszög")
# 2. feladat: Szabáloys háromszög?
if a == b and b == c:
    print("Szabályos háromszög")
# 3. feladat: Egyenlő szárú?
if a == b or b == c or a == c:
    print("Egyenlő szárú")
# 4. feladat: Derékszögű? a**2 + b**2 = c**2
if a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
    print("Derékszögű háromszög")
else:
    print("Nem derékszögű")
# 5. feladat: Írjuk ki a legnagyobb számot!
if a >= b and a >= c:
    print("Legnagyobb:", a)
elif b >= a and b >= c:
    print("Legnagyobb:", b)
else:
    print("Legnagyobb:", c)
# 6. feladat: Írjuk ki a legkisebb számot!
if a <= b and a <= c:
    print("Legkisebb:", a)
elif b <= a and b <= c:
    print("Legkisebb:", b)
else:
    print("Legkisebb:", c)

#C#-ban foreach
# Az i változó egy lista elemeit veszi fel szépen sorban
for i in range(10): # range(10) = [0,1,2,3,4,5,6,7,8,9]
    print("Hello szia", i)

for i in [1,2,3, "négy", "öt", "háromszorkettő"]:
    print(i)

for i in range(5, 10): # [5, 6, 7, 8, 9]
    print("i =", i)

for i in range(0, 1800, 100):
    print(i)

for i in range(2000, -3000, -500):
    print(i, end=" ")
print()






