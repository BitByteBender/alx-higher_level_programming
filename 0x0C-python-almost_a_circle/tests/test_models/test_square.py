#!/usr/bin/python3
""" Start of Unit Tests """


import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
import os


class TestSquare_Init(unittest.TestCase):
    """ Unittesting Square Class """

    def test_zero_args(self):
        with self.assertRaises(TypeError):
            Square()

    def test_multiple_args(self):
        sqrA = Square(5, 7, 5)
        sqrB = Square(6, 9, 5)
        self.assertNotEqual(sqrA.id, sqrB.id)

    def test_is_base(self):
        self.assertIsInstance(Square(10), Base)

    def test_negative(self):
        with self.assertRaises(ValueError):
            Square(12, 4, -1)


class TestSquare_Size(unittest.TestCase):
    """ Unittesting Square size """

    def test_zero(self):
        with self.assertRaises(ValueError):
            Square(0)

    def test_negative(self):
        with self.assertRaises(ValueError):
            Square(-8)

    def test_NaN(self):
        with self.assertRaises(TypeError):
            txt = "NaN"
            Square(txt)

    def test_none(self):
        with self.assertRaises(TypeError):
            Square(None)


class TestSquare_X_Coord(unittest.TestCase):
    """ Unittesting Square X Coord """

    def test_zero(self):
        self.assertEqual(Square(16, 0).x, 0)

    def test_negative(self):
        with self.assertRaises(ValueError):
            Square(16, -8)

    def test_NaN(self):
        with self.assertRaises(TypeError):
            txt = "NaN"
            Square(16, txt)

    def test_none(self):
        with self.assertRaises(TypeError):
            Square(16, None)
