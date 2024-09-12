import unittest
from models.user import User

class TestUser(unittest.TestCase):
    def setUp(self):
        self.user = User()

    def test_instance_creation(self):
        self.assertIsInstance(self.user, User)

    def test_attributes(self):
        self.assertEqual(self.user.first_name, "")
        self.assertEqual(self.user.last_name, "")

if __name__ == "__main__":
    unittest.main()

