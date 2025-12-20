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
