import json
import unittest
from unittest.mock import patch

from cources.coursera_mipt.week_4.unit_tests.program_under_test import Asteroid


class TestAsteroid(unittest.TestCase):
    def setUp(self):
        self.asteroid = Asteroid(2099942)

    def mocked_get_data(self):
        with open('apophis_fixture.txt') as f:
            return json.loads(f.read())

    @patch('program_under_test.Asteroid.get_data', mocked_get_data)
    def test_name(self):
        self.assertEqual(
            self.asteroid.name, '99942 Apophis (2004 MN4)'
        )

    @patch('program_under_test.Asteroid.get_data', mocked_get_data)
    def test_diameter(self):
        self.assertEqual(self.asteroid.diameter, 682)
