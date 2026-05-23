# 1. feladat: Írjunk egy függvényt ami megkap egy stringet, és visszadja
# azt a stringet ami az eredeti első 2, és utolsó 2 elemét tartalmazza.
# ha nincs minimum 2 karaktere, hibát dob

def first_and_last_two(string):
    if len(string) < 2:
        raise ValueError("A string minimum 2 karakterből kell álljon!")
    return string[:2] + string[-2:]

print(first_and_last_two("Hello World!"))
try:
    print(first_and_last_two("A"))
except Exception as ex:
    print(ex)

# 1. b: Legyen egy általános ferzió is, ami az első és utolsó n karaktert adja vissza

def first_and_last_nth(string, n = 1):
    if len(string) < n:
        raise ValueError(f"A string minimum n ({n}) karakterből kell álljon!")
    return string[:n] + string[-n:]

print(first_and_last_nth("Hello World!"))
print(first_and_last_nth("Hello World!", 4))
try:
    print(first_and_last_nth("Hello World!", 15))
except Exception as ex:
    print(ex)

# 2. feladat: Írjunk egy függvényt ami visszaadja hogy egy stringben, hanyadik indexen
# találhatü az első ismétlődő karakter (és melyik ez a karakter).
# Ha nincs ismétlődés None értéket adunk vissza
# pl.: abcddcba    -> (4, "d")
# pl.: abcdefgh    -> None

def first_repeated(string):
    chars = set() # halmaz (set)
    for i in range(len(string)):
        if string[i] in chars:
            return (i, string[i])
        else:
            chars.add(string[i])
    return None

# Ahalmazzal gyorsabb mint listával.
# halmazban megnézni, hogy szerepel-e egy elem 1 lépésből [O(1)]
# Listában ugyan ez O(n) lépés (Amilyen hosszú)
print(first_repeated("abcddcba"))
print(first_repeated("abcdefgh"))


# 3. feladat: Írjunk egy függvényt ami türli egy tuple egy megadott elemét!
# a tuple az immutable ( nem módosítható )
def remove_nth_from_tuple(tup, n):
    lista = list(tup)
    del lista[n]   # lista.pop(n)    is műkedne
    return tuple(lista)

tup = (6,3,7,9,5,3,4,2,3,7,8,5,6,5,4,3,1)
print(tup)
tup = remove_nth_from_tuple(tup, 4)
print(tup)

#del tup[1] # TypeError: 'tuple' object doesn't support item deletion
#del "asd"[2] # TypeError: 'str' object doesn't support item deletion


# 4. feladat: Rendezzünk egy dictionaryt.
# Problem: A dictinary nem rendezhető

colors = {"red": 4, "green": 1, "blue": 3, "white": 2, "black": 6, "yellow": 4}
print(colors)

def sorted_dict(dictionary, reverse = False, key = None):
    items = dictionary.items()
    items = sorted(items, reverse=reverse, key = key)
    return dict(items)

print(sorted_dict(colors))
print(sorted_dict(colors, reverse=True))
print(sorted_dict(colors, reverse=True, key = lambda x: x[1]))
print(sorted_dict(colors, reverse=True, key = lambda x: len(x[0])))

# 5. feladat: Írjunk egy függvényt ami törli egy lista minden 3. elemét.
# pl.: [4,5,6,3,4,5,6,7] -> [4, 5, 3, 4, 6, 7]

# 5. b: Általánosan, minden n. elemet törli

def remove_every_nth(lista, n = 3):
    new_list = []
    for i in range(len(lista)):
        if i % n != n-1:
            new_list.append(lista[i])
    return new_list

print(remove_every_nth([4,5,6,3,4,5,6,7], 2))

# 6. feladat: Írjunk egy függvényt ami egy mátrixot alakít listává
# pl.: [[1,2,3], [4,5,6], [2], [5,5,3,2,1]] -> [1,2,3,4,5,6,2,5,5,3,2,1]

def matrix_to_list(mtx):
    lista = []
    for i in range(len(mtx)):
        for j in range(len(mtx[i])):
            lista.append(mtx[i][j])
    return lista

print(matrix_to_list([[1,2,3], [4,5,6], [2], [5,5,3,2,1]]))

# 7. feladat: Írjuk ki n elem összes sorbarendezési lehetőségét:
# pl.: A, B, C, D moziba mennek, és egymás mellé ülnek le.
# Hányféleképpen tudnak helyet foglalni?
# ismétlés nélküli permutáció (n!)
# ABCD, ABDC, ACDB, ACBD, ADBC, ADCB, BCDA, CDAB, DBCA...

def permutations(lista):
    if len(lista) <= 1:
        return [lista[:]]
    result = []
    for i in range(len(lista)):
        item = lista[i]
        others = lista[:i] + lista[i+1:] # Mindenki más, aki nem az item
        for perm in permutations(others):
            result.append([item] + perm)
    return result

print(permutations(["Anna", "Béla", "Cecil"]))