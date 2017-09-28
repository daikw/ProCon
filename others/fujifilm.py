#!/usr/bin/env python3
import csv
import statistics as st
import itertools as it
import math

def main(argv):
    n, filename = argv
    if int(n) == 1:
        result = summary(filename)

    elif int(n) == 2:
        result = pearson(filename)

    for row in result:
        print(','.join(row))


def summary(filename):
    result = [['Subject', 'Mean', 'Median', 'Variance']]
    data = [[] for _ in range(6)]
    with open(filename, newline='') as csvfile:
        reader = csv.reader(csvfile)
        header = reader.__next__()[1:]
        for row in reader:
            for j in range(1, 7):
                data[j-1].append(int(row[j]))

        for j in range(6):
            row = []
            row.append(header[j])
            row.append('{:.2f}'.format(st.mean(data[j])))
            row.append('{:.1f}'.format(st.median(data[j])))
            row.append('{:.2f}'.format(st.pvariance(data[j])))
            result.append(row)
    return result


def pearson(filename):
    result = [['Pair', 'Coefficient']]
    data = [[] for _ in range(6)]
    with open(filename, newline='') as csvfile:
        reader = csv.reader(csvfile)
        h = reader.__next__()[1:]
        for row in reader:
            for j in range(1, 7):
                data[j-1].append(int(row[j]))

        for i, j in it.combinations(range(6), 2):
            pair = h[i] +'-'+ h[j] if h[i] <= h[j] else h[j] +'-'+ h[i]

            row = [pair, '{:.3f}'.format(calc_pearson(data[i], data[j]))]
            result.append(row)
    return result

def calc_pearson(lis1, lis2):
    n = len(lis1)

    sum1 = sum(lis1)
    sum2 = sum(lis2)
    sum1Sq = sum(pow(lis1[p], 2) for p in range(n))
    sum2Sq = sum(pow(lis2[p], 2) for p in range(n))
    pSum = sum(lis1[p]*lis2[p] for p in range(n))

    num=pSum-(sum1*sum2/n)
    den=math.sqrt((sum1Sq-pow(sum1, 2)/n)*(sum2Sq-pow(sum2, 2)/n))

    if den==0: return 0

    return num/den