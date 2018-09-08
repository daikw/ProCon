def fib(n, memo={}):
    if n == 1 or n == 2:
        return 1
    if n in memo.keys():
        return memo[n]
    else:
        memo[n] = fib(n-1) + fib(n-2)
        return memo[n]


if __name__ == "__main__":
    print(fib(90))