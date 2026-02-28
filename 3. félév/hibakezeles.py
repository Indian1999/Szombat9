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