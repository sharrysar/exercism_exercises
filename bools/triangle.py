"""
    equilateral: all sides are equal
    isosceles: two sides are equal
    scalene: all sides are not equal
"""

def equilateral(sides):
    for side in sides:
        if side == 0:
            return False
    if sides[0] == sides[1] and sides[1] == sides[2] and sides[0] == sides[2]:
        if sides[0] + sides[1] >= sides[2] and sides[1] + sides[2] >= sides[0] and sides[0] + sides[2] >= sides[1]:
            return True
    return False


def isosceles(sides):
    for side in sides:
        if side == 0:
            return False
    if sides[0] == sides[1] or sides[1] == sides[2] or sides[0] == sides[2]:
        if sides[0] + sides[1] >= sides[2] and sides[1] + sides[2] >= sides[0] and sides[0] + sides[2] >= sides[1]:
            return True
    return False


def scalene(sides):
    for side in sides:
        if side == 0:
            return False
    if sides[0] != sides[1] and sides[1] != sides[2] and sides[0] != sides[2]:
        if sides[0] + sides[1] >= sides[2] and sides[1] + sides[2] >= sides[0] and sides[0] + sides[2] >= sides[1]:
            return True
    return False
