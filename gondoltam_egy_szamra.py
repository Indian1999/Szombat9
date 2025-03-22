import random   # olyan mint a using c# ban

gameRunning = True

while gameRunning:
    num = random.randint(1, 100)
    guess = 0 # Ebbe tároljuk el a játékos által tippelt számot
    guessCount = 0
    while guess != num and guessCount < 7:
        guess = int(input(f"Tippelj egy számot 1 és 100 között! (Még {7-guessCount} tipped van hátra)\n"))
        guessCount += 1
        if guess > num:
            print("Ettől egy kisebb számra gondoltam!")
        elif guess < num:
            print("Ettől nagyobb számra gondoltam!")
    if guess == num:
        print(f"Gratulálok! Sikeresen kitaláltad {guessCount} lépésből, hogy erre gondoltam: {num}.")
    else:
        print(f"Sajnos ez most nem jött össze😿, a szám amire gondoltam ez volt: {num}")
    
    ans = input("Szeretnél még egyet játszani? (igen/nem)\n")
    if ans == "nem":
        gameRunning = False
        
    
