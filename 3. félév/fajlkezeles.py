import os

path_forras = os.path.join(os.path.dirname(__file__), "forras")
path_ascii = os.path.join(path_forras, "story_ascii.txt")

data = []
with open(path_ascii, "r", encoding="utf-8") as f:
    for line in f:
        if line == "\n":
            continue
        line = line.strip() # elejéről, végéről eltünteti a whitespace karaktereket
        line = line.split(" ")
        data.append(line)

data_dec = []
for row in data:
    row_dec = []
    for binary in row:
        row_dec.append(int(binary, 2))
    data_dec.append(row_dec)

story = ""
for row in data_dec:
    for num in row:
        story += chr(num)
    story += "\n"

path_decoded = os.path.join(path_forras, "decoded.txt")
with open(path_decoded, "w", encoding="utf-8") as f:
    f.write(story)

f = open(path_ascii)

#input("Megállj1")

f.close()

#input("Megállj2")

code = [73, 116, 116, 32, 97, 32, 118, 233, 103, 101, 32, 102, 117, 115, 115, 32, 101, 108, 32, 118, 101, 108, 101]
with open(path_decoded, "a", encoding="utf-8") as f:
    for num in code:
        f.write(chr(num))
    f.write('\n')

# +-t hozzárakva a módhoz tudunk írni és olvasni is.

with open(os.path.join(path_forras, "plus.txt"), "r+", encoding="utf-8") as f:
    f.write("Szervusz!")
    print(f.read())

with open(os.path.join(path_forras, "plus.txt"), "w+", encoding="utf-8") as f:
    f.write("Hi there!\nGeneral Kenobi!")
    f.seek(0)
    print(f.read())

print("\n#####################################################################\n")
with open(os.path.join(path_forras, "plus.txt"), "a+", encoding="utf-8") as f:
    f.write("\nHi there!\nGeneral Kenobi!")
    f.seek(0)
    print(f.read())

# r: Olvasás, kurzor az elejéről, nem törli a fájl tartalmát
# w: Írás,    kurzor az elejéről, törli a fájl tartalmát
# a: Írás,    kurzor a végéről,   nem törli a fájl tartalmát

# r+: Írás és olvasás, kurzor az elejéről, nem törli fájl tartalmát
# w+: Írás és olvasás, kurzor az elejéről, törli fájl tartalmát
# a+: Írás és olvasás, kurzor a végéről, nem törli fájl tartalmát
    