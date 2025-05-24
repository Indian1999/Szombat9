# 1. feladat: Írjunk egy programot ami bekéri a felhasználó születési dátumát
# és kiszámolja, hogy hány napja született!

birthday = input("Add meg a születési dátumod (pl.: 2000-01-01):\n")
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