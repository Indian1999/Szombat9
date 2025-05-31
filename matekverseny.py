# 1. feladat: Olvassuk be, hogy hány versenzyő eredményeit akarjuk beolvasni

n = int(input("Add meg a versenyzők számát: "))

# 2. feladat: Olvassunk be ennyi eredményt, elösször a versenzyző nevét,
# utána az általa elért pontszámot (0-100). Tároljuk is el!

nevek = []
pontok = []
for i in range(n):
    név = input(f"{i+1}. versenyző neve: ")
    pont = int(input(f"{i+1}. versenyző pontszáma: "))
    nevek.append(név)
    pontok.append(pont)

# 3. feladat: Határozzuk meg a versenyzők átlagos pontszámát

összeg = 0
for item in pontok:
    összeg += item
print("A pontszámok átlaga:", round(összeg / len(pontok)))
#print("A pontszámok átalag:", sum(pontok) / len(pontok))

# 4. feladat: Írjuk ki, hogy ki nyerte a versenyt és hogy hány pontot ért el



# 5. feladat: Hány olyan versenyző volt, aki kerek pontszámot ért el?
# (0, 5, 10, 15, 20, 25, ..., 90, 95, 100)

# 6. feladat: Kérjünk be egy pontszámot a felhasználótól és írjuk ki, hogy
# kik azok akik ezalatt a pontszám alatt teljesítettek

# 7. feladat: Hány pontszámot ért el Csaba, ha nem volt ilyen nevű versenyző,
# akkor írjuk ki hogy nem volt Csaba