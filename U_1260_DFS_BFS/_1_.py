import unittest

def myFunc():
    pass

class ForTest(unittest.TestCase):

    def test1(self):
        test = myFunc(param)
        self.assertEqual(test,result)