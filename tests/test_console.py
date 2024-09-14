#!/usr/bin/python3
"""
Unit tests for the HBNBCommand class
"""

import unittest
from console import HBNBCommand
from unittest.mock import patch
from io import StringIO


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
            self.assertEqual(output.getvalue(), "** class name missing **\n")  # Corrected output

    # Add more tests for the rest of the commands if needed

if __name__ == "__main__":
    unittest.main()
