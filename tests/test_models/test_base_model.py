#!/usr/bin/env python3
"""
test_base_model.py

This module define tests that will help validate the BaseModel class
methods as it is intended to.

The module achives this by the help of the unittest module.
"""
from datetime import datetime
from models.base_model import BaseModel
import unittest
from models import storage
import os


class TestBaseModel(unittest.TestCase):
    """
    TestBaseModel class.

    This class contain all possible test cases that ensure
    the BaseModel class is working correctly.
    """

    def test_unique_id(self):
        """
        test_unique_id test case.

        This test case tests wither the assigned instance id
        differes from other instance's id or not
        """
        base1 = BaseModel()
        base2 = BaseModel()
        self.assertIsInstance(base1.id, str)
        self.assertIsInstance(base2.id, str)
        self.assertNotEqual(base1.id, base2.id)

    def test_created_at(self):
        """
        test_created_at test case.

        This test case tests wither the assigned instance timestamp is created
        correctly and both creation and update times are equal.
        """
        base1 = BaseModel()
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
        base1 = BaseModel()
        old_time = base1.updated_at
        base1.save()
        self.assertNotEqual(old_time, base1.updated_at)
        self.assertTrue(base1.updated_at > old_time)

    def test_init_from_dict(self):
        """
        test_init_from_dict test case.

        This test case tests the initializing process form a passed dictionary
        to the __init__() method.
        """
        base1 = BaseModel()
        bm1_dict = base1.to_dict()
        bm_from_dict = BaseModel(**bm1_dict)
        self.assertEqual(bm_from_dict.id, base1.id)
        self.assertEqual(bm_from_dict.created_at, base1.created_at)
        self.assertEqual(bm_from_dict.updated_at, base1.updated_at)

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
        base1 = BaseModel()
        bm_dict = base1.to_dict()
        self.assertIsInstance(bm_dict, dict)
        self.assertEqual(bm_dict['id'], str(base1.id))
        self.assertEqual(bm_dict['__class__'], 'BaseModel')
        self.assertEqual(
                bm_dict['created_at'], base1.created_at.isoformat()
            )
        self.assertEqual(
                bm_dict['updated_at'], base1.updated_at.isoformat()
            )

    def test_string_repr(self):
        """
        test_string_repr test case.

        This test case tests the string representation of the instance and
        check if it contains the required info:
            e.g. [<class name>] (<self.id>) <self.__dict__>
        """
        base1 = BaseModel()
        expected_str = "[BaseModel] ({}) {}".format(
                            base1.id,
                            base1.__dict__
                        )
        self.assertEqual(str(base1), expected_str)

    def tearDown(self):
        storage._FileStorage__objects = {}
        if os.path.exists(storage._FileStorage__file_path):
            os.remove(storage._FileStorage__file_path)


if __name__ == "__main__":
    unittest.main()