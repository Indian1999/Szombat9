# 1. feladat: Írjuk ki 1436-től 2347- ig azokat a számokat amelyek 7-tel és 5-gyel is oszhatók
for i in range(1436, 2348):
    if i % 7 == 0 and i % 4 == 0:
        print(i)
        
# 2. feladat: Állítsuk elő az összes lehetséges vezetéknév + keresztnév kombinációt
keresztnevek = ["James", "Amy", "Charles", "Gabriel"]
vezeteknevek = ["Smith", "Boyle", "Novak", "Doe"]

for kereszt in keresztnevek:
    for vezetek in vezeteknevek:
        print(kereszt, vezetek)
        
# 3. feladat: Írjunk ki * karaktereket félpiramis alakban
#    *
#    **
#    ***
#    ****
#    *****

for i in range(1, 11):
    print("*" * i)
    
# 4. feladat: Találjuk meg és írjuk ki az összes lehetséges párt
nevek = ["Ádám", "Béla", "Cecil", "Dénes", "Elemér", "Ferenc", "Gábor", "Hugó"]
# Ádám Béla
# Cecil Dénes (Dénes Cecil ne legyen)
for i in range(len(nevek)):
    for j in range(i + 1, len(nevek)):
        print(nevek[i], nevek[j])

