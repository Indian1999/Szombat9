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

# 3. feladat: mérföld - km   1 km = 0.62137 mi

# 4. feladat: Nézzük a számokat 1-75-ig
# Ha egy szám osztható 3 mal, írjuk ki, hogy bim
# Ha egy számban szerepel a 3-mas számjegy, írjuk ki, hogy bam
# Ha mindkettő teljesül, írjuk ki, hogy bimbam

# 5. feladat: Ellenőrizzük, hogy egy jelszó elég erős-e
# A hossza 6 és 16 karakter között van
# Van benne kis és nagy betű      string.islower()    string.isupper()
# Van benne szám                  string.isdigit()
# Van benne speciális karakter (&@.! stb.)  special_chars = "@{}.,;!+-<>#"   char in special_chars

# 6. feladat: Adottak egy háromszög 3 oldalának hosszai
# Határozzuk meg, hogy a háromszög létezik-e? (szerkeszthető)
    # Bármely két oldal hosszának összege, legyen nagyobb a 3. oldal hoszsánál
    # a + b > c és a + c > b és b + c > a
# Ha derékszögű, írjuk ki hogy derékszögű  (pitagorasz: a^2 + b^2 = c^2)
# Ha egyenlő szárú vagy szabályos azt is írjuk ki
a = 3
b = 4
c = 5