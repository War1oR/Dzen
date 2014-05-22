__author__ = 'warior'
__mastermind__ = 'https://docs.python.org/3/library/unittest.html'

import unittest
import file4test


class WidgetTestCase(unittest.TestCase):
    #Срабатывает до тестов
    def setUp(self):
        self.widget = file4test.Widget('The widget')

    def test_resize(self):
        self.widget.resize(100, 150)
        self.assertEqual(self.widget.size, (100, 150), 'wrong size after resize')

    def test_default_size(self):
        self.assertEqual(self.widget.size, (50, 50), 'incorrect default size')

    def test_name(self):
        self.assertEqual(self.widget.name, 'The widget', 'incorrect name')

    #Срабатывает до тестов
    def tearDown(self):
        del self.widget


class SkippingTestCase(unittest.TestCase):

    def setUp(self):
        self.widget = file4test.Widget('The widget')

    @unittest.skip("demo skipping")
    def test_nothing(self):
        self.assertEqual('s', "e")

    @unittest.skipIf(file4test.__version__ < 0.1, 'not supported version')
    def test_var_q(self):
        self.assertEqual(self.widget.q, ('foo', 'bar'), 'Incorrect q')

    @unittest.skipUnless(file4test.__author__ == 'warior', 'Not you problem ')
    def test_master(self):
        self.assertEqual(file4test.__mastermind__,
                         "https://docs.python.org/3/library/unittest.html",
                         'incorrect master')


def suite():
    st = unittest.TestSuite()
    st.addTest(WidgetTestCase('test_resize'))
    st.addTest(WidgetTestCase('test_name'))
    return st