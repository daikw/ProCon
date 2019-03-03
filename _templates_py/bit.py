class BIT:
    def __init__(self, n_max):
        self.arr = []
        self.n_max = n_max

    def read(self, idx):
        if idx > self.n_max:
            return None
        sum = 0
        while idx > 0:
            sum += self.arr[idx]
            idx &= idx - 1
        return sum

    def update(self, idx, val=1):
        while idx <= self.n_max:
            self.arr[idx] += val
            idx += idx & -idx


if __name__ == '__main__':
    arr = []
    bit = BIT(10)
    inv = 0

