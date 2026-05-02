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


    