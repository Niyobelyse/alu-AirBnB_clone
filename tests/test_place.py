import unittest
from models.place import Place

class TestPlace(unittest.TestCase):
    def setUp(self):
        self.place = Place()

    def test_instance_creation(self):
        self.assertIsInstance(self.place, Place)

if __name__ == "__main__":
    unittest.main()

