if __name__ == "__main__":
    h, w = map(int, input().split())
    n = int(input())
    an = list(map(int, input().split()))

    seq = []
    for i, ai in enumerate(an):
        seq.extend([i+1]*ai)

    rows = [seq[s:e] for s, e in zip(range(0, h*w, w), range(w, h*w+w, w))]
    rows = [row if i%2 == 0 else row[::-1] for i, row in enumerate(rows)]

    for row in rows:
        print(' '.join(map(str, row)))

