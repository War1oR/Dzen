__author__ = 'warior'
__mastermind__ = ['https://docs.python.org/3/library/unittest.html']

import unittest
import file4test


class WidgetTestCase(unittest.TestCase):
    def setUp(self):
        self.widget = file4test.Widget('The widget')

    def test_resize(self):
        self.widget.resize(100, 150)
        self.assertEqual(self.widget.size, (100, 150),
                         'wrong size after resize')

    def test_default_size(self):
        self.assertEqual(self.widget.size, (50, 50),
                         'incorrect default size')

