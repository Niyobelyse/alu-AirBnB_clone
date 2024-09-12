import unittest
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):
    def setUp(self):
        self.model = BaseModel()

    def test_instance_creation(self):
        self.assertIsInstance(self.model, BaseModel)

    def test_save(self):
        old_updated_at = self.model.updated_at
        self.model.save()
        self.assertNotEqual(old_updated_at, self.model.updated_at)

    def test_to_dict(self):
        self.assertIsInstance(self.model.to_dict(), dict)

if __name__ == "__main__":
    unittest.main()

