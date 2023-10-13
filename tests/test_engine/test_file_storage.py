import unittest
import os
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class TestFileStorage(unittest.TestCase):
    """Test FileStorage file"""

    def setUp(self):
        """Create a FileStorage instance for testing"""
        self.storage = FileStorage()

    def test_initialization(self):
        """Test file and objects"""
        self.assertEqual(self.storage._FileStorage__file_path, "file.json")
        self.assertEqual(self.storage._FileStorage__objects, {})

    def test_all_method(self):
        """Test the main methods"""
        my_model = BaseModel()
        self.storage.new(my_model)
        all_objects = self.storage.all()
        self.assertIn(
            f"{my_model.__class__.__name__}.{my_model.id}", all_objects)

    def test_new_method(self):
        """test the next method"""
        my_model = BaseModel()
        self.storage.new(my_model)
        self.assertEqual(
            self.storage._FileStorage__objects[f"{my_model.__class__.__name__}.{my_model.id}"],
            my_model
        )

    def test_save_and_reload_methods(self):
        """Create an object, add it to FileStorage, and save"""
        my_model = BaseModel()
        my_model.name = "My First Model"
        my_model.my_number = 89
        self.storage.new(my_model)
        self.storage.save()

        # Create a new FileStorage instance and reload data
        new_storage = FileStorage()
        new_storage.reload()

        # Check if the reloaded object matches the original object
        reloaded_objects = new_storage.all()
        self.assertIn(
            f"{my_model.__class__.__name__}.{my_model.id}", reloaded_objects)
        reloaded_model = reloaded_objects[f"{my_model.__class__.__name__}.{my_model.id}"]
        self.assertEqual(my_model.to_dict(), reloaded_model.to_dict())

    def tearDown(self):
        """Remove the test JSON file if it exists"""
        if os.path.exists("file.json"):
            os.remove("file.json")


if __name__ == '__main__':
    unittest.main()
