def is_triangle(f):
    return  lambda sides: all(sides) and 2 * max(sides) < sum(sides) and f(sides)

@is_triangle
def is_equilateral(sides):
    return sides[0] == sides[1] == sides[2]

@is_triangle
def is_isosceles(sides):
    return sides[0] == sides[1] != sides[2] or sides[1] == sides[2] != sides[0] or sides[0] == sides[2] != sides[1] or is_equilateral(sides)

@is_triangle
def is_scalene(sides):
    return sides[0] != sides[1] != sides[2]
