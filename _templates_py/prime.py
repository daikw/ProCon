import math
import random


class Prime:
    seed_primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

    def is_prime(self, n):
        """
        prime test (hybrid)

        see also: https://qiita.com/gushwell/items/ff9ed83ba55350aaa369

        :param n:
        :return: boolean
        """
        is_prime_common = self.is_prime_common(n)
        if is_prime_common is not None:
            return is_prime_common

        if n < 2000000:
            return self.is_prime_brute_force(n)
        else:
            return self.is_prime_miller_rabin(n)

    def is_prime_common(self, n):
        if n == 1: return False
        if n in Prime.seed_primes: return True
        if any(map(lambda x: n % x == 0, self.seed_primes)): return False

    def is_prime_brute_force(self, n):
        """
        brute force prime test
        use with is_prime_common if you want to skip seed_primes

        :param n:
        :return: boolean
        """
        for k in range(2, int(math.sqrt(n)) + 1):
            if n % k == 0:
                return False
        return True

    def is_prime_miller_rabin(self, n):
        """
        miller rabin prime test
        use with is_prime_common if you want to skip seed_primes

        see also: https://qiita.com/srtk86/items/609737d50c9ef5f5dc59

        :param n:
        :return: boolean
        """

        d = (n - 1) >> 1
        while d & 1 == 0:
            d >>= 1

        for k in range(100):
            a = random.randint(1, n - 1)
            t = d
            y = pow(a, t, n)

            while t != n - 1 and y != 1 and y != n - 1:
                y = (y * y) % n
                t <<= 1

            if y != n - 1 and t & 1 == 0:
                return False

        return True

    def gcd(self, a, b):
        if a < b:
            return self.gcd(b, a)
        if b == 0:
            return a
        while b:
            a, b = b, a % b
        return a

