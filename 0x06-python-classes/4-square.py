#!/usr/bin/python3
class Square:
    """A square class"""

    def __init__(self, size=0):
        """Initializes instance of Square
        Args:
            size (int): size of square
        """
        self.size = size

    @property
    def size(self):
        """gets size, and sets to an integer greater than zero"""
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """finds area"""
        return self.__size ** 2
