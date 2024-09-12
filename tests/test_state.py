import unittest
from models.state import State

class TestState(unittest.TestCase):
    def setUp(self):
        self.state = State()

    def test_instance_creation(self):
        self.assertIsInstance(self.state, State)

if __name__ == "__main__":
    unittest.main()

