szöveg = "A a fekete kiskutya átsétált az úton, hogy megegye a finom illatú szalámit."
print(szöveg)
print("A szöveg karaktereinek a száma:", len(szöveg))
print("Az első 't' betű indexe a stringben:", szöveg.find("t"))
print("Az első 'ty' betű a szövegben:", szöveg.find("ty"))

szöveg_darabonként = szöveg.split(" ") # szóközek mentén feldarabolj a szöveget
print(szöveg_darabonként)

szöveg_senként = szöveg.split("s")
print(szöveg_senként)

hosszú_szöveg = """A három idézőjeles
megoldás azért jó, mert
így könnyen tudok több
soros stringeket
írogatni anélkül, hogy
különleges karaktereket
kellene használnom."""

print(hosszú_szöveg)
szöveg_soronként = hosszú_szöveg.split("\n") # alt gr + Q -> \
print(szöveg_soronként)

szó = "kUtYa"
print(szó.lower()) # kisbetűssé alakítja
print(szó.upper()) # nagybetűssé alakítja
print(szó.capitalize()) # Az első betűt teszi nagybetűssé a többit kicsivé

print("a kutya és a cica története".title()) # A Kutya És A Cica Története

szöveg = "A a fekete kiskutya átsétált az úton, hogy megegye a finom illatú szalámit."

print(szöveg)
print("A szövegben található szavak száma:", szöveg.count(" ") + 1)
print("Az 'a' betűk száma a szövegben:", szöveg.lower().count("a"))
"""
# alt gr + Q -> \
tárgy1 = input("Adj meg egy tárgyat:\n")
tárgy2 = input("Adj meg még egy tárgyat:\n")
tulajdonság = input("Kérek egy tulajdonságot!\n")
zene = input("Add meg egy zene címét!\n")
híresség = input("Adj meg egy híres embert:\n")
érzés = input("Mondj egy érzést:\n")
ige = input("Kérek egy igét!\n")
hely = input("Adj meg egy helyet:\n")
étel = input("Mondj egy ételt:\n")
ember = input("Kérek egy nevet/embert\n")

print(f""""""
Most értem vissza {ember} pizza partyjáról.
El sem hinnéd, {tulajdonság} pizzát ettünk {hely}-ban
Mindenki kiválaszthatta, hogy milyen feltéteket szeretne a saját pizzájára.
Én '{étel} és {tárgy1}' pizzát választottam, mert az a kedvencem!
Még a széleit is megtöltötték {tárgy2}-vel! {érzés.capitalize()}!
És ha ez mind nem volna elég, még {híresség} is ott volt és a {zene}-t
énekelte. Annyira meginspirált a zene, hogy felkeltem a székemből és elkezdtem {ige}.
"""""")"""


a = int(input("Adj meg egy számot!\n"))
b = int(input("Adj meg még egy számot!\n"))

print(f"{a} + {b} = {a + b}")
print(f"{a} - {b} = {a - b}")
print(f"{b} - {a} = {b - a}")
print(f"{a} * {b} = {a * b}")
print(f"{a} / {b} = {round(a / b, 2)}")
print(f"{b} / {a} = {round(b / a, 2)}")
print(f"{a} % {b} = {a % b}")
print(f"{b} % {a} = {b % a}")
print(f"{a} // {b} = {a // b}") # Csak az egész eredményt nézi: 7 // 3 = 2
print(f"{b} // {a} = {b // a}")
print(f"{a} ** {b} = {a ** b}") # Hatványozás 2**10 = 2^10 = 1024
print(f"{b} ** {a} = {b ** a}")
print(f"2 * {a} - {b} ** 2 = {2 * a - b ** 2}")

lista = []
lista = [6, 5, 4]
lista.append(6)
lista[0]
# 1. feladat: Olvassuk be egy kör sugarát! Ebből számoljuk ki és írjuk ki a kerületét
#             és a területét   (K = 2*pi*sugár      T = pi*sugár*sugár       pi = 3.14)
sugár = float(input("Add meg a kör sugarát: "))
kerület = 2 * 3.14 * sugár
terület = 3.14 * sugár * sugár
print(f"K = {kerület}, T = {terület}")

# 2. feladat: Olvass be egy szöveget, majd írd ki, hogy hány darab 'k' betű van benne
szöveg = input("Adj meg egy szöveget!\n")
print(szöveg.lower().count("k"))

# 3. feladat: Olvassunk be három számot (ezek egy háromszög oldalainak a hossza), döntsük el,
#             hogy létezik-e a háromszög! (Ahhoz hogy létezhessen a háromszög, az kell, hogy
#             bármely 2 oldal hosszának összege, legyen nagyobb a 3. oldal hosszánál)
#               (a + b) > c és (a + c) > b és (b + c) > a

a = float(input("Add meg az 1. oldalt: "))
b = float(input("Add meg a 2. oldalt: "))
c = float(input("Add meg a 3. oldalt: "))

if a + b > c and a + c > b and b + c > a:
    print("Létezik a háromszög")
else:
    print("Ilyen háromszög nem létezik")



