def create_matrix(n: int, m: int, value: any = 0) -> list[list[any]]:    
    """
    Létrehoz egy n x m méretű mátrixot, a megadott értékkel feltöltve.

    Args:
        n (int): A mátrix sorainak száma.
        m (int): A mátrix oszlopainak száma.
        value (any, optional): Az érték, amellyel a mátrixot fel kell tölteni. Alapértelmezett értéke 0.

    Raises:
        TypeError: Ha n vagy m nem egész szám.
        ValueError: Ha n vagy m kisebb, mint 1.

    Returns:
        list[list[any]]: A létrehozott mátrix.    
    """
    if type(n) != int or type(m) != int:
        raise TypeError("A mátrix dimenziói egész számok kell legyenek!")
    if n < 1 or m < 1:
        raise ValueError("A dimenziók mérete minimum 1 kell, hogy legyen!")
    mtx = []
    for i in range(n):
        lista = []
        for j in range(m):
            lista.append(value)
        mtx.append(lista)
    return mtx

# Feladat: Készíts egy faktoriális függvényt!
# 1 egész szám típusú paramétert kap, 1 egész számot ad vissza
# Ha nem egész számot kapott paraméterben -> TypeError
# Ha egész szám, de kisebb, mint 0        -> ValueError
# Visszaadja a szám faktoriális értékét
# A fóggvényhez készítsd leírást is!
def factorial(n: int) -> int:
    """
    Visszaadja n faktoriálisát.
    Args:
            n (int): A szám
    Raises:
            Type: Ha nem egész szám
            Value: Ha nem pozitív
    Returns:
            factorial, a szám faktoriálisa
    """
    if type(n) != int:
            raise TypeError("Egész szám lehet csak az n!")
    if n < 0:
            raise ValueError("Csak pozitív szám lehet az n!")
    factorial = 1
    for i in range(n, 0, -1):
            factorial *= i
    return factorial


# Írjunk egy függvényt ami megkap egy stringet és visszaadja, hogy hány darab magánhangzó
# található a stringben (int) (:str)
# Figyeljünk hogy kis és nagybetűkre is működjön
# Írjunk leírást a függvényhez

def count_vowels(string: str) -> int:    
    """
    Megszámolja a magánhangzókat egy adott stringben.

    Args:
        string (str): A bemeneti string.

    Raises:
        TypeError: Ha a bemenet nem string.

    Returns:
        int: A magánhangzók száma a stringben.
    """
    
    if type(string) != str:
         raise TypeError("A string paraméternek string típusúnak kell lennie!")
    counter = 0
    vowels = "öüóűúőoiueáéaí"
    for char in string:
        if char.lower() in vowels:
             counter += 1
    return counter

def is_leap_year(year: int) -> bool:    
    """
    Ellenőrzi, hogy egy adott év szökőév-e.

    Args:
        year (int): Az évszám.

    Raises:
        TypeError: Ha a year paraméter nem egész szám.

    Returns:
        bool: True, ha az év szökőév, különben False.
    """
    
    if type(year) != int:
        raise TypeError("A year mindenképp egész szám kell, hogy legyen!")
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False
