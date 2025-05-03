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

