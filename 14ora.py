# 1. feladat: Írjunk egy programot ami bekéri a felhasználó születési dátumát
# és kiszámolja, hogy hány napja született!

birthday = "1999-02-10"#input("Add meg a születési dátumod (pl.: 2000-01-01):\n")
today = [2025, 5, 24]
date = birthday.split("-") # ["2000", "01", "01"]
date[0] = int(date[0])
date[1] = int(date[1])
date[2] = int(date[2])

# Léptessük a napokat, addig amíg el nem érünk a mai dátumhoz

def is_leap_year(year):
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False

months = ["kutya", 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
days_counter = 0

while date != today:
    if date[2] == months[date[1]] or (date[1] == 2 and date[2] == 29):
        if date[1] == 2 and is_leap_year(date[0]) and date[2] == 28:
            date[2] = 29
        else:    
            date[2] = 1
            if date[1] == 12:
                date[1] = 1
                date[0] += 1
            else:
                date[1] += 1
    else: 
        date[2] += 1
    days_counter += 1

print(days_counter)


# 2. feladat: Döntsük el 2 stringről, hogy anargrammák-e!
# Két szöveg akkor anagramma, ha ugyan azokat a betűket tartalmazzák
# Amy - May

def is_anagramma(string1, string2):
    return sorted(string1.lower()) == sorted(string2.lower())
    
print(is_anagramma("Amy", "May"))
print(is_anagramma("Csoki", "Kocsi"))
print(is_anagramma("Auto", "Ajtó"))

# 3. feladat: Számoljuk meg, hogy hány autónak kell lelassítania!
# Ha egy auto előtt halad egy nála lasabb auto, akkor előbb utóbb utol fogja érni (lassítania kell)
cars = [59, 84, 38, 45, 67, 54, 49, 55, 67, 32, 48, 49, 55, 50, 67, 80, 75, 82, 90, 85, 99, 100]

számláló = 0
for i in range(0, len(cars)):
    for j in range(i + 1, len(cars)):
        if cars[i] > cars[j]:
            számláló += 1
            break
        
print(számláló, "autónak kell lassítania!")
# 4. feladat: Burger szavazás

burgers = ["Spicy Pinata", "Cheese Itz", "Tortuga", "Fatty Bottom", "Porkie Pie", "Conquistador"]
votes = [93456, 95344, 95678, 95845, 98744, 93412]

# Írjuk ki, hogy melyik burger nyerte a versenyt
maxi = 0
for i in range(1, len(votes)):
    if votes[i] > votes[maxi]:
        maxi = i
print(f"A legnépszerűbb burger: {burgers[maxi]}")

# Írjuk ki, hogy összesen hány szavazat érkezett
összeg = 0
for item in votes:
    összeg += item
print(f"Összesen {összeg} szavazat érkezett.")

# Írjuk ki a legkevesbé népszerű burgert
mini = 0
for i in range(1, len(votes)):
    if votes[mini] > votes[i]:
        mini = i
print(f"A legkevesebb szavazatot kapott burger: {burgers[mini]}")

# Írjuk ki, hogy melyik burger hány szavazatot kapott
for i in range(len(burgers)):
    print(f"{burgers[i]} - {votes[i]}")