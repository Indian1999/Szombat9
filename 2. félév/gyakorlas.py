import matplotlib.pyplot as plt # terminálba: pip install matplotlib

# Írjunk egy olyan függvényt ami összeszorozza egy lista összes elemét

def mult_list(lista):
    szorzat = 1
    for item in lista:
        szorzat *= item
    return szorzat

# Most legyen ugyan ez, rekurzívan

def mult_list_rek(lista):
    if len(lista) == 0:
        return 1
    return lista[0] * mult_list_rek(lista[1:])

print(mult_list([3, 3, 7, 2, 11]))
print(mult_list_rek([3, 3, 7, 2, 11]))

# Határozzzuk meg, hogy a labirintus egyes pontjaiba hány lépésből tud eljutni a játékos


def find_start_pos(map):
    for i in range(len(map)):
        for j in range(len(map[i])):
            if map[i][j] == "^":
                return (i, j)
    return None
map = [
    [".",".",".",".","#",".","#","#",".","."],
    [".","#","#",".",".",".",".",".",".","#"],
    [".",".","#",".","#","#","#","#","#","#"],
    ["#","#","#",".",".",".",".",".",".","."],
    [".",".",".",".",".",".",".","#","#","."],
    [".",".",".",".",".","#",".",".","#","."],
    [".","#",".",".","^","#",".",".","#","."],
    ["#","#","#","#",".",".",".","#","#","."],
    ["#",".",".","#",".",".",".",".",".","."],
    [".",".",".",".",".",".","#",".",".","F"]
    ]

tavolsagok = [[float("inf") for j in range(len(map[i]))] for i in range(len(map))]
start_pos = find_start_pos(map)
tavolsagok[start_pos[0]][start_pos[1]] = 0

def find_distances(i, j):
    # Az aktuális poz értékét átírjuk, ha találunk jobbat
    if i > 0 and tavolsagok[i-1][j] < tavolsagok[i][j] + 1:
        tavolsagok[i][j] = tavolsagok[i-1][j] + 1
    if i < len(tavolsagok) - 1 and tavolsagok[i+1][j] < tavolsagok[i][j] + 1:
        tavolsagok[i][j] = tavolsagok[i+1][j] + 1
    if j > 0 and tavolsagok[i][j-1] < tavolsagok[i][j] + 1:
        tavolsagok[i][j] = tavolsagok[i][j-1] + 1
    if j < len(tavolsagok[0]) - 1 and tavolsagok[i][j+1] < tavolsagok[i][j] + 1:
        tavolsagok[i][j] = tavolsagok[i][j+1] + 1
    # Megyünk tovább a szomszédos mezőkre
    if i > 0 and (map[i-1][j] == "." or map[i-1][j] == "F") and tavolsagok[i-1][j] > tavolsagok[i][j] + 1:
        find_distances(i-1, j)
    if i < len(map) - 1 and (map[i+1][j] == "." or map[i+1][j] == "F") and tavolsagok[i+1][j] > tavolsagok[i][j] + 1:
        find_distances(i+1, j)
    if j > 0 and (map[i][j-1] == "." or map[i][j-1] == "F") and tavolsagok[i][j-1] > tavolsagok[i][j] + 1:
        find_distances(i, j-1)
    if j < len(map[0]) - 1 and (map[i][j+1] == "." or map[i][j+1] == "F") and tavolsagok[i][j+1] > tavolsagok[i][j] + 1:
        find_distances(i, j+1)

# start_pos = (8, 7)
# *start_pos = 8, 7    (*: kicsomagoló operátor)
find_distances(*start_pos)
    
plt.imshow(tavolsagok)

for i in range(len(tavolsagok)):
    for j in range(len(tavolsagok[i])):
        if tavolsagok[i][j] != float("inf"):
            plt.text(j, i, tavolsagok[i][j], ha = "center", va = "center")
plt.axis("off") # kikapcsolja a koordináta tengelyeket
plt.title("Labirintus legkisebb lépésszámok")
plt.savefig("map.png")
plt.close()