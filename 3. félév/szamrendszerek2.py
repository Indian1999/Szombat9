# 2-es számrendszerbe váltás
binaris = bin(974)

print(binaris)          # 0b1111001110
print(type(binaris))    # <class 'str'>

# 16-os számrendszerbe váltás

hexa = hex(974)

print(hexa)             # 0x3ce
print(type(hexa))       # <class 'str'>

# 8-as számrendszerbe váltás

okta = oct(974)

print(okta)         # 0o1716


a = int("974")
print(a)

a = int("100100")
print(a)


a = int("100100",2 )
print(a)

a = int("3ce", 16)
print(a)

a = 39 # 100111
b = 52 # 110100

print(a & b) # 100100 -> 36
print(a | b) # 110111 -> 55
print(a ^ b) # 010011 -> 19
print(~a) # alt gr + 1    (+ 1 és negáljuk) -40
print(a >> 2) # 9
print(a << 3) # 312

# terminálba: ipconfig
# IPv4 Address. . . . . . . . . . . : 192.168.1.105
# Subnet Mask . . . . . . . . . . . : 255.255.255.0

ip = [192, 168, 1, 105]
mask = [255, 255, 255, 240]
network = [ip[i] & mask[i] for i in range(4)]

print(ip)
print(mask)
print(network)

# Adott egy színkód (pl.: #3f8fc1), váltsuk át, ilyen alakba: (63, 143, 193)

color_code = "3f8fc1"
color_mask = int("FF", 16) # 255
red = int(color_code[:2], 16) & color_mask
green = int(color_code[2:4], 16) & color_mask
blue = int(color_code[4:], 16) & color_mask
print((red, green, blue))


# Linuxon a chmod parancs, jogosultságok adására van használva
# első számjegy - admin
# második - felhasználó
# harmadik - csoport
# 1 - olvasás, 2 - írás, 4 - futtatás
# 7 = 1 + 2 + 4, olvasni, írni, futtatni
# 5 = 1 + 4, olvasni, futtatni
# chmod 777 program.a 

# Megkapunk egy számot, írjuk ki hogy milyen jogosultságok tartoznak a számhoz

def permissions(num):
    perms = []
    if num & 1 == 1:
        perms.append("olvasás")
    if num & 2 == 2:
        perms.append("írni")
    if num & 4 == 4:
        perms.append("futtatás")
    return perms

for i in range(8):
    print(f"{i}: {permissions(i)}")
