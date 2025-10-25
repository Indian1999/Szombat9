import random

def func(x):
    for i in range(10):
        if i == x:
            return
    print("Függvény vége")

func(6) # Nem ír ki semmit
func(23) # Függvény vége

# Felsoroló/generátor függvények: (yield)

def négyzet_range(also_index, felso_index):
    for i in range(also_index, felso_index):
        yield i**2

print(négyzet_range(5, 10)) # <generator object négyzet_range at 0x0000024317D5E5E0>
print(range(80))            # range(0, 80)
for num in négyzet_range(253, 321):
    print(num, end = " ")
print()

def myRange(n):
    i = 0
    while i < n:
        yield i
        i += 1

for i in myRange(10):
    print(i, end=" ")
print()

# Írjunk egy generátor függvény ami felsorolja a fibonacci számokat

from functools import cache

@cache
def fib(n):
    if n == 1 or n == 2:
        return 1
    return fib(n-1) + fib(n-2)

def fib_generator(n):
    for i in range(1, n + 1):
        yield fib(i)

print([num for num in fib_generator(20)])

# Írjunk egy generátort ami vasszdobálgajta egy listából a páros számokat

def yield_evens(lista):
    for item in lista:
        if item % 2 == 0:
            yield item

print([num for num in yield_evens([32, 5, 56, 32, 23, 54, 6,56,78,76,34,1,23,2,31,43,4,33,12])])

# 1. feladat: Írjunk egy generátor függvényt ami az
# a(n) = a(n-1) - 4
# a(1) = 100
# 100, 96, 92, ...

def a(n):
    value = 100
    for i in range(n):
        yield value
        value -= 4

print([num for num in a(15)])

# 2. feladat: Írjunk egy generátort ami egy stringet kap meg és felsorolja a stringben található magánhangzókat

def yield_vowels(string):
    vowels = "óüöűúőoiueáéaíÓÜÖŰÚŐOIUEÁÉAÍ"
    for char in string:
        if char in vowels:
            yield char

print([char for char in yield_vowels("Kiskacsa fürdik")])
print(" ".join([char for char in yield_vowels("Kiskacsa fürdik")]))

# 3. feladat: Írjunk egy prímszámokat generáló függvényt
# Egy n természetes számot kap paraméterül, visszaadj az első n darab prímszámot
def is_prime(num):
    for i in range(2, num // 2 + 1):
        if num % i == 0:
            return False
    return True

def prime_generator(n):
    counter = 0
    num = 2
    while counter < n:
        if is_prime(num):
            counter += 1
            yield num
        num += 1

print([i for i in prime_generator(50)])

# Feladat: Írjunk egy függvény ami kiszűri egy listából azokat az elemeket, amik teljesítenek
# egy paraméterben megkapott feltételt

def divisible_by_5(num):
    return num % 5 == 0

def filter_list(lista, func):
    for item in lista:
        if func(item):
            yield item

lista = [random.randint(1, 100) for i in range(50)]
primes = [item for item in filter_list(lista, is_prime)]
divs_by_5 = [item for item in filter_list(lista, divisible_by_5)]
smaller_than_10 = [item for item in filter_list(lista, lambda x: x < 10)]

print(lista)
print(primes)
print(divs_by_5)
print(smaller_than_10)


def slow(num):
    if num <= 2:
        return num
    return slow(num-1) + 2*slow(num-2)

def slow_generator():
    i = 1
    while True:
        yield slow(i)
        i += 1

for i in slow_generator():
    print(i)
