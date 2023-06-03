#!/usr/bin/python3
"""
    Module contains of a single class
"""


class Rectangle:
    """Represents a rectangle. No body."""

    def __init__(self, width=0, height=0):
        if not isinstance(width, (int, float)):
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        if not isinstance(height, (int, float)):
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__width = width
        self.__height = height

    def width(self):
        return self.__width

    def height(self):
        return self.__height

    def set_width(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    def set_height(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
