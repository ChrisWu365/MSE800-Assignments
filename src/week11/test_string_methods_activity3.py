'''
Activity Week11-3: Understanding Unit Testing
Examine the following Python code that uses the unittest framework:
 
Tasks to do:
1. Describe what each test method is checking.
    The descriptions are commented in each test function.
2. Run the code and interpret the results.
    The result is "Ran 3 tests in 0.001s OK", which means 3 test functions are executed and all of the tests are passed.
3. Modify the code to add a new test case that checks if '123'.isdigit() returns True.
    New test function test_isdigit() is added to checks if '123'.isdigit() returns True.
4. What happens if one of the assertions fails? Try changing one expected value and observe the result.
    A new test function test_fail_upper() is added to fail the test with an unexpected value, the result prints the traceback information, total number of tests ran and number of failures. The result is pasted below:
        ======================================================================
        FAIL: test_fail_upper (__main__.TestStringMethods.test_fail_upper)
        ----------------------------------------------------------------------
        Traceback (most recent call last):
        File "xxx\MSE800-Assignments\src\week11\test_string_methods_activity3.py", line 25, in test_fail_upper
            self.assertEqual('foo'.upper(), 'FOO1')
        AssertionError: 'FOO' != 'FOO1'
        - FOO
        + FOO1
        ?    +


        ----------------------------------------------------------------------
        Ran 5 tests in 0.001s

        FAILED (failures=1)
'''
import unittest

class TestStringMethods(unittest.TestCase):
    def test_upper(self):
        # check if upper() function of a string object will convert lowercase string 'foo' into uppercase string 'FOO'
        self.assertEqual('foo'.upper(), 'FOO')

    def test_fail_upper(self):
        # check if upper() function of a string object will convert lowercase string 'foo' into uppercase string 'FOO'
        self.assertEqual('foo'.upper(), 'FOO')
        self.assertEqual('foo'.upper(), 'FOO1')

    def test_isupper(self):
        # check if string 'FOO' is uppercase
        self.assertTrue('FOO'.isupper())
        # check if string 'Foo' is not uppercase
        self.assertFalse('Foo'.isupper())
    
    def test_split(self):
        s = 'hello world'
        # check if split() function of the string object will split the string 'hello world' into an array of two substrings by the default whitespace charater seperators. 
        self.assertEqual(s.split(), ['hello', 'world'])
        # check fails when the seperator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

    def test_isdigit(self):
        # checks if '123'.isdigit() returns True
        self.assertTrue('123'.isdigit())

if __name__ == '__main__':
    unittest.main()