#!/usr/bin/python3
""" Start of Unit Tests """


import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
import os


class TestBase_Init(unittest.TestCase):
    """ Unittesting Base Class """

    def reset_nb_objs(self):
        Base._Base__nb_objects = 0

    def test_init_without_id(self):
        be1 = Base()
        self.assertEqual(be1.id, 1)

    def test_multiple(self):
        be1 = Base()
        be2 = Base()
        self.assertEqual(be1.id, be2.id - 1)

    def test_with_id(self):
        be1 = Base(25)
        self.assertEqual(be1.id, 25)

    def test_public_id(self):
        be1 = Base(19)
        be1.id = 28
        self.assertEqual(28, be1.id)

    def test_negative_id(self):
        self.assertEqual(-1, Base(-1).id)

    def test_float_id(self):
        floatTest = 15.99
        self.assertEqual(floatTest, Base(15.99).id)

    def test_dict_id(self):
        dictTest = {'X': 5, 'Y': 7}
        self.assertEqual(dictTest, Base({'X': 5, 'Y': 7}).id)

    def test_string_id(self):
        str_Test = "String Test"
        self.assertEqual(str_Test, Base("String Test").id)

    def test_list_id(self):
        list_Test = [19, 8, 9, 3]
        self.assertEqual(list_Test, Base([19, 8, 9, 3]).id)


class TestBase_json_to_str(unittest.TestCase):
    """ Unittesting JSON to String """

    def test_to_json_string_rect_type(self):
        rect = Rectangle(15, 5, 1, 12, 2)
        rect_json = Base.to_json_string([rect.to_dictionary()])
        self.assertTrue(isinstance(rect_json, str))

    def test_to_json_string_sqr_type(self):
        sqr = Square(12, 5, 4, 2)
        sqr_json = Base.to_json_string([sqr.to_dictionary()])
        self.assertTrue(isinstance(sqr_json, str))

    def test_to_json_string_rect_dict(self):
        rect = Rectangle(15, 5, 1, 12, 2)
        rect_json = Base.to_json_string([rect.to_dictionary()])
        rectLen = len(rect_json)
        self.assertEqual(rectLen, 54)

    def test_to_json_string_sqr_dict(self):
        sqr = Square(12, 5, 4, 2)
        sqr_json = Base.to_json_string([sqr.to_dictionary()])
        sqrLen = len(sqr_json)
        self.assertEqual(sqrLen, 39)

    def test_to_json_string_rect_three_dict(self):
        ra = Rectangle(15, 5, 1, 12, 2)
        rb = Rectangle(11, 6, 1, 10, 5)
        rc = Rectangle(17, 11, 3, 1, 9)
        rct_list = [ra.to_dictionary(), rb.to_dictionary(), rc.to_dictionary()]
        rect_json = Base.to_json_string(rct_list)
        rectLen = len(rect_json)
        self.assertEqual(rectLen, 162)

    def test_to_json_string_sqr_three_dict(self):
        sa = Square(12, 5, 4, 2)
        sb = Square(5, 12, 2, 4)
        sc = Square(9, 15, 4, 6)
        sqr_list = [sa.to_dictionary(), sb.to_dictionary(), sc.to_dictionary()]
        sqr_json = Base.to_json_string(sqr_list)
        sqrLen = len(sqr_json)
        self.assertEqual(sqrLen, 117)

    def test_to_json_string_none(self):
        with self.assertRaises(TypeError):
            Base.to_json_string()

    def test_to_json_more_args(self):
        with self.assertRaises(TypeError):
            Base.to_json_string([], 1)


if (__name__ == "__main__"):
    unittest.main()
