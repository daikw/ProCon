import unittest
from nose.tools import eq_
from .c import determine_digit, convert
from random import randint


def generate_test_case():
    test_case = '1'
    size = randint(0, 10)
    for i in range(size):
        test_case += str(randint(0, 1))

    return test_case


class Test(unittest.TestCase):
    def setUp(self):
        print('before test')

    def tearDown(self):
        print('after test')

    def test_determine_digit(self):
        eq_(determine_digit(0, 0, 1), 1)
        eq_(determine_digit(0, 0, 2), 0)
        eq_(determine_digit(0, 0, 3), 1)
        eq_(determine_digit(0, 0, 4), 0)
        eq_(determine_digit(1, 0, 2), 1)
        eq_(determine_digit(1, 1, 3), 1)
        eq_(determine_digit(1, 1, 5), 0)
        eq_(determine_digit(2, 0, 4), 1)
        eq_(determine_digit(0, 0, 9), 1)
        eq_(determine_digit(1, 1, 9), 0)
        eq_(determine_digit(2, 1, 9), 0)
        eq_(determine_digit(3, 1, 9), 1)
        eq_(determine_digit(0, 0, -9), 1)
        eq_(determine_digit(1, 1, -9), 1)
        eq_(determine_digit(2, -1, -9), 0)
        eq_(determine_digit(3, -1, -9), 1)

    @staticmethod
    def _convert(test_case):
        n = 0
        for i, digit in enumerate(test_case[::-1]):
            n += int(digit) * (-2)**i
        return n

    test_cases = [
         '10101101',
         '10101000',
         '101101011',
         '10000000',
         '1',
         '1001',
         '10101',
         '11100110',
         '11101',
         '1',
         '110101',
         '11',
         '110111111',
         '10010110',
         '111110011',
         '10'
    ]

    def test_result(self):
        for test_case in self.test_cases:
            eq_(convert(self._convert(test_case)), test_case)
