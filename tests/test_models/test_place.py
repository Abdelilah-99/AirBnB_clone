import unittest
from models.place import Place
from models import storage
from models.city import City
from models.user import User
from models.amenity import Amenity

class TestPlace(unittest.TestCase):

    def setUp(self):
        # Create new instances for testing: Place, City, User, and Amenity
        self.place = Place()
        self.city = City()
        self.user = User()
        self.amenity = Amenity()

    def tearDown(self):
        # Clear the storage for each test
        storage._FileStorage__objects = {}

    def test_initialization(self):
        self.assertEqual(self.place.city_id, "")
        self.assertEqual(self.place.user_id, "")
        self.assertEqual(self.place.name, "")
        self.assertEqual(self.place.description, "")
        self.assertEqual(self.place.number_rooms, 0)
        self.assertEqual(self.place.number_bathrooms, 0)
        self.assertEqual(self.place.max_guest, 0)
        self.assertEqual(self.place.price_by_night, 0)
        self.assertEqual(self.place.latitude, 0.0)
        self.assertEqual(self.place.longitude, 0.0)
        self.assertEqual(self.place.amenity_ids, [])

    def test_attribute_assignment(self):
        self.place.city_id = self.city.id
        self.place.user_id = self.user.id
        self.place.name = "Cozy Cottage"
        self.place.description = "A lovely vacation home"
        self.place.number_rooms = 2
        self.place.number_bathrooms = 1
        self.place.max_guest = 4
        self.place.price_by_night = 100
        self.place.latitude = 34.05
        self.place.longitude = -118.24
        self.place.amenity_ids = [self.amenity.id]
        self.assertEqual(self.place.city_id, self.city.id)
        self.assertEqual(self.place.user_id, self.user.id)
        self.assertEqual(self.place.name, "Cozy Cottage")
        self.assertEqual(self.place.description, "A lovely vacation home")
        self.assertEqual(self.place.number_rooms, 2)
        self.assertEqual(self.place.number_bathrooms, 1)
        self.assertEqual(self.place.max_guest, 4)
        self.assertEqual(self.place.price_by_night, 100)
        self.assertEqual(self.place.latitude, 34.05)
        self.assertEqual(self.place.longitude, -118.24)
        self.assertEqual(self.place.amenity_ids, [self.amenity.id])

    def test_str_method(self):
        self.place.name = "Seaside Villa"
        expected_str = f"[Place] ({self.place.id}) {self.place.__dict__}"
        self.assertEqual(str(self.place), expected_str)

    def test_inheritance_from_base_model(self):
        self.assertTrue(hasattr(self.place, "id"))
        self.assertTrue(hasattr(self.place, "created_at"))
        self.assertTrue(hasattr(self.place, "updated_at"))
        self.assertTrue(hasattr(self.place, "save"))
        self.assertTrue(hasattr(self.place, "to_dict"))

    def test_serialization_and_deserialization(self):
        self.place.name = "Mountain Cabin"
        self.place.save()

        # Load the place object back from the storage mechanism
        reloaded_place = Place(**self.place.to_dict())

        # Check if the reloaded object matches the original object
        self.assertEqual(self.place.name, reloaded_place.name)

    def test_save_and_reload_methods(self):
        # Create a new Place instance and save it
        place = Place()
        place.name = "Luxury Penthouse"
        place.save()

        # Reload all objects from storage
        storage.reload()

        # Check if the reloaded object matches the original object
        all_objs = storage.all()
        reloaded_place = all_objs[f"Place.{place.id}"]
        self.assertEqual(place.name, reloaded_place.name)

if __name__ == '__main__':
    unittest.main()
