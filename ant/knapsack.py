n = 4
w = [2, 1, 3, 2]  # weight
v = [3, 2, 4, 2]  # value
W = 5  # max weight

# back track method
def rec1(i: int, j: int):
    res = 0
    if i == n:
        pass
    elif j < w[i]:
        res = rec1(i + 1, j)
    else:
        res = max(
            rec1(i + 1, j),
            rec1(i + 1, j - w[i]) + v[i]
        )
    return res

# dynamic programming
lw = len(w) + 2
lv = len(v) + 2
table = [ [-1]*lw for _ in range(lv) ]
def rec2(i: int, j: int):
    if table[i][j] >= 0:
        return table[i][j]

    # ---------------------↓ここは同じ↓---------------------
    res = 0
    if i == n:
        pass
    elif j < w[i]:
        res = rec2(i + 1, j)
    else:
        res = max(
            rec2(i + 1, j),
            rec2(i + 1, j - w[i]) + v[i]
        )
    # ---------------------↑ここは同じ↑---------------------

    table[i][j] = res  # save result to the table
    return res

if __name__ == '__main__':
    print("{}\n".format(rec2(0, W)))
