s = input()

def dec(n):
    if n == '0':
        return -1
    else:
        return 1

ls = [dec(el) for el in s]
print(len(ls) - abs(sum(ls)))
