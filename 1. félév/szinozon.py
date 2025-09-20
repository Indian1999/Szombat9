import random

def generate_puzzle():
    puzzle = ""
    while len(puzzle) < 4:
        num = random.randint(1,8) # 8 különböző "szín" lehetséges
        if str(num) not in puzzle:
            puzzle += str(num)
    return puzzle

puzzle = generate_puzzle() # pl.: 5723
gameOn = True
tippek_szama = 0

while gameOn:
    tipp = input("Adj meg 4 1-8 közötti számjegyet (pl.: 1234)!\n")
    jo_szamok = 0
    jo_szamok_jo_helyen = 0
    for i in range(len(tipp)):
        if tipp[i] == puzzle[i]:
            jo_szamok_jo_helyen += 1
        elif tipp[i] in puzzle:
            jo_szamok += 1
    tippek_szama += 1
    if tipp == puzzle:
        gameOn = False
    else:
        print(f"Jó számok jó helyen: {jo_szamok_jo_helyen}")
        print(f"Jó számok, de nem jó helyen: {jo_szamok}")

print(f"Szép volt! {tippek_szama} lépésből kitaláltad, hogy a megoldás {puzzle} volt.")