import LogiLib
print(LogiLib.constants.pi)

from LogiLib import constants
print(constants.e)

from LogiLib.constants import tau
print(tau)

print(LogiLib.funcs.create_matrix(3, 4, 5))