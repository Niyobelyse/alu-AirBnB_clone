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

        # Check if both instances are in the all_users result by their string representations
        user1_str = f"[User] ({user1.id}) {{'id': '{user1.id}', 'created_at': {user1.created_at}, 'updated_at': {user1.updated_at}}}"
        user2_str = f"[User] ({user2.id}) {{'id': '{user2.id}', 'created_at': {user2.created_at}, 'updated_at': {user2.updated_at}}}"

        self.assertIn(user1_str, all_users)
        self.assertIn(user2_str, all_users)

        # Ensure their IDs are in the printed output
        with patch('sys.stdout', new=StringIO()) as output:
            for user_str in all_users:
                print(user_str)
            
            output_value = output.getvalue()
            self.assertIn(user1.id, output_value)
            self.assertIn(user2.id, output_value)


if __name__ == "__main__":
    unittest.main()
