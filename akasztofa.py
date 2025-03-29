import random
puzzles = ["lion king", "finding nemo", "despicable me", "monster university", "frozen", "rio", "walle", "incerdibles", "sponge bob", "tom and jerry", "turning red", "finding dory", "shrek", "how to train your dragon", "inside out", "asterix and obelix", "the little mermaid", "cinderella", "tangled", "phineas and ferb", "kim possible", "samurai jack", "johny bravo", "pocahontas"]

puzzle = puzzles[random.randrange(0, len(puzzles))]
my_solution = ""
for char in puzzle:
    if char == " ":
        my_solution += " "
    else:
        my_solution += "*"

life = 10
correct_letters = []
wrong_letters = []

while life > 0 and my_solution != puzzle: # Amíg tart a játék
    print(my_solution)
    tipp = input("Tippelj egy betűt, vagy add meg a megoldást!\n").lower()
    if len(tipp) == 0:
        continue # Ami a continue után jönne, az aktuális ciklus futásban, az kimarad és a következő ciklus iterációra ugrunk
    elif len(tipp) == 1:
        found = False
        for i in range(len(puzzle)):
            if puzzle[i] == tipp:
                found = True
                # Lista elemeit tudjuk módosítani, viszont string elemeket nem tudunk átítni (string[0] = f  NEM LEHET)
                lista = list(my_solution) # ["*", "*", "a", "*", " ", "*", "f", "*"]
                lista[i] = tipp
                my_solution = "".join(lista) # A my_solution legyen egyenlő a lista elemeivel "" (üres string)-el elválasztva "b*a* *f*"
        if found:
            correct_letters.append(tipp)
        else:
            wrong_letters.append(tipp)
            life -= 1
            print(f"{tipp} betű nem szerepel a feladványban, még {life} életed maradt.")
    else:
        if tipp == puzzle:
            print("Eltaláltad!")
            my_solution = tipp
        else:
            life -= 1
            print(f"Nem ez a megoldás! Még {life} életed maradt.")
    print("Kitalált betűk:", correct_letters)
    print("Elrontott betűk:", wrong_letters)
        

if life > 0:

    print(puzzle)
    print("Gratulálok, kitaláltad!")
else:
    print(f"Ez most nem jött össze. A megoldás ez volt: {puzzle}")


