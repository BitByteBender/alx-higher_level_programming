#!/usr/bin/python3
""" Start of Unit Tests """


import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
import os


class TestRectangle_Init(unittest.TestCase):
    """ Unittesting Rectangle Class """

    def test_zero_args(self):
        with self.assertRaises(TypeError):
            Rectangle()

    def test_multiple_args(self):
        rectA = Rectangle(5, 7, 9, 5)
        rectB = Rectangle(6, 9, 7, 5)
        self.assertNotEqual(rectA.id, rectB.id)

    def test_is_base(self):
        self.assertIsInstance(Rectangle(5, 4), Base)


class TestRectangle_Height(unittest.TestCase):
    """ Unittesting Rectangle Height """

    def reset(self):
        self.rectangle = Rectangle(2, 4)

    def test_zero(self):
        with self.assertRaises(ValueError):
            Rectangle(2, 0)

    def test_negative(self):
        with self.assertRaises(ValueError):
            Rectangle(2, -4)


class TestRectangle_Width(unittest.TestCase):
    """ Unittesting Rectangle Width """

    def reset(self):
        self.rectangle = Rectangle(4, 8)

    def test_zero(self):
        with self.assertRaises(ValueError):
            Rectangle(4, 0)

    def test_negative(self):
        with self.assertRaises(ValueError):
            Rectangle(4, -8)


class TestRectangle_X_Coord(unittest.TestCase):
    """ Unittesting Rectangle X Coord """

    def reset(self):
        self.rectangle = Rectangle(2, 4, 8)

    def test_negative(self):
        with self.assertRaises(ValueError):
            Rectangle(2, 4, -8)


class TestRectangle_Y_Coord(unittest.TestCase):
    """ Unittesting Rectangle Y Coord """

    def reset(self):
        self.rectangle = Rectangle(2, 4, 8, 16)

    def test_negative(self):
        with self.assertRaises(ValueError):
            Rectangle(2, 4, 8, -16)


class TestRectangle_Area(unittest.TestCase):
    """ Unittesting Rectangle Area """

    def testRectangle_Area(self):
        rect = Rectangle(7, 14, 4, 6)
        self.assertEqual(rect.area(), 98)
