#!/usr/bin/python3
class BaseGeometry():
    """base class"""

    def area(self):
        """area function"""
        raise Exception('area() is not implemented')
    def integer_validator(self, name, value):
        """Validates value"""
        if not isinstance(value, int):
            raise TypeError('{} must be an integer'.format(name))
        if value <= 0:
            raise ValueError('{} must be greater than 0'.format(name))


class Rectangle(BaseGeometry):
    """class that inherits from basegeometry"""
    def __init__(self, width, height):
        if self.integer_validator("width", width):
            self.__width = width
        if self.integer_validator("height", height):
            self.__height = height