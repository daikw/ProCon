import collections as col


def convert(x):
    if x % 4 == 0:
        return 4
    elif x % 2 == 0:
        return 2
    else:
        return 1


if __name__ == "__main__":
    n = int(input())
    a = map(int, input().split())

    count = col.Counter(map(convert, a))

    if count[1] >= 1:
        if count[4] >= count[1]:
            print('Yes')
        elif count[1] == count[4] + 1 and count[2] == 0:
            print('Yes')
        else:
            print('No')

    else:  # count[1] == 0
        if count[4] >= 1:
            print('Yes')
        elif count[2] >= 2:
            print('Yes')
        else:
            print('No')
