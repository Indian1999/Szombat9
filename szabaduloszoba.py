gameOn = True
chances = 3 # 3 próbálkozásunk van a kód kitalálására
win = False
solution = "4686"
rooms = []
items = []
switches = "0000000"
correct_switches = "1010011"

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
        if room_number not in rooms:
            rooms.append(room_number)
            items.append("kulcs")
            print("""A szobában nincs semmi, csak nagyon fényesen világít egy villanykörte. úgy látod mintha lenne benne
valami, ezért összetöröd és mostmár kukk sötét van. A szilánkok között tapogatózva megvágod
egy picit a kezed, de rátalálsz egy kulcsra. Még biztos jól fog jönni a későbbiekben...""")
            if "lezárt doboz" in items:
                rooms.append(room_number)
                items.append("hús")
                print("A kulcs pont illeszkedik a lezárt dobozba. Kinyitod és egy szelet húst találsz benne.")
        else:
            print("A szoba még mindig kukk sötét.")
    if room_number == "1":
        print("""Egy mesekönyvet találsz, amiben a következő kis rövid történetet olvasod:
    Egyszer volt, hol nem volt, élt egyszer egy Leo nevű oroszlán, aki nagyon szeretett egyenleteket oldani.
Ebben mindig segítségére volt legjobb barátja Cirmi, a bohóc cica. Időről időre előfordult,
hogy Leo nem tudott rájönni a megoldásra, de ilyenkor Cirmi feje fölött mindig felvillant egy villanykörte.
Boldog éltek, míg meg nem haltak.
Elég fura történet...""")
        if room_number not in rooms:
            rooms.append(room_number)
            items.append("mesekönyv")
    if room_number == "2":
        print(f"A falra 7 számjegy van felfestve: {correct_switches}")
        if room_number not in rooms:
            rooms.append(room_number)
            items.append(f"számok a falon - {correct_switches}")
    if room_number == "3":
        print("""Ebben a szobában egy videó van kivetítve a falra, amin az látszik ahogy egy cicaeszik a
táljából. Többszörös újranézés után meglátod, hogy táljára egy 2-es számjegy van írva""")
        if room_number not in rooms:
            rooms.append(room_number)
            items.append("cica eszik a 2-es tálból")
    if room_number == "4":
        print("Ebben a szobában egy tábla van, amire villanykörték vannak erősítve.")
        if room_number not in rooms:
            rooms.append(room_number)
            items.append("tábla villanykörtékkel")
        if switches == correct_switches:
            print("Olyan mintha a villanykörték egy 6-os számjegyet rajzolnának ki.")
            if "6-os villanykörték" not in items:
                rooms.append(room_number)
                items.append("6-os villanykörték")
    if room_number == "5": # x = 10111 - 10001    23 - 17 = 6
        print("Egy egyenlet van a falon: x = 10111 - 10001")
        print("Biztosan az x lesz az egyik számjegy...")
        if room_number not in rooms:
            rooms.append(room_number)
            items.append("x = 10111 - 10001")
    if room_number == "6":
        if room_number not in rooms:
            rooms.append(room_number)
            items.append("oroszlán")
            print("Uram Isten! Egy oroszlán van a szobában! Úgy néz ki, mintha nagyon őrizne valamit.")
        else:
            print("Még mindig itt az oroszlán.")
        akció = input("Megpróbálod elterelni az oroszlán figyelmét, hogy lásd mit őriz? (igen/nem)\n")
        if akció == "igen":
            if "hús" in items:
                print("A sarokba dobod a szelet húst amit találtál, az oroszlán pedig utána ered.")
                print("Az oroszlán egy ezüst serleget védelmezett amire egy 4-es számjegy van írva.")
                rooms.append(room_number)
                items.append("4-es ezüst serleg")
            else:
                print("Megpróbálod elterelni a figyelmét, de csak rádtámad és te meghalsz.")
                gameOn = False
        else:
            print("Majd legközelebb...")
    if room_number == "7":
        if room_number not in rooms:
            rooms.append(room_number)
            items.append("balta")
            print("A szobába belépve egy baltát látsz a falnakj támasztva. Tuti jól fog még jönni...")
        else:
            print("A szoba kong az ürességtől.")
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
        if room_number not in rooms:
            rooms.append(room_number)
            items.append("kijárat")
        print("Itt található a kijárat a szabadulószobából, viszont egy 4-számjegyű kombinációs lakat védi.")
        print(f"Vigyázz, mert összesen csak {chances} alkalommal próbálkozhatsz!")
        akció = input("Megpróbálod beütni a számjegyeket? (igen/nem)\n")
        if akció == "igen":
            tipp = input("Add meg a 4 számjegyet (pl.: 1234): ")
            if tipp == solution:
                gameOn = False
                win = True
            else:
                chances -= 1
                print(f"Helytelen kód! Még {chances} próbálkozásod maradt!")
                if chances == 0:
                    gameOn = False
        else:
            print("Majd viszajössz később...")
    if room_number == "11":
        print("""Itt egy festményt találsz amin az látható ahogy 2 bohóc kerget egy cicát.""")
        if room_number not in rooms:
            rooms.append(room_number)
            items.append("festmény - 2 bohóc kerget egy cicát")
    if room_number == "12":
        print("7 darab kapcsolót látsz a falon, de látszólag semmit nem csinálnak.")
        if room_number not in rooms:
            rooms.append(room_number)
            items.append("7 kapcsoló a falon")
        switches = input("Add meg, hogy milyen sorrendben akarod felkapcsolni a kapcsolókat (pl.: 0101111)\n")
    if room_number == "13":
        if room_number not in rooms:
            rooms.append(room_number)
            items.append("korhadt faláda")
        if "lezárt doboz" not in items:
            print("""Ebben a szobában egy korhadt ládát találsz. Elég gyengének tűnik, viszont úgy néz ki mintha lenne benne
valami. Kézzel nem tudod kinyitni, keresni kéne hozzá valami eszközt...""")
            if "balta" in items:
                print("A korábban összeszedett baltával szétvered a ládát és lakattal lezárt kis dobozt találsz benne.")
                rooms.append(room_number)
                items.append("lezárt doboz")
                if "kulcs" in items:
                    print("A nálad lévő kulccsal kinyitod a dobozt és egy szelet húst találsz benne.")
                    rooms.append(room_number)
                    items.append("hús")
        else:
            print("Itt szerezted meg a lezárt dobozt.")    
    
if win:
    print("Kijutottál! Gratulálok!")
else:
    print("Ez most nem jött össze...")