import os

path = os.path.join(os.path.dirname(__file__), "minecraft-adatok.txt")
print(path)


szerverek = []
with open(path, encoding="utf-8") as f:
    mezonevek = f.readline().strip().split(";")
    for line in f:
        line = line.strip().split(";")
        szerver = {
            mezonevek[0]: line[0],
            mezonevek[1]: line[1],
            mezonevek[2]: int(line[2]),
            mezonevek[3]: int(line[3]),
        }
        szerverek.append(szerver)

#1. Írd ki, hogy hány szerver van összesen!
print(f"Összesen {len(szerverek)} szerver adatai vannak eltárolva.")

#2. Legtöbb játékos
max_index = 0
for i in range(1, len(szerverek)):
    if szerverek[i]["jatekosok"] > szerverek[max_index]["jatekosok"]:
        max_index = i

print(f"A legnépszerűbb szerver a {szerverek[max_index]['nev']}, {szerverek[max_index]['jatekosok']} játékossal.")

#3.

def vip_ar(ar:int) -> int:
    return int(ar * 1.5)

#4. 
szervernev = input("Add meg egy szerver nevét: ")
for szerver in szerverek:
    if szerver["nev"] == szervernev:
        print(f"Ezen a szerveren a vip ár {vip_ar(szerver['havi_dij'])} Ft.")
        break
else:
    print("Nincs ilyen nevű szerver.")

#5.

path = os.path.join(os.path.dirname(__file__), "minecraft-export.txt")

with open(path, "w", encoding="utf-8") as f:
    print("'minecraft-export.txt' létrehozva")
    for szerver in szerverek:
        if szerver["mod"] == "survival":
            f.write(szerver["nev"] + "\n")