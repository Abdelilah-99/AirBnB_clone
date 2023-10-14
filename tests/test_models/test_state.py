import unittest
from models.state import State
from models import storage


class TestState(unittest.TestCase):
    """..."""
    def setUp(self):
        """# Create a new State instance for testing"""
        self.state = State()

    def tearDown(self):
        """# Clear the storage for each test"""
        storage._FileStorage__objects = {}

    def test_initialization(self):
        """..."""
        self.assertEqual(self.state.name, "")

    def test_attribute_assignment(self):
        """..."""
        self.state.name = "California"
        self.assertEqual(self.state.name, "California")

    def test_str_method(self):
        """..."""
        self.state.name = "New York"
        expected_str = f"[State] ({self.state.id}) {self.state.__dict__}"
        self.assertEqual(str(self.state), expected_str)

    def test_inheritance_from_base_model(self):
        """..."""
        self.assertTrue(hasattr(self.state, "id"))
        self.assertTrue(hasattr(self.state, "created_at"))
        self.assertTrue(hasattr(self.state, "updated_at"))
        self.assertTrue(hasattr(self.state, "save"))
        self.assertTrue(hasattr(self.state, "to_dict"))

    def test_serialization_and_deserialization(self):
        """..."""
        self.state.name = "Florida"
        self.state.save()

        # Load the state object back from the storage mechanism
        reloaded_state = State(**self.state.to_dict())

        # Check if the reloaded object matches the original object
        self.assertEqual(self.state.name, reloaded_state.name)

    def test_save_and_reload_methods(self):
        """# Create a new State instance and save it"""
        state = State()
        state.name = "Texas"
        state.save()

        # Reload all objects from storage
        storage.reload()

        # Check if the reloaded object matches the original object
        all_objs = storage.all()
        reloaded_state = all_objs[f"State.{state.id}"]
        self.assertEqual(state.name, reloaded_state.name)


if __name__ == '__main__':
    unittest.main()
