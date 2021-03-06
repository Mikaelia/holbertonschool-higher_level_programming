#!/usr/bin/python3
class Square:
    """A square class"""

    def __init__(self, size=0):
        """Initializes instance of Square
        Args:
            size (int): size of square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
