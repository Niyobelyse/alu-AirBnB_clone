#!/usr/bin/python3
"""
Unit tests for the HBNBCommand class
"""

import unittest
from console import HBNBCommand
from unittest.mock import patch
from io import StringIO
from models import storage
from models.base_model import BaseModel


class TestHBNBCommand(unittest.TestCase):
    """Unit tests for the HBNBCommand interpreter"""

    def test_quit(self):
        """Test that typing quit exits the command interpreter"""
        with patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd("quit")
            self.assertEqual(output.getvalue(), "")

    def test_EOF(self):
        """Test that typing EOF exits the command interpreter"""
        with patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd("EOF")
            self.assertEqual(output.getvalue(), "")

    def test_create_missing_model(self):
        """Test create command with no model name"""
        with patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd("create")
            self.assertEqual(output.getvalue(), "** Model name missing **\n")

    def test_do_all(self):
        """Test all command with no model name"""
        # Create a dummy instance of BaseModel
        base_model_instance = BaseModel()
        base_model_instance.save()  # Save it to storage
        
        with patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd("all")
            # Check if the output includes the string representation of the instance
            self.assertIn(str(base_model_instance), output.getvalue())

    def test_do_all_with_model(self):
        """Test all command with a model name"""
        # Create a dummy instance of BaseModel
        base_model_instance = BaseModel()
        base_model_instance.save()  # Save it to storage
        
        with patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd("all BaseModel")
            # Check if the output includes the string representation of the instance
            self.assertIn(str(base_model_instance), output.getvalue())

    def test_do_all_with_invalid_model(self):
        """Test all command with an invalid model name"""
        with patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd("all InvalidModel")
            self.assertEqual(output.getvalue(), "** class doesn't exist **\n")

    # Add more tests for the rest of the commands if needed

if __name__ == "__main__":
    unittest.main()
