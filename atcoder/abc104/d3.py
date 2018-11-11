if __name__ == "__main__":
    modulus = 10 ** 9 + 7
    s = input()
    n = len(s)
    dp = [[0] * 4 for _ in range(n + 1)]

    for i in range(n + 1)[::-1]:
        for j in range(4)[::-1]:
            if i == n:
                if j == 3:
                    dp[i][j] = 1
                else:
                    dp[i][j] = 0
            else:
                is_wildcard = s[i] == '?'
                if j == 3:
                    m = 3 if is_wildcard else 1
                    dp[i][j] = m * dp[i + 1][3] % modulus

                else:
                    m1 = 3 if is_wildcard else 1
                    m2 = 1 if is_wildcard or s[i] == 'ABC'[j] else 0

                    dp[i][j] = (m1 * dp[i + 1][j] + m2 * dp[i + 1][j + 1]) % modulus
            # print(i, j, dp[i][j])
    print(dp[0][0])
