import unittest
from models.review import Review

class TestReview(unittest.TestCase):
    def setUp(self):
        self.review = Review()

    def test_instance_creation(self):
        self.assertIsInstance(self.review, Review)

if __name__ == "__main__":
    unittest.main()

