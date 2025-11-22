import LogiLib
print(LogiLib.constants.pi)

from LogiLib import constants
print(constants.e)

from LogiLib.constants import tau
print(tau)

print(LogiLib.funcs.create_matrix(3, 4, 5))

from LogiLib.funcs import factorial

print(factorial(0))

print(LogiLib.funcs.count_vowels("A cica felmászott a fára, miközben esett az eső."))