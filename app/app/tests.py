from django.test import TestCase
from .calc import add, subtract


class CalcTests(TestCase):

    def test_add_numbers(self):
        """Test that two numbers are added toghether"""
        self.assertEqual(add(3, 8), 11)

    def test_substact_numbers(self):
        """Test that values are substracted and returned"""
        self.assertEqual(subtract(5, 11), 6)
