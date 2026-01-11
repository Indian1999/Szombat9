import os

path = __file__
print(path) # c:\Users\Meggyecske\Desktop\Szombat9\2. félév\fajlkezeles.py
path = os.path.dirname(path)
print(path) # c:\Users\Meggyecske\Desktop\Szombat9\2. félév
path = os.path.join(path, "bemenetek")
print(path) # c:\Users\Meggyecske\Desktop\Szombat9\2. félév\bemenetek

path_homerseklet = os.path.join(path, "homerseklet.txt")

file = open(path_homerseklet, "r", encoding="utf-8")

print(file.read(15)) # Beolvas 15 karaktert
print(file.read(10))
file.seek(0) # AZ olvasófejet a 0. karakterre viszi
print(file.read(10))

file.close()

# Ehelyett: Context manager

with open(path_homerseklet, "r", encoding="utf-8") as f:
   print(f.readlines())

homersekletek = []
with open(path_homerseklet, "r", encoding="utf-8") as f:
   sor = f.readline()
   while sor != "":
      sor = sor.strip() # whitespace karaktereket leszedi az elejéről és a végéről
      sor = sor.split(";")
      sor = [int(item) for item in sor]
      homersekletek.append(sor)
      sor = f.readline()
    
with open(path_homerseklet, "r", encoding="utf-8") as f:
    for sor in f:
       print([sor])

# Feladat: Olvassuk be és tároljuk el egy megfelelő adatszerkezetben a pontok.txt
# fájl tartalmát
# Két pont távolsága: ((x1-x2)**2 + (y1-y2)**2 + (z1-z2)**2) ** 0.5
pontok = []
with open(os.path.join(path, "pontok.txt"), "r", encoding="utf-8") as f:
   for line in f:
      line = line.strip().split(",")
      line = [int(item) for item in line]
      pontok.append(line)

# a, Írjuk ki azt a pontot amelyik a legtávolabb van az origótól (0,0,0)
max = (pontok[0][0]**2 + pontok[0][1]**2 + pontok[0][2]**2) ** 0.5
max_index = 0
for i in range(1, len(pontok)):
   pont = pontok[i]
   tavolsag = (pont[0]**2 + pont[1]**2 + pont[2]**2) ** 0.5
   if tavolsag > max:
      max = tavolsag
      max_index = i

print(f"Az origótól legtávolabbi pont a {pontok[max_index]}, {round(max,2)} egység távolságra van az origótól.")

# b, Írjuk ki azt a 2 pontot amelyek a legközelebb vannak egymáshoz
def distance(pont1, pont2):
    return ((pont1[0] -  pont2[0])**2 + (pont1[1]-pont2[1])**2 + (pont1[2]-pont2[2])**2) ** 0.5

min_i = 0
min_j = 1
min = distance(pontok[0], pontok[1])
for i in range(len(pontok) - 1):
    for j in range(i+1, len(pontok)):
        tavolsag = distance(pontok[i], pontok[j])
        if tavolsag < min:
            min = tavolsag
            min_i = i
            min_j = j

print(f"Az egymáshoz legközelebb lévő két pont a: {pontok[min_i]} és {pontok[min_j]}, {round(min,2)} egység távolságra vannak egymástól.")

path_kimenetek = os.path.join(os.path.dirname(__file__), "kimenetek")

with open(os.path.join(path_kimenetek, "pontok_kimenet.txt"), "w", encoding="utf-8") as f:
    f.write(f"Az origótól legtávolabbi pont a {pontok[max_index]}, {round(max,2)} egység távolságra van az origótól.\n")
    f.write(f"Az egymáshoz legközelebb lévő két pont a: {pontok[min_i]} és {pontok[min_j]}, {round(min,2)} egység távolságra vannak egymástól.\n")

# Ha már létezik a fájl amikor 'w' módban megynitom, akkor törli a tartalmát.
# Ha ezt el szeretnénk kerülni, használjunk 'a' (append) módot
with open(os.path.join(path_kimenetek, "pontok_kimenet.txt"), "a", encoding="utf-8") as f:
    f.write("Ide írok még valamit...\n")

# Módok:
# 'r' (read):   olvasó mód
# 'w' (write):  író mód, törli a fájl addigi tartalmát
# 'a' (append): író mód, de nem törli a fájl addigi tartalmát
      
      
