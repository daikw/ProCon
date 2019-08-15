import sys
from itertools import chain

s = [
    '100 100\n',
    '12 12\n',
    '13 13\n',
    '14 14\n',
    '12 112\n',
    '13 113\n',
    '14 114\n',
    '12 1212\n',
    '13 1213\n',
    '14 1214\n',
    '12 12312\n',
    '13 12313\n',
    '14 12314\n',
    '2 15\n',
    '3 16\n',
    '4 17\n',
    '2 155\n',
    '2 177\n',
    '2 2\n',
    '3 3\n',
    '4 4\n',
    '2 5\n',
    '3 6\n',
    '4 7\n',
    '2 55\n',
    '2 77\n',
    '2 99',
]

def main():
    s = sys.stdin.readlines()
    # print(s)

    n, m = map(int, s[0].split())
    table = [list(chain([i], list(map(int, py.split())))) for i, py in zip(range(m), s[1:])]

    # print('table1')
    # print(table)

    table.sort(key=lambda x: x[2])
    table.sort(key=lambda x: x[1])

    # print('table2')
    # print(table)

    _i = table[0][0]
    _p = table[0][1]
    count = 1
    result = [[_i, _p, count]]

    for i, p, _ in table[1:]:
        if p == _p:
            count += 1
        else:
            count = 1
            _p = p
        result.append([i, p, count])

    # print('result')
    # print(result)

    result.sort(key=lambda x: x[0])
    print('\n'.join([str(p).rjust(6, '0') + str(count).rjust(6, '0') for _, p, count in result]))


if __name__ == '__main__':
    main()