'''
Activity Week 11-1: Unit-testing
Describe the usage of unit testing in short paragraph, share your GitHub link. See the following code: 
'''
import unittest

def add(x, y):
    return x + y

class TestMathOperation(unittest.TestCase):
    '''
    Create a class inherited from unittest.TestCase, so the methods started with 'test' prefix in this class will be executed when running this class
    '''
    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)

if __name__ == '__main__':
    unittest.main()

