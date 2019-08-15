import sys
sys.setrecursionlimit(10**7)

modulus = 10 ** 9 + 7
s = input()
n = len(s)


def dp(i, j):
    """
    dynamic programming for abc 104
    :param i: index of the given string
    :param j: count of letters of composed string (like 'ABC')
    :return: the number of cases
    """
    if i == n:
        if j == 3:
            return 1
        else:
            return 0

    else:
        wildcard = s[i] == '?'
        if j == 3:
            m = 3 if wildcard else 1
            return m * dp(i + 1, 3) % modulus

        else:
            m1 = 3 if wildcard else 1
            m2 = 1 if wildcard or s[i] == 'ABC'[j] else 0

            return (m1 * dp(i + 1, j) + m2 * dp(i + 1, j + 1)) % modulus


print(dp(0, 0))
