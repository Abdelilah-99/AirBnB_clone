import unittest
from models.user import User
from models import storage


class TestUser(unittest.TestCase):
    """unittest"""
    def setUp(self):
        """# Create a new User instance for testing"""
        self.user = User()

    def tearDown(self):
        """# Clear the storage for each test"""
        storage._FileStorage__objects = {}

    def test_initialization(self):
        """..."""
        self.assertEqual(self.user.email, "")
        self.assertEqual(self.user.password, "")
        self.assertEqual(self.user.first_name, "")
        self.assertEqual(self.user.last_name, "")

    def test_attribute_assignment(self):
        """..."""
        self.user.email = "user@example.com"
        self.user.password = "password123"
        self.user.first_name = "John"
        self.user.last_name = "Doe"
        self.assertEqual(self.user.email, "user@example.com")
        self.assertEqual(self.user.password, "password123")
        self.assertEqual(self.user.first_name, "John")
        self.assertEqual(self.user.last_name, "Doe")

    def test_str_method(self):
        """..."""
        self.user.email = "user@example.com"
        self.user.first_name = "John"
        expected_str = f"[User] ({self.user.id}) {self.user.__dict__}"
        self.assertEqual(str(self.user), expected_str)

    def test_inheritance_from_base_model(self):
        """..."""
        self.assertTrue(hasattr(self.user, "id"))
        self.assertTrue(hasattr(self.user, "created_at"))
        self.assertTrue(hasattr(self.user, "updated_at"))
        self.assertTrue(hasattr(self.user, "save"))
        self.assertTrue(hasattr(self.user, "to_dict"))

    def test_serialization_and_deserialization(self):
        """..."""
        self.user.email = "user@example.com"
        self.user.password = "password123"
        self.user.first_name = "John"
        self.user.last_name = "Doe"
        self.user.save()

        # Load the user object back from the storage mechanism
        reloaded_user = User(**self.user.to_dict())

        # Check if the reloaded object matches the original object
        self.assertEqual(self.user.email, reloaded_user.email)
        self.assertEqual(self.user.password, reloaded_user.password)
        self.assertEqual(self.user.first_name, reloaded_user.first_name)
        self.assertEqual(self.user.last_name, reloaded_user.last_name)

    def test_save_and_reload_methods(self):
        """..."""
        # Create a new User instance and save it
        my_user = User()
        my_user.email = "user@example.com"
        my_user.save()

        # Reload all objects from storage
        storage.reload()

        # Check if the reloaded object matches the original object
        all_objs = storage.all()
        reloaded_user = all_objs[f"User.{my_user.id}"]
        self.assertEqual(my_user.email, reloaded_user.email)


if __name__ == '__main__':
    unittest.main()
