# ValueError: could not convert string to float: '5ű'
# TypeError: unsupported operand type(s) for /: 'str' and 'str'
# ZeroDivisionError: float division by zero

try:
    osztando = float(input("Osztandó: "))
    oszto = float(input("Osztó: "))

    eredmény = osztando / oszto

    print(f"{osztando} / {oszto} = {eredmény}")
except ValueError:
    print("Számokat adj meg!")
except ZeroDivisionError:
    print("Nullával nem szabad osztani!")
except:
    print("Ismeretlen hiba!")
finally:
    # A finally lefut akkor is ha volt hiba, akkor is ha nem
    print("Osztás vége.")


def fakt(n):
    if not isinstance(n, int): # Ha n nem integer
        raise TypeError(f"The fact(n) function only takes 'int' as parameter not '{type(n)}'")
    if n < 0:
        raise ValueError(f"Argument of the fakt(n) function has to be a non-negitve integer! ({n} was given)")
    if n == 0:
        return 1
    return n * fakt(n-1)

#print(fakt(1.1)) # TypeError: The fact(n) function only takes 'int' as parameter not '<class 'float'>'
print(fakt(-2))   # ValueError: Argument of the fakt(n) function has to be a non-negitve integer! (-2 was given)
