#!/usr/bin/env python3
"""
test_file_storage.py

This module defines all possible test cases that will help validate the
FileStorage class methods as it is intended to.

The module achives this by the help of the unittest module.
"""
import unittest
from models.base_model import BaseModel
from models import storage
import json
import os


class TestFileStorage(unittest.TestCase):
    """
    TestFileStorage class.

    This class contain all possible test cases that ensure
    the FileStorage class is working correctly.
    """

    def setUp(self):
        storage._FileStorage__objects = {}
        if os.path.exists(storage._FileStorage__file_path):
            os.remove(storage._FileStorage__file_path)
        self.bm1 = BaseModel()
        self.bm2 = BaseModel()

    def test_class_attribute(self):
        """
        test_class_attribute test case.
        
        Tests the data type of __objects class attr.
        """
        self.assertIsInstance(storage._FileStorage__objects, dict)
        self.assertIsInstance(storage.all(), dict)        

    def test_file_storage_save(self):
        """
        test_file_storage_save test case.

        tests if the pre-created objects' data are successfuly saved
        to a JSON file.
        """
        storage.save()  # This should save the 2 new objs in a JSON file

        # Open the saved JSON file and check if bm1 and bm2 are present
        with open(storage._FileStorage__file_path, mode='r', encoding='utf-8')\
                as file:
            objs_data = json.load(file)

        # Now check the keys for bm1 and bm2
        key_bm1 = 'BaseModel.' + self.bm1.id
        key_bm2 = 'BaseModel.' + self.bm2.id
        self.assertIn(key_bm1, objs_data)
        self.assertIn(key_bm2, objs_data)
        self.assertEqual(objs_data[key_bm1]['id'], self.bm1.id)
        self.assertEqual(objs_data[key_bm1]['__class__'], 'BaseModel')
        self.assertEqual(objs_data[key_bm2]['id'], self.bm2.id)
        self.assertEqual(objs_data[key_bm2]['__class__'], 'BaseModel')

    def test_file_storage_reload(self):
        """
        test_file_storage_reload test case.

        This test case tests if the storage.reload() method correctly
        deserializes BaseModel instances from the JSON file.
        """
        storage.reload()
        key_bm1 = 'BaseModel.' + self.bm1.id
        key_bm2 = 'BaseModel.' + self.bm2.id
        all_objs = storage.all()
        self.assertIn(key_bm1, all_objs)
        self.assertIn(key_bm2, all_objs)
        self.assertIsInstance(all_objs[key_bm1], BaseModel)
        self.assertIsInstance(all_objs[key_bm2], BaseModel)
        self.assertEqual(all_objs[key_bm1].id, self.bm1.id)
        self.assertEqual(all_objs[key_bm2].id, self.bm2.id)
        storage._FileStorage__objects = {}
    
    def test_file_storage_no_file(self):
        """
        test_file_storage_no_file test case.

        This test case tests if the storage.reload() method does nothing
        when the JSON file does not exist.
        """
        if os.path.exists(storage._FileStorage__file_path):
            os.remove(storage._FileStorage__file_path)

        storage.reload()
        self.assertEqual(len(storage._FileStorage__objects), 0)
    
    def tearDown(self):
        """
        tearDown method.

        Cleans up any created files and resets storage.
        """
        if os.path.exists(storage._FileStorage__file_path):
            os.remove(storage._FileStorage__file_path)
        storage._FileStorage__objects = {}


if __name__ == '__main__':
    unittest.main()
