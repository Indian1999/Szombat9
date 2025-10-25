# Számrendszerek
binary = bin(90)
print(binary) # 0b1011010      (0b jelzi, hogy 2-es számrendszer)
print(type(binary)) # <class 'str'>
print("0b nélkül:", binary[2:])

hexa = hex(12648430)
print(hexa) # 0xc0ffee         (0x jelzi, hogy 16-os számrendszer)
print(type(hexa)) # <class 'str'>
print(hexa[2:])

# Hol használjuk a 16-os számrendszert?
# RGB kódok színeknél (#FF1207)   vörös szín (255 piros, 18 zöld, 7 kék)
# MAC cíkenél    (A8-13-E6-2B-60-02) [A szg. fizikai címe]
# IPv6-os ip címek: fe80::c34d:9be7:aeb7%17
# Memóricímzés
class Osztály:
    pass
var = Osztály()
print(var) # <__main__.Osztály object at 0x0000017B868E4390>


octa = oct(90)
print(octa) # 0o132            (0o jelzi, hogy 8-as számrendszer)

# Egyéb számrendszerekből 10-esbe váltás

binary = "101101010101101"
num = int(binary) # Alapaesetben az int() fgv. 10-es számrendszerű számként értelmezi
print(num)
num = int(binary, 2)
print(num) # 23213

hexa = "FA3B"
num = int(hexa, 16)
print(num) # 64059

# Mi van ha 16-osból akarunk 2-esbe?
binary = bin(int(hexa, 16))
print(binary)

# Bináris operátorok

num1 = 42
num2 = 97

# alt gr + w -> |
# alt gt + 3 -> ^     (kétszer kell megnyomni)
print(f"{num1} és {num2} = {num1 & num2}")          # 32
print(f"{num1} vagy {num2} = {num1 | num2}")        # 107
print(f"{num1} kizáró vagy {num2} = {num1 ^ num2}") # 75

# Döntsük el egy számról, hogy páros-e?
if num1 & 1 == 1:
    print(num1, "nem páros!")
else:
    print(num1, "páros!")
if num2 & 1 == 1:
    print(num2, "nem páros!")
else:
    print(num2, "páros!")

# Shiftelés

print(num1)
print(num1 >> 1) # 21
print(num1 >> 2) # 10
print(num1 >> 3) # 5

print(num1 << 1) #  84
print(num1 << 2) # 168
print(num1 << 3) # 336

# Határozzuk meg, hogy x GigaByte az hány TeraByte, MegaByte, KiloByte, Byte, bit
# 1 TB = 1024 GB
# 1 GB = 1024 MB
# 1 MB = 1024 KB
# 1 KB = 1024 B
# 1 B = 8 bit
# 1 bit = 1 db 1-es vagy 0-s
# 1024 = 2^10

giga = int(input("Add meg a GigaByte-ok számát: "))
print(f"{giga} GB = {giga >> 10} TB")
print(f"{giga} GB = {giga << 10} MB")
print(f"{giga} GB = {giga << 20} KB")
print(f"{giga} GB = {giga << 30} B")
print(f"{giga} GB = {giga << 33} bit")
