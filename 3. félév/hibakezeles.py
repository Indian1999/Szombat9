import os

try:
    a = 1 #int(input("Add meg az osztandót: "))
    b = 1 #int(input("Add meg az osztót: "))

    # TypeError: unsupported operand type(s) for /: 'str' and 'str'
    # stringre nincs definiálva az osztás művelet
    # ValueError: invalid literal for int() with base 10: '3ű' (nem konvertálható int-té)
    # ZeroDivisionError: division by zero
    c = a / b

    print(f"{a} / {b} = {c}")
except ValueError:
    print("Egész számokat adj meg!")
except ZeroDivisionError:
    print("0-val nem szabad osztani!")
except:
    # KeyboardInterrupt - ctrl + c esetén történik
    print("HIBA")

path_forras = os.path.join(os.path.dirname(__file__), "forras")

try:
    # FileNotFoundError: [Errno 2] No such file or directory:
    with open(os.path.join(path_forras, "storyk.txt")) as f:
        print(f.read())
except FileNotFoundError:
    print("Nem létezik a file!")
finally:
    print("A finally ág, mindig lefut, ha volt kivétel, ha nem")

try:
    path = os.path.join("C:\\", "Windows", "System32", "config", "SAM")
    # PermissionError: [Errno 13] Permission denied: 'C:\\Windows\\System32\\config\\SAM'
    with open(path) as f:
        print(f.read())
except PermissionError:
    print("Ehez nincs jogom!")
except:
    print("Egyéb hiba!")


def fakt(n):
    if not isinstance(n, int): # Ha n nem egy integer
        raise TypeError(f"Érvénytelen argumentum típus ({type(n)}) (fakt({n})). Az argumentumnak egész számnak kell lennie!")
    if n < 0:
        raise ValueError(f"Érvénytelen argumentum érték ({n}). A fakt(n) függvény argumentuma kötelezően nemnegatív számnak kell lennie!")
    if n == 0:
        return 1
    return n * fakt(n-1)

try:
    #print(fakt("cica")) # TypeError: unsupported operand type(s) for -: 'str' and 'int'
    #print(fakt(3.5))
    #print(fakt(-7))
    print(fakt(1500))
except TypeError as ex:
    print(f"Típus hiba lépett fel a program futása során: {ex}")
except ValueError as ex:
    print(f"Érték hiba lépett fel: {ex}")
except Exception as ex: # Általános/bármilyen hiba
    print(f"Ismeretlen hiba: {type(ex)}, {ex}")


# Saját kivétel típus létrehozása
class CicaError(Exception):
    def __init__(self, message):
        super().__init__(f"{message}")

#raise CicaError("Hát ez egy cica hiba...")


# 1. feladat: Írjunk egy függvényt amely paraméterben megkap egy évszámot.
# És visszaadja, hogy azóta hány év telt el.
# Ha jövőbeli évszámot adunk meg -> ValueError
# Az egyáb lehetséges hibákat is kezeld le.

# 1. b: Írj egy programot amely meghívja ezt a függvényt, és a lehetséges hibákat is lekezeli

def elapsed_years(year):
    if not isinstance(year, int):
        raise TypeError(f"Az évszámnak egész számnak kell lennie, ehelyett {year} ({type(year)}-t kaptam.)")
    if year > 2026:
        raise ValueError(f"Jövőbeli évszámot ne adj meg. {year}-t kaptam. A year legyen kisebb mint 2026!")
    return 2026 - year

try:
    print(elapsed_years(2000))
    print(elapsed_years(-2000))
    #print(elapsed_years(342.3))
    #print(elapsed_years(3242))
    print(elapsed_years("cica"))
except TypeError as ex:
    print("Típus hiba:", ex)
except ValueError as ex:
    print("Érték hiba:", ex)
except Exception as ex:
    print("Ismeretlen hiba:", ex)


# 2. feladat: Írj egy függvényt ami megkap paraméterben egy iterálható objektumot (végig lehet menni rajta for ciklusssal)
# A függvény adja vissza a paraméterben megkapott elemeinek az átlagát.
# A függvény futása során esetlegesen fellépő problémákat kezeljük le!