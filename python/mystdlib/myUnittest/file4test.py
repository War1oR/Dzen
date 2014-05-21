__author__ = 'warior'
__mastermind__ = ['https://docs.python.org/3/library/unittest.html']


class Widget():

    def __init__(self, arg):
        self.name = arg
        self.size = (510, 50)

    def resize(self, x, y):
        self.size = (x, y)
