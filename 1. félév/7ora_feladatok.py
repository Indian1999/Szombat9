# 1. feladat: Olvassunk be egy x és egy y koordinátát, 
# döntsük el, hogy melyik síknegyedben található ez a pont
#   4 # 1
#   # # #
#   3 # 2
x_pos = int(input("Add meg az x koordinátát!\n"))
y_pos = int(input("Add meg az y koordinátát!\n"))
if x_pos > 0 and y_pos > 0:
    print("1. síknegyed")
elif x_pos > 0 and y_pos < 0:
    print("2. síknegyed")
elif x_pos < 0 and y_pos < 0:
    print("3. síknegyed")
else:
    print("4. síknegyed")

# 2. feladat: Határozzuk meg 2 szám, legnagyobb közös osztóját
num1 = 42
num2 = 84
lnko = 1
for i in range(2, num1 + 1):
    if num1 % i == 0 and num2 % i == 0:
        lnko = i
print(f"lnko({num1}, {num2}) = {lnko}")
# 3. feladat: Határozzuk meg 2 szám legkisebb közös többszörösét
lkkt = 1
while not (lkkt % num1 == 0 and lkkt % num2 == 0):
    lkkt += 1
print(f"lkkt({num1}, {num2}) = {lkkt}")

# 4. feladat: Írjuk ki egy szám prímtényezőit

# 5. feladat: Határozzuk meg egy téglatest térfogatát az élek hosszának ismeretében.
a = 10
b = 12
c = 7

# 6. feladat: Határozzuk meg ugyan ennek a téglatestnek a felszínét