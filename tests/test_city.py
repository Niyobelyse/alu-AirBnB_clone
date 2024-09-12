import unittest
from models.city import City

class TestCity(unittest.TestCase):
    def setUp(self):
        self.city = City()

    def test_instance_creation(self):
        self.assertIsInstance(self.city, City)

if __name__ == "__main__":
    unittest.main()

