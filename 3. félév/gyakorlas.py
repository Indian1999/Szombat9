# Hány kettőskeresztet ír ki a program?
for i in range(12, 19, 2):
    print("#")
# 4

#Hány kettőskeresztet ír ki a program?
for i in range(5, 18, 3): # 5, 8, 11, 14, 17
    print("#"*(i%2))


#Hány kettőskeresztet ír ki a program?
for i in range(5): 
    print("#"*i)
else:
    print("#")

#Hány kettőskeresztet ír ki a program?
for i in range(20, 15):
    print("#")
else:
    print("#"*4)



# Mit ír ki a program?
def f(x):
    return x**2

print(f(3) + f(f(2)))

print(f(3) + f(4) == f(5))


def a():
    num = 3
    for i in range(10):
        num += i
        yield num 

print([i for i in a()]) # [3, 4, 6, 9, 13, 18, 24, 31, 39, 48]
print([i for i in range(10)])

def b(from_num, to_num):
    while from_num < to_num:
        yield from_num**2
        from_num += 1

print([i for i in b(10, 16)])


def c(text):
    for ch in text.lower():
        yield ch

print([item for item in c("AlmaFa")]) # ['d', 'u' ]

from functools import cache


# 1, 1, 2, 3, 5, 8, 13, 21, ...
@cache
def fib(n):
    if n == 1 or n == 2:
        return 1
    return fib(n-1) + fib(n-2)


def fib_gen():
    n = 1
    while True:
        yield (n, fib(n))
        n += 1

for item in fib_gen():
    print(item)
    if item[1] > 1000:
        break



print(243, 432, 54,4,32423, 234, True, "kiscica", sep="; ", end = "\nkiskutya\n")



# *args, bármennyi pozícionális argumentum
def create_list(*args, ordered = False, reverse = False, allow_duplicates = True):
    lista = [arg for arg in args]
    if not allow_duplicates:
        lista = list(set(lista))
    if ordered:
        lista.sort(reverse=reverse)
    return lista

lista = create_list(18, 6, 3, 10, 7, 3, 4, 3, 4, 91)
print(lista)
lista = create_list(18, 6, 3, 10, 7, 3, 4, 3, 4, 91, ordered = True)
print(lista)
lista = create_list(18, 6, 3, 10, 7, 3, 4, 3, 4, 91, ordered = True, reverse = True)
print(lista)
lista = create_list(18, 6, 3, 10, 7, 3, 4, 3, 4, 91, ordered = True, allow_duplicates=False)
print(lista)



# Készíts egy generátor függvényt, amely két paramétert vár.
# a-tól b-ig
# a generátor visszaadogtja a. fibonacci számtól a b-ik fibonacci számig az értékek
# (b. nincs benne)

def fib_range(a, b):
    for i in range(a, b):
        yield fib(i)

print([i for i in fib_range(5, 11)])

# Készíts egy generátor függvényt, aminek 3 paramétere van.
# a-tól b-ig,
# 3. paraméter egy függvényt, amit alkalmazunk számokra- a és b között
# a függvény ezeket az a eredményeket adogassa vissza

def apply_func(a, b, func):
    for i in range(a, b):
        yield func(i)
    
    
print([i for i in apply_func(5, 11, fib)])
print([i for i in apply_func(5, 11, lambda x: x**2)])