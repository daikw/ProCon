import unittest
from nose.tools import eq_
from .d import count_lr
import pickle


class Test(unittest.TestCase):
    def setUp(self):
        print('before test')

    def tearDown(self):
        print('after test')

    sample = [
        ((3, 2), (4, 1, 5), 3),
        ((13, 17), (29, 7, 5, 7, 9, 51, 7, 13, 8, 55, 42, 9, 81), 6),
        ((10, 400000000), (1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000), 25),
    ]

    def test_sample(self):
        for test_case in self.sample:
            n, m = test_case[0]
            a = test_case[1]
            eq_(count_lr(n, m, a), test_case[2])

    def test_long(self):
        with open('abc105/test_case_d.pickle', mode='rb') as f:
            test_cases = pickle.load(f)

        for test_case in test_cases:
            n, m = test_case[0]
            a = test_case[1]
            print('n, m: ', n, m)
            print('a: ', a)
            eq_(count_lr(n, m, a), test_case[2])
