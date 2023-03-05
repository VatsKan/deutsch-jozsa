from enum import Enum

CONSTANT='constant'
BALANCED='balanced'

BalOrConst = Enum('BalOrConst', ['CONSTANT_0', 'CONSTANT_1', 'BALANCED'])
"""
BalOrConst(Enum)
    'CONSTANT_0' means the black box should always output 0
    'CONSTANT_1' means the black box should always output 1
    'BALANCED' means the black box should output a 1 half of the time and 0 otherwise.
"""