import unittest
from models.engine.file_storage import FileStorage

class TestFileStorage(unittest.TestCase):
    def setUp(self):
        self.storage = FileStorage()

    def test_instance_creation(self):
        self.assertIsInstance(self.storage, FileStorage)

if __name__ == "__main__":
    unittest.main()

