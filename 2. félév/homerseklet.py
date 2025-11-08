

file = open("2. félév/homerseklet.txt", "r", encoding = "utf-8")

homerseklet = []
for line in file:
    line = line.strip() # törli a whitespace karaktereket az elejéről és a végéről
    line = line.split(";") # ['9', '-5', '24', '20', '6', '28', '11']
    het_adatai = [int(item) for item in line] # [9, -5, 24, 20, 6, 28, 11]
    homerseklet.append(het_adatai)

file.close()

for item in homerseklet:
    print(item)

# 1. feladat: Hanyadik nap volt a leghidegebb az évben?
min_sor = 0
min_oszlop = 0
for i in range(len(homerseklet)):
    for j in range(len(homerseklet[i])):
        if homerseklet[i][j] < homerseklet[min_sor][min_oszlop]:
            min_sor = i
            min_oszlop = j
nap_sorszam = 7 * min_sor + min_oszlop + 1
print(f"Az év leghidegebb napja a {nap_sorszam}. nap volt, {homerseklet[min_sor][min_oszlop]} °C volt aznap.")

# 2. feladat: Írjuk ki, hogy melyik héten mennyi volt az átlag, min, max hőmérséklet!
for i in range(len(homerseklet)):
    összeg = 0
    min_index = 0
    max_index = 0
    for j in range(len(homerseklet[i])):
        összeg += homerseklet[i][j]
        if homerseklet[i][j] < homerseklet[i][min_index]:
            min_index = j
        if homerseklet[i][j] > homerseklet[i][min_index]:
            max_index = j
    print(f"{i+1}. hét adatai:")
    print(f"\tÁtlag: {round(összeg / len(homerseklet[i]), 1)} °C")
    print(f"\tMinimum: {homerseklet[i][min_index]} °C")
    print(f"\tMaximum: {homerseklet[i][max_index]} °C")



# 3. feladat: Írjuk ki, hogy milyen napon mennyi volt az átlag, min, max hőmérséklet!
# pl.:
# Hétfői napok:
#       Átlag: 13.8
#       min:    5.9
#       max:   18.7