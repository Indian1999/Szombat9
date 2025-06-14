gameOn = True
chances = 3 # 3 próbálkozásunk van a kód kitalálására
win = False
solution = "4686"
rooms = []
items = []


print("""Üdvözöllek a szabadulószobában! 14 ajtót látsz magad előtt, ezek közül az egyik
rejti a szabadságod kapuját! Találd ki a 4 számjegyű kódot, amivel ki
tudsz jutni innen! Sok sikert!
""")
while gameOn:
    room_number = input("Melyik szobába szeretnél bemenni? (0-13, -1)\n")
    if room_number == "-1":
        print("A történeted idáig:")
        for i in range(len(rooms)):
            print(f"{rooms[i]}. szoba: {items[i]}")
    if room_number == "0":
        pass
    if room_number == "1":
        pass
    if room_number == "2":
        pass
    if room_number == "3":
        print("""Ebben a szobában egy videó van kivetítve a falra, amin az látszik ahogy egy cicaeszik a
táljából. Többszörös újranézés után meglátod, hogy táljára egy 2-es számjegy van írva""")
        if room_number not in rooms:
            rooms.append(room_number)
            items.append("cica eszik a 2-es tálból")
    if room_number == "4":
        pass
    if room_number == "5": # x = 10111 - 10001    23 - 17 = 6
        print("Egy egyenlet van a falon: x = 10111 - 10001")
        print("Biztosan az x lesz az egyik számjegy...")
        if room_number not in rooms:
            rooms.append(room_number)
            items.append("x = 10111 - 10001")
    if room_number == "6":
        pass
    if room_number == "7":
        pass
    if room_number == "8":
        print("""A szobába belépve azt látod, hogy egy bohóc ül egy székben  és
3 db színes lufit tart a kezében.""")
        if room_number not in rooms:
            rooms.append(room_number)
            items.append("bohóc 3 lufival")
    if room_number == "9": # binárból decimálsba
        print("""Egy cetlit találsz a szobában, amira az van írva, hogy
binárisból decimálisba. Ez az info még biztosan hasznos lesz...""")
        if room_number not in rooms:
            items.append("binárisból decimálisba")
            rooms.append(room_number)
    if room_number == "10":
        pass
    if room_number == "11":
        print("""Itt egy festményt találsz amin az látható ahogy 2 bohóc kerget egy cicát.""")
        if room_number not in rooms:
            rooms.append(room_number)
            items.append("festmény - 2 bohóc kerget egy cicát")
    if room_number == "12":
        pass
    if room_number == "13":
        pass
    
    
if win:
    print("Kijutottál! Gratulálok!")
else:
    print("Ez most nem jött össze...")