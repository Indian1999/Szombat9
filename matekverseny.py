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

maxi = 0
for i in range(1, len(pontok)):
    if pontok[i] > pontok[maxi]:
        maxi = i
print(f"A verseny nyertese {nevek[maxi]}, aki {pontok[maxi]} pontot ért el.")

# 5. feladat: Hány olyan versenyző volt, aki kerek pontszámot ért el?
# (0, 5, 10, 15, 20, 25, ..., 90, 95, 100)

számláló = 0
for item in pontok:
    if item % 5 == 0:
        számláló += 1
print(f"{számláló} versenyző ért el kerek pontszámot.")

# 6. feladat: Kérjünk be egy pontszámot a felhasználótól és írjuk ki, hogy
# kik azok akik ezalatt a pontszám alatt teljesítettek

határ = int(input("Adj meg egy pontszámot: "))
print("Akik nem értek el ennyi pontot:")
for i in range(len(pontok)):
    if határ > pontok[i]:
        print(f"{nevek[i]} - {pontok[i]} pont")

# 7. feladat: Hány pontszámot ért el Csaba, ha nem volt ilyen nevű versenyző,
# akkor írjuk ki hogy nem volt Csaba

csaba_index = -1
for i in range(len(nevek)):
    if nevek[i] == "Csaba":
        csaba_index = i
        break # kilép a ciklusból
    
if csaba_index == -1:
    print("Nem volt Csaba nevű versenyző.")
else:
    print(f"Csaba {pontok[csaba_index]} pontot ért el.")
