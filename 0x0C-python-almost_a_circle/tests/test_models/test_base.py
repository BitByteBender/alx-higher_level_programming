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
        self.assertEqual(be1.id, 7)

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

class TestBase_json_from_str(unittest.TestCase):
    """ Unittesting from_json_string method """

    def reset(self):
        Base._Base__nb_objects = 0

    def testMultipleRect_from_json_string(self):
        rect1 = {"id": 18, "width": 5, "height": 1, "x": 9, "y": 15}
        rect2 = {"id": 19, "width": 18, "height": 2, "x": 19, "y": 1}
        rect3 = {"id": 20, "width": 5, "height": 3, "x": 6, "y": 5}
        data_in = [rect1, rect2, rect3]
        json_data = Rectangle.to_json_string(data_in)
        data_out = Rectangle.from_json_string(json_data)
        self.assertTrue(data_in, data_out)

    def testMultipleSqr_from_json_string(self):
        sqr1 = {"id": 21, "size": 4, "height": 5, "x": 7}
        sqr2 = {"id": 22, "size": 3, "height": 2, "y": 10}
        sqr3 = {"id": 23, "size": 2, "height": 3, "x": 5, "y": 6}
        data_in = [sqr1, sqr2, sqr3]
        json_data = Rectangle.to_json_string(data_in)
        data_out = Rectangle.from_json_string(json_data)
        self.assertTrue(data_in, data_out)

    def testType_from_json_string(self):
        data_in = [{"id": 115, "width": 5, "height": 1}]
        json_data = Rectangle.to_json_string(data_in)
        data_out = Rectangle.from_json_string(json_data)
        self.assertTrue(isinstance(data_out, list))

    def testEmptyList_from_json_string(self):
        empty_list = []
        self.assertEqual(empty_list, Base.from_json_string("[]"))

    def testNone_from_json_string(self):
        lst = []
        self.assertEqual(lst, Base.from_json_string(None))

    def testNoArgs_from_json_string(self):
        with self.assertRaises(TypeError):
            Base.from_json_string()

class TestBase_Create(unittest.TestCase):
    """ Unittesting create method """

    def reset(self):
        Base._Base__nb_objects = 0

    def testNewlyCreated_square(self):
        sqrA_dict = Square(7, 4, 1, 5).to_dictionary()
        sqrB = Square.create(**sqrA_dict)
        txtFormatter = "[Square] (5) 4/1 - 7"
        self.assertEqual(txtFormatter, str(sqrB))

    def testOrg_square(self):
        sqrA_dict = Square(9, 6, 2, 9).to_dictionary()
        sqrB = Square.create(**sqrA_dict)
        txtFormatter = "[Square] (9) 6/2 - 9"
        self.assertEqual(txtFormatter, str(sqrB))

    def testIsNot_created_square(self):
        sqrA = Square(2, 7, 3, 3)
        sqrA_dict = sqrA.to_dictionary()
        sqrB = Square.create(**sqrA_dict)
        self.assertIsNot(sqrA, sqrB)

    def testNewlyCreated_rect(self):
        rectA_dict = Rectangle(7, 4, 1, 5, 3).to_dictionary()
        rectB = Rectangle.create(**rectA_dict)
        txtFormatter = "[Rectangle] (3) 1/5 - 7/4"
        self.assertEqual(txtFormatter, str(rectB))

    def testOrg_rect(self):
        rectA_dict = Rectangle(8, 6, 1, 4, 3).to_dictionary()
        rectB = Rectangle.create(**rectA_dict)
        txtFormatter = "[Rectangle] (3) 1/4 - 8/6"
        self.assertEqual(txtFormatter, str(rectB))

    def testEqual_rect(self):
        rectA = Rectangle(10, 5, 3, 2, 4)
        rectA_dict = rectA.to_dictionary()
        rectB = Rectangle.create(**rectA_dict)
        self.assertNotEqual(rectA, rectB)

class TestBase_save_to_file(unittest.TestCase):
    """ Unittesting save_to_file method """

    def testMultipleSavings_to_file_rect(self):
        rectA = Rectangle(11, 17, 8, 7, 15)
        rectB = Rectangle(11, 17, 17, 6, 51)
        Rectangle.save_to_file([rectA, rectB])
        with open("Rectangle.json", mode='r') as file:
            rectLen = len(file.read())
            self.assertTrue(rectLen == 111)

    def testMultipleSavings_to_file_sqr(self):
        sqrA = Square(8, 7, 1, 5)
        sqrB = Square(5, 8, 1, 5)
        Square.save_to_file([sqrA, sqrB])
        with open("Square.json", mode='r') as file:
            sqrLen = len(file.read())
            self.assertTrue(sqrLen == 76)

    def testOverride(self):
        rectA = Rectangle(11, 19, 5, 7, 15)
        Rectangle.save_to_file([rectA])
        rectB = Rectangle(1, 17, 17, 6, 51)
        Rectangle.save_to_file([rectB])
        with open("Rectangle.json", mode='r') as file:
            rectLen = len(file.read())
            self.assertTrue(rectLen == 55)

    def testNone_save_to_file(self):
        Rectangle.save_to_file(None)
        with open("Rectangle.json", mode='r') as file:
            empty = "[]"
            self.assertEqual(empty, file.read())

    def testEmptyList_save_to_file(self):
        Rectangle.save_to_file([])
        with open("Rectangle.json", mode='r') as file:
            empty_list = "[]"
            self.assertEqual(empty_list, file.read())

    def test_fileFetch(cls):
        try:
            os.remove("Base.json")
        except FileNotFoundError:
            pass
        try:
            os.remove("Rectangle.json")
        except FileNotFoundError:
            pass
        try:
            os.remove("Square.json")
        except FileNotFoundError:
            pass

class TestBase_load_from_file(unittest.TestCase):
    """ Unittesting load_from_file method """

    def testLoadingsRectangle_from_file(self):
        rectA = Rectangle(11, 17, 8, 7, 15)
        rectB = Rectangle(11, 17, 17, 6, 51)
        Rectangle.save_to_file([rectA, rectB])
        loader = Rectangle.load_from_file()
        self.assertEqual(str(rectB), str(loader[1]))

    def testLoadingsSquare_from_file(self):
        sqrA = Square(8, 7, 1, 5)
        sqrB = Square(5, 8, 1, 5)
        Square.save_to_file([sqrA, sqrB])
        loader = Square.load_from_file()
        self.assertEqual(str(sqrA), str(loader[0]))

    def testTypes_square(self):
        rectA = Rectangle(11, 19, 5, 7, 15)
        Rectangle.save_to_file([rectA])
        rectB = Rectangle(1, 17, 17, 6, 51)
        Rectangle.save_to_file([rectB])
        load = Square.load_from_file()
        self.assertTrue(all(type(o) == Square for o in load))

    def testLoadNone_from_file(self):
        self.assertEqual([], Square.load_from_file())

    def test_fileFetch(cls):
        try:
            os.remove("Rectangle.json")
        except FileNotFoundError:
            pass
        try:
            os.remove("Square.json")
        except FileNotFoundError:
            pass



if (__name__ == "__main__"):
    unittest.main()
