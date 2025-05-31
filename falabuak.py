print("1. feladat")
n = int(input("Fordulók száma: "))
print()

print("2. feladat")
golkulonbsegek = []
for i in range(1, n+1):
    gk = int(input(f"{i}. fordulóban a gólkülönbség: "))
    golkulonbsegek.append(gk)
print()

print("3. feladat")    
w_számláló = 0
l_számláló = 0
d_számláló = 0
for item in golkulonbsegek:
    if item > 0:
        w_számláló += 1
    elif item < 0:
        l_számláló += 1
    else:
        d_számláló += 1
print(f"A szezonban a csapatnak {w_számláló} győzelme, {l_számláló} veresége, {d_számláló} döntetlene volt.")
print()

print("4. feladat")
print(f"A csapatnak a szezonban összesen {w_számláló * 3 + d_számláló} pontja lett.")
print()

print("5. feladat")
if w_számláló > l_számláló + d_számláló:
    print("A csapatnak több győztes mérkőzése volt, mint veresége és döntetlene együttvéve.")
else:
    print("A csapatnak NEM volt több győztes mérkőzése, mint veresége és döntetlene együttvéve.")
print()
    
print("6. feladat")
elso_win_index = 0
for i in range(len(golkulonbsegek)):
    if golkulonbsegek[i] > 0:
        elso_win_index = i
        break
utolso_win_gk = golkulonbsegek[elso_win_index]
számláló = 0
for i in range(elso_win_index + 1, len(golkulonbsegek)):
    if golkulonbsegek[i] > utolso_win_gk:
        számláló += 1
    if golkulonbsegek[i] > 0:
        utolso_win_gk = golkulonbsegek[i]
print(f"A kitűzött célt {számláló} alkalommal sikerült elérnie a csapatnak.")
