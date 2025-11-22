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

