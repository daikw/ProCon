class ABC104:
    modulus = 10 ** 9 + 7

    def __init__(self, s):
        self.s = s
        self.n = len(s)

    def dp(self, i, j):
        """
        dynamic programming for abc 104
        :param i: index of the given string
        :param j: count of letters of composed string (like 'ABC')
        :return: the number of cases
        """
        if i == self.n:
            if j == 3:
                return 1
            else:
                return 0

        if i < self.n and j == 3:
            m = 3 if self.s[i] == '?' else 1
            return m * self.dp(i + 1, 3) % self.modulus

        if i < self.n and j < 3:
            m1 = 3 if self.s[i] == '?' else 1
            m2 = 1 if self.s[i] == '?' or self.s[i] == 'ABC'[j] else 0

            _pass = m1 * self.dp(i + 1, j) % self.modulus
            _take = m2 * self.dp(i + 1, j + 1) % self.modulus

            return _pass + _take


if __name__ == '__main__':
    import sys
    sys.setrecursionlimit(10**7)

    abc = ABC104(input())
    print(abc.dp(0, 0))
