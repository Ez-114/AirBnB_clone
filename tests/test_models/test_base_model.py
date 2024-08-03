#!/usr/bin/env python3
"""
test_base_model.py

This module define tests that will help validate that BaseModel class
functions as it is intended to.

The module achives this by the help of the unittest module.
"""
from datetime import datetime
from models.base_model import BaseModel
import unittest
import uuid


class TestBaseModel(unittest.TestCase):
    """
    TestBaseModel class.

    This class contain all possible test cases that ensure
    the BaseModel class is working correctly.
    """

    def setUp(self):
        """
        setUp method.

        sets up instances of the BaseModel class.
        """
        base1 = BaseModel()
        base2 = BaseModel()

    def test_unique_id(self):
        """
        test_unique_id test case.

        This test case tests wither the assigned instance id
        differes from other instance's id or not
        """
        self.assertIsInstance(base1.id, str)
        self.assertIsInstance(base2.id, str)
        self.assertNotEqual(base1.id, base2.id)

    def test_created_at(self):
        """
        test_created_at test case.

        This test case tests wither the assigned instance timestamp is created
        correctly and both creation and update times are equal.
        """
        self.assertIsInstance(base1.created_at, datetime)
        self.assertIsInstance(base1.updated_at, datetime)
        self.assertEqual(base1.created_at, base1.updated_at)

    def test_update_timestamp(self):
        """
        test_update_timestamp test case.

        This test case tests wither the assigned instance timpestamp is updated
        when the save method is called or not. Also, tests if the updated
        timestamp is greater than the old timestamp
        """
        old_time = base1.updated_at
        base1.save()
        self.assertNotEqual(old_time, base1.updated_at)
        self.assertTrue(base1.updated_at > old_time)

    def test_dictionary_repr(self):
        """
        test_dictionary_repr test case.

        This test case tests wither the dictionary representation
        of the instance by validating if it is a dictionary data type and
        contain all the required attributes:
            - class name
            - id
            - create date
            - update date
        """
        bm_dict = base1.to_dict()
        self.assertIsInstance(bm_dict, dict)
        self.assertEqual(bm_dict['id'], str(base1.id))
        self.assertEqual(bm_dict['__class__'], 'BaseModel')
        self.assertEqual(bm_dict['created_at'], base1.created_at.isoformat())
        self.assertEqual(bm_dict['updated_at'], base1.updated_at.isoformat())

    def test_string_repr(self):
        """
        test_string_repr test case.

        This test case tests the string representation of the instance and
        check if it contains the required info:
            e.g. [<class name>] (<self.id>) <self.__dict__>
        """
        expected_str = "[BaseModel] ({}) {}".format(base1.id, base1.__dict__)
        self.assertEqual(str(base1), expected_str)


if __name__ == "__main__":
    unittest.main()
