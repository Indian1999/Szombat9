# Szótárak (dictionary adatszerkezet)

szotar = {} # Üres dictionary
szotar = {
    "alma": "apple",
    "bögre": "mug",
    "citrom": "lemon",
    "dinnye": "melon",
    "kukorica": "corn",
    "só": "salt",
    3: "three",
    "3": "three",
    "három": "three",
    "dinnye": "watermelon" # Felülírja a dinnye kulcshoz tartozó értéket
}

print(szotar)
print(type(szotar)) # <class 'dict'>
print(len(szotar)) # 6
print(szotar["citrom"]) # lemon
print(szotar["3"]) # three
print(szotar["dinnye"]) # watermelon

# A dictionary kulcs-érték párokat tárol
# Egy kulcs csak egyszer szerepelhet a szótárban!
# Az értékekre, nincs ilyen megkötés

#############################
#    DICTIONARY BEJÁRÁSA    #
#############################

def opcio1():
    """A dictionary kulcsain iterálunk végig"""
    for key in szotar.keys():
        print(key, "->", szotar[key])

def opcio2():
    """A dictionary értékein iterálunk végig"""
    # Hátrány: értékből nem tudjuk megkapni a kulcsot
    for value in szotar.values():
        print(value)

def opcio3():
    """kulcs-érték párokon megyünk végig"""
    x,y = (57, 83)
    for item in szotar.items():
        print(item, item[0], item[1]) # ('alma', 'apple') alma apple

    for key, value in szotar.items(): # key = 'alma', value = 'apple'
        print(key,"->",value)

#opcio1()
#opcio2()
opcio3()

# Elem hozzáadása:
szotar["banán"] = "banan"
print(szotar)

# Elem átírása
szotar["banán"] = "banana"
print(szotar)

# Kulcs ellenőrzése (szerepel-e?)
if "bögre" in szotar.keys():
    print("Van benne bögre")
else:
    print("Nincs benne bögre")

# Elem törlése:
del szotar["bögre"]
print(szotar)

if "bögre" in szotar.keys():
    print("Van benne bögre")
else:
    print("Nincs benne bögre")
