import unittest
from models.amenity import Amenity
from models import storage


class TestAmenity(unittest.TestCase):
    """Test Amenity"""

    def setUp(self):
        """Create a new Amenity instance for testing"""
        self.amenity = Amenity()

    def tearDown(self):
        """Clear the storage for each test"""
        storage._FileStorage__objects = {}

    def test_initialization(self):
        """Test during initialization"""
        self.assertEqual(self.amenity.name, "")

    def test_attribute_assignment(self):
        """Test attribute during assignment"""
        self.amenity.name = "Wi-Fi"
        self.assertEqual(self.amenity.name, "Wi-Fi")

    def test_str_method(self):
        """test the expected str"""
        self.amenity.name = "Swimming Pool"
        expected_str = f"[Amenity] ({self.amenity.id}) {self.amenity.__dict__}"
        self.assertEqual(str(self.amenity), expected_str)

    def test_inheritance_from_base_model(self):
        """test inheritance"""
        self.assertTrue(hasattr(self.amenity, "id"))
        self.assertTrue(hasattr(self.amenity, "created_at"))
        self.assertTrue(hasattr(self.amenity, "updated_at"))
        self.assertTrue(hasattr(self.amenity, "save"))
        self.assertTrue(hasattr(self.amenity, "to_dict"))

    def test_serialization_and_deserialization(self):
        """test serialization and deserialization"""
        self.amenity.name = "Parking"
        self.amenity.save()

        # Load the amenity object back from the storage mechanism
        reloaded_amenity = Amenity(**self.amenity.to_dict())

        # Check if the reloaded object matches the original object
        self.assertEqual(self.amenity.name, reloaded_amenity.name)

    def test_save_and_reload_methods(self):
        """test save and reload"""
        # Create a new Amenity instance and save it
        amenity = Amenity()
        amenity.name = "Gym"
        amenity.save()

        # Reload all objects from storage
        storage.reload()

        # Check if the reloaded object matches the original object
        all_objs = storage.all()
        reloaded_amenity = all_objs[f"Amenity.{amenity.id}"]
        self.assertEqual(amenity.name, reloaded_amenity.name)


if __name__ == '__main__':
    unittest.main()
