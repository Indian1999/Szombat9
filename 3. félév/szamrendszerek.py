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
    szamjegyek = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    output = ""
    if n == 1:
        pass
    while num != 0:
        output += szamjegyek[num % n]
        num = num // n
    return output[::-1]

print(dec_to_base_n(155, 8)) # 233
print(dec_to_base_n(155, 7)) # 311
print(dec_to_base_n(155, 16))# 9B
print(dec_to_base_n(155, 1))
