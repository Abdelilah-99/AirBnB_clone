import unittest
from models.review import Review
from models import storage
from models.place import Place
from models.user import User


class TestReview(unittest.TestCase):

    def setUp(self):
        # Create new instances for testing: Review, Place, and User
        self.review = Review()
        self.place = Place()
        self.user = User()

    def tearDown(self):
        # Clear the storage for each test
        storage._FileStorage__objects = {}

    def test_initialization(self):
        self.assertEqual(self.review.place_id, "")
        self.assertEqual(self.review.user_id, "")
        self.assertEqual(self.review.text, "")

    def test_attribute_assignment(self):
        self.review.place_id = self.place.id
        self.review.user_id = self.user.id
        self.review.text = "A wonderful stay!"
        self.assertEqual(self.review.place_id, self.place.id)
        self.assertEqual(self.review.user_id, self.user.id)
        self.assertEqual(self.review.text, "A wonderful stay!")

    def test_str_method(self):
        self.review.text = "Great experience!"
        expected_str = f"[Review] ({self.review.id}) {self.review.__dict__}"
        self.assertEqual(str(self.review), expected_str)

    def test_inheritance_from_base_model(self):
        self.assertTrue(hasattr(self.review, "id"))
        self.assertTrue(hasattr(self.review, "created_at"))
        self.assertTrue(hasattr(self.review, "updated_at"))
        self.assertTrue(hasattr(self.review, "save"))
        self.assertTrue(hasattr(self.review, "to_dict"))

    def test_serialization_and_deserialization(self):
        self.review.text = "Excellent service"
        self.review.save()

        # Load the review object back from the storage mechanism
        reloaded_review = Review(**self.review.to_dict())

        # Check if the reloaded object matches the original object
        self.assertEqual(self.review.text, reloaded_review.text)

    def test_save_and_reload_methods(self):
        # Create a new Review instance and save it
        review = Review()
        review.text = "Lovely accommodations"
        review.save()

        # Reload all objects from storage
        storage.reload()

        # Check if the reloaded object matches the original object
        all_objs = storage.all()
        reloaded_review = all_objs[f"Review.{review.id}"]
        self.assertEqual(review.text, reloaded_review.text)


if __name__ == '__main__':
    unittest.main()
