from src import taskmath
import unittest
import random
import math

from flask import json


class ApplicationTestCase(unittest.TestCase):
    """
    Test case for our Flask application -_o
    """

    TEST_CASE_COUNT = 100

    def setUp(self):
        super(ApplicationTestCase, self).setUp()
        self.app = taskmath.app.test_client()

    def tearDown(self):
        super(ApplicationTestCase, self).tearDown()

    def test_factorial_correct_response(self):
        for _ in range(self.TEST_CASE_COUNT):
            value = random.randint(0, 1000)
            result = self.app.get('/main/factorial{}'.format(value))

            assert math.factorial(value) == json.loads(result.data)

    def test_fibonacci_correct_response(self):
        for _ in range(self.TEST_CASE_COUNT):
            value = random.randint(0, 1000)
            result = self.app.get('/main/fibonacci{}'.format(value))

            fib_arr = json.loads(result.data)

            if len(fib_arr) <= 2:
                for i in fib_arr:
                    assert i == 1
            else:
                for i in range(2, len(fib_arr)):
                    assert fib_arr[i] == fib_arr[i - 1] + fib_arr[i - 2]


if __name__ == '__main__':
    unittest.main()
