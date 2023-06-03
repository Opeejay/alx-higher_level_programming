#!/usr/bin/python3
"""
    Module contains of a single class
"""


class Rectangle:
    def __init__(self, width=0, height=0):
        self._width = self._check_dimension(width)
        self._height = self._check_dimension(height)

    def _check_dimension(self, dimension):
        if not isinstance(dimension, (int, float)):
            raise TypeError("Dimension must be an integer or float")
        if dimension < 0:
            raise ValueError("Dimension must be >= 0")
        return dimension

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        self._width = self._check_dimension(value)

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self._height = self._check_dimension(value)
