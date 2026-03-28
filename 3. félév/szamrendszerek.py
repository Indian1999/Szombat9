# Számrendszerek

# feladat: Írjunk egy függénvyt ami megkap egy egész számot és visszaadja a 2-es
# számrendszerbeli reprezentációját (stringként)

def dec_to_bin(num):
    output = ""
    while num != 0:
        output += str(num%2)
        num = num // 2
    return output[::-1]

print(dec_to_bin(155))
print(dec_to_bin(2315))

# Feladat: Írjunk egy függvényt ami megkap egy egész számot és egy számrendszer alapot.
# ami alapján visszaadja az adott számrendszer-beli alakját (stringként)
# dec_to_base_n(155, 8) -> "233"


def dec_to_base_n(num, n):
    if n < 1 or n > 35:
        raise ValueError("A cél számrendszer alapja 1 és 35 között kell, hogy legyen!")
    szamjegyek = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    output = ""
    if n == 1:
        for i in range(num):
            output += "0"
        return output
    while num != 0:
        output += szamjegyek[num % n]
        num = num // n
    return output[::-1]

print(dec_to_base_n(155, 8)) # 233
print(dec_to_base_n(155, 7)) # 311
print(dec_to_base_n(155, 16))# 9B
#print(dec_to_base_n(155, 160))

# Feladat: Írjunk egy függvényt ami 2-es (str) számrendszerből vált 10-esbe

def bin_to_dec(binary):
    bin_reversed = binary[::-1]
    összeg = 0
    for i in range(len(bin_reversed)):
        összeg += int(bin_reversed[i]) * 2**i
    return összeg

print(bin_to_dec("1100")) # 12


def base_n_to_dec(num, n):
    szamjegyek = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    num_reversed = num[::-1]
    összeg = 0
    for i in range(len(num_reversed)):
        összeg += szamjegyek.index(num_reversed[i]) * n**i
    return összeg

print(base_n_to_dec("245", 8)) # 165
print(base_n_to_dec("AF", 16)) # 175

# Feladat: Írjunk egy függvényt, ami bármyilen számrendből átvált bármilyen számrendszerbe! (str)

def base_n_to_base_m(num, n, m):
    base10 = base_n_to_dec(num, n)
    return dec_to_base_n(base10, m)

print(base_n_to_base_m("14", 5, 3)) # 100
print(base_n_to_base_m("FE17A9", 16, 2)) # 111111100001011110101001
