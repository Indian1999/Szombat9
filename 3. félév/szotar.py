import os
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


# Feladat: Számoljuk meg, hogy melyik szó hányszor szerepel a story.txt-ben

path = os.path.join(os.path.dirname(__file__), "forras", "story.txt")
print(path)

with open(path, encoding="utf-8") as f:
    szöveg = f.read()
    szöveg = szöveg.replace(".", "")
    szöveg = szöveg.replace("…", "")
    szöveg = szöveg.replace(",", "")
    szöveg = szöveg.replace(":", "")
    szöveg = szöveg.replace("?", "")
    szöveg = szöveg.replace("!", "")
    szöveg = szöveg.replace("'s", "")
    szöveg = szöveg.replace("\n", " ")
    szöveg = szöveg.replace("–", "")
    szöveg = szöveg.replace("n't", " not")
    szöveg = szöveg.replace("'re", " are")
    szöveg = szöveg.replace("'ve", " have")
    szöveg = szöveg.replace("'ll", " will")
    szöveg = szöveg.replace("'", "")
    while "  " in szöveg:
        szöveg = szöveg.replace("  ", " ")
    szöveg = szöveg.strip()
    szöveg = szöveg.lower()
    szöveg = szöveg.split(" ")

word_counter = {}
for word in szöveg:
    if word in word_counter:
        word_counter[word] += 1
    else:
        word_counter[word] = 1

word_counter = list(word_counter.items())
# x = ('all', 8)     x[1] = 8
word_counter.sort(key=lambda x: x[1], reverse=True)
word_counter = dict(word_counter)
print(word_counter)

lista = [6,3,7,32,6,57,8,4,34,6]
lista.sort(key = lambda x: x//10 + x%10)
print(lista)

