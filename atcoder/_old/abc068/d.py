# coding: utf-8

if __name__ == "__main__":

    k = int(input())
    n = 50

    x, y = k//n, k%n

    ans = [i + x for i in range(n)]

    for i in range(n):
        if i <= y-1:
            ans[i] += n-y+1
        else:
            ans[i] -= y

    print(n)
    print(' '.join(map(str, ans)))





