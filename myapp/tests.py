from django.test import TestCase
import unittest
from django.test import Client
# from myapp.models import Animal
#
# class AnimalTestCase(TestCase):
#     def setUp(self):
#         Animal.objects.create(name="lion", sound="roar")
#         Animal.objects.create(name="cat", sound="meow")
#
#     def test_animals_can_speak(self):
#         """Animals that can speak are correctly identified"""
#         lion = Animal.objects.get(name="lion")
#         cat = Animal.objects.get(name="cat")
#         self.assertEqual(lion.speak(), 'The lion says "roar"')
#         self.assertEqual(cat.speak(), 'The cat says "meow"')

class SimpleTest(TestCase):
    def test_basic_addition(self):
        """
        Tests that 1 + 1 always equals 2.
        """
        self.assertEqual(1 + 1, 2)

import unittest

class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

if __name__ == '__main__':
    unittest.main()


class SimpleTest(unittest.TestCase):
    def test_details(self):
        client = Client()
        response = client.get('/')
        self.assertEqual(response.status_code, 301)


# class HelloTestCase(unittest.TestCase):
#     def test_get(self):
#
#         # Setup.
#         #request = 'fake request'
#         #name = 'world'
#
#         request = "abc"
#         response = application(request)
#         # Check.
#         self.assertEqual(response.status_code, 200)
#         #self.assertEqual(response.content, u'Hello world!')
