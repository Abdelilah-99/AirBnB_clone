import unittest
from models.city import City
from models import storage


class TestCity(unittest.TestCase):

    def setUp(self):
        # Create a new City instance for testing
        self.city = City()

    def tearDown(self):
        # Clear the storage for each test
        storage._FileStorage__objects = {}

    def test_initialization(self):
        self.assertEqual(self.city.state_id, "")
        self.assertEqual(self.city.name, "")

    def test_attribute_assignment(self):
        self.city.state_id = "State.27c12caa-9c2a-40a4-8a6c-5c12a39105e8"
        self.city.name = "New York City"
        self.assertEqual(self.city.state_id, "State.27c12caa-9c2a-40a4-8a6c-5c12a39105e8")
        self.assertEqual(self.city.name, "New York City")

    def test_str_method(self):
        self.city.state_id = "State.27c12caa-9c2a-40a4-8a6c-5c12a39105e8"
        self.city.name = "Los Angeles"
        expected_str = f"[City] ({self.city.id}) {self.city.__dict__}"
        self.assertEqual(str(self.city), expected_str)

    def test_inheritance_from_base_model(self):
        self.assertTrue(hasattr(self.city, "id"))
        self.assertTrue(hasattr(self.city, "created_at"))
        self.assertTrue(hasattr(self.city, "updated_at"))
        self.assertTrue(hasattr(self.city, "save"))
        self.assertTrue(hasattr(self.city, "to_dict"))

    def test_serialization_and_deserialization(self):
        self.city.state_id = "State.27c12caa-9c2a-40a4-8a6c-5c12a39105e8"
        self.city.name = "Chicago"
        self.city.save()

        # Load the city object back from the storage mechanism
        reloaded_city = City(**self.city.to_dict())

        # Check if the reloaded object matches the original object
        self.assertEqual(self.city.state_id, reloaded_city.state_id)
        self.assertEqual(self.city.name, reloaded_city.name)

    def test_save_and_reload_methods(self):
        # Create a new City instance and save it
        city = City()
        city.state_id = "State.27c12caa-9c2a-40a4-8a6c-5c12a39105e8"
        city.name = "San Francisco"
        city.save()

        # Reload all objects from storage
        storage.reload()

        # Check if the reloaded object matches the original object
        all_objs = storage.all()
        reloaded_city = all_objs[f"City.{city.id}"]
        self.assertEqual(city.state_id, reloaded_city.state_id)
        self.assertEqual(city.name, reloaded_city.name)


if __name__ == '__main__':
    unittest.main()
