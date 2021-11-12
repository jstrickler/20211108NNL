"""
General geometry routines
"""
import math

ANIMAL = 'wombat'
NUMBERS = 5, 8, 10

def rectangle_area(length, width):
    """
    Given length and width, calculate area of a rectangle.

    :param length: length of longer side
    :param width: length of shorter side
    :return: area in same units as length and width
    """
    return length * width

def circle_area(diameter):
    """
    Calculate area of circle from its diameter.

    :param diameter: Diameter (not radius) of circle
    :return: area of circle
    """
    radius = diameter / 2
    return math.pi * radius ** 2

def square_area(side):
    """
    Calculate area of square.

    :param side: length of one side
    :return: area of square
    """
    return rectangle_area(side, side)

print("my name is", __name__)

if __name__ == '__main__':  # is this the *main* script
    print("Hi, Mom!")
    x = rectangle_area(8, 19.5)
    print(x)
