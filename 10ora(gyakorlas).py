# 1. feladatban egy kilogrammban megadott értéket váltsunk át grammba
kg = 6 # int(input("Adj meg egy kilogramm értéket!\n"))
print(f"{kg} kg = {kg * 1000} g")
# b, g -> kg
g = 4362
print(f"{g} g = {g / 1000} kg")
# 2. feladatban Egy program ami °F - °C átváltás
# F = 1.8 * C + 32
# C = (F - 32 ) / 1.8
fahrenheit = 65
print(f"{fahrenheit} °F = {round( (fahrenheit - 32) / 1.8 )} °C")

celsius = 32
print(f"{celsius} °C = {round(1.8*celsius + 32)} °F")

# 3. feladat: mérföld - km   1 km = 0.62137 mi
km = 5
print(f"{km} km = {round(km * 0.62137, 2)} mi")

mi = 5
print(f"{mi} mi = {round(mi / 0.62137, 2)} km")

# 4. feladat: Nézzük a számokat 1-75-ig
# Ha egy szám osztható 3 mal, írjuk ki, hogy bim
# Ha egy számban szerepel a 3-mas számjegy, írjuk ki, hogy bam
# Ha mindkettő teljesül, írjuk ki, hogy bimbam

for i in range(1, 76):
    if i % 3 == 0 and "3" in str(i):
        print(i, "bimbam")
    elif i % 3 == 0:
        print(i, "bim")
    elif "3" in str(i):
        print(i, "bam")

# 5. feladat: Ellenőrizzük, hogy egy jelszó elég erős-e
# A hossza 6 és 16 karakter között van
# Van benne kis és nagy betű      string.islower()    string.isupper()
# Van benne szám                  string.isdigit()
# Van benne speciális karakter (&@.! stb.)  special_chars = "@{}.,;!+-<>#"   char in special_chars
password = "asdASd32."
correct_length = len(password) >= 6 and len(password) <= 16
hasLower = False        # pipa
hasUpper = False        # pipa
hasDigit = False        # pipa
hasSpecial = False
special_chars = "<>#&@{}!+-=/_*?;,[]()"
for char in password:
    if char.islower():
        hasLower = True
    if char.isupper():
        hasUpper = True
    if char.isdigit():
        hasDigit = True
    if char in special_chars:
        hasSpecial = True
        
if hasSpecial and hasUpper and hasLower and correct_length and hasDigit:
    print("A jelszó elég erős")
else:
    if not hasDigit:
        print("A jelszónak tartalmazni kell legalább 1 számjegyet!")
    if not hasLower:
        print("A jelszónak tartalmazni kell legalább 1 kisbetűt!")
    if not hasUpper:
        print("A jelszónak tartalmazni kell legalább 1 nagybetűt!")
    if not hasDigit:
        print("A jelszónak tartalmazni kell legalább 1 speciális karaktert!")
    if not correct_length:
        print("A jelszó hosszának 6 és 16 karakter közöttinek kell lennie!")
# 6. feladat: Adottak egy háromszög 3 oldalának hosszai
# Határozzuk meg, hogy a háromszög létezik-e? (szerkeszthető)
    # Bármely két oldal hosszának összege, legyen nagyobb a 3. oldal hoszsánál
    # a + b > c és a + c > b és b + c > a
# Ha derékszögű, írjuk ki hogy derékszögű  (pitagorasz: a^2 + b^2 = c^2)
# Ha egyenlő szárú vagy szabályos azt is írjuk ki
a = 3
b = 3
c = 3
if a + b > c and a + c > b and b + c > a: # szerkeszthető-e
    if a ** 2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
        print("Derékszögű háromszög")
    if a == b and b == c:
        print("Szabályos háromszög")
    if a == b or a == c or b == c:
        print("Egyenlő szárú háromszög")
else:
    print("Ilyen háromszög nem létezik!")