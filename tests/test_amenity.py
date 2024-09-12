import unittest
from models.amenity import Amenity

class TestAmenity(unittest.TestCase):
    def setUp(self):
        self.amenity = Amenity()

    def test_instance_creation(self):
        self.assertIsInstance(self.amenity, Amenity)

if __name__ == "__main__":
    unittest.main()

