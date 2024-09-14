from models.user import User  # Assuming User is a subclass of BaseModel
import unittest
from unittest.mock import patch
from io import StringIO


class TestUser(unittest.TestCase):
    """Test the User class"""

    def test_user_initialization(self):
        """Test initialization of a new User"""
        user = User(email="test@example.com", password="password123")
        self.assertEqual(user.email, "test@example.com")
        self.assertEqual(user.password, "password123")
        self.assertEqual(user.first_name, "")
        self.assertEqual(user.last_name, "")

    def test_user_all(self):
        """Test User.all() method"""
        # Create two user instances
        user1 = User()
        user2 = User()

        # Save both instances
        user1.save()
        user2.save()

        # Retrieve all User instances
        all_users = User.all()

        # Check if both instances are in the all_users result
        self.assertIn(user1, all_users)
        self.assertIn(user2, all_users)

        # Ensure their IDs are in the printed output
        with patch('sys.stdout', new=StringIO()) as output:
            for user in all_users:
                print(user.id)
            
            output_value = output.getvalue()
            self.assertIn(user1.id, output_value)
            self.assertIn(user2.id, output_value)


if __name__ == "__main__":
    unittest.main()
