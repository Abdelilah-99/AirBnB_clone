import unittest
from models.base_model import BaseModel
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    """..."""

    def test_initialization(self):
        """test intialization"""
        my_model = BaseModel()
        self.assertIsNotNone(my_model.id)
        self.assertIsInstance(my_model.created_at, datetime)
        self.assertIsInstance(my_model.updated_at, datetime)

    def test_str_method(self):
        """test str method"""
        my_model = BaseModel()
        expected_str = f"[BaseModel] ({my_model.id}) {my_model.__dict__}"
        self.assertEqual(str(my_model), expected_str)

    def test_save_method(self):
        """Test save method"""
        my_model = BaseModel()
        original_updated_at = my_model.updated_at
        my_model.save()
        self.assertNotEqual(my_model.updated_at, original_updated_at)

    def test_to_dict_method(self):
        """Test to dict method"""
        my_model = BaseModel()
        my_model_dict = my_model.to_dict()
        self.assertIsInstance(my_model_dict, dict)
        self.assertEqual(my_model_dict['id'], my_model.id)
        self.assertEqual(my_model_dict['__class__'], 'BaseModel')

    def test_deserialization(self):
        """Test deserialization of BaseModel"""
        my_model = BaseModel()
        my_model_dict = my_model.to_dict()
        new_model = BaseModel(**my_model_dict)
        self.assertEqual(my_model.id, new_model.id)
        self.assertNotEqual(my_model.created_at, new_model.created_at.isoformat())
        self.assertNotEqual(my_model.updated_at, new_model.updated_at.isoformat())


if __name__ == '__main__':
    unittest.main()
