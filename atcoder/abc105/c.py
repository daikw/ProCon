def determine_digit(digit_num, acm, n):
    mod = 2 ** (digit_num + 1)
    if (n - acm) % mod:
        return 1
    else:
        return 0


def convert(n):
    if n == 0:
        return '0'

    result = ''
    acm = 0
    digit_num = 0
    while n != acm:
        print(digit_num, acm, result)
        d = determine_digit(digit_num, acm, n)
        print('d: ', d)
        acm += d * (-2)**digit_num
        digit_num += 1
        result += str(d)
        if digit_num > 10:
            break

    return result


if __name__ == "__main__":
    n = int(input())

    print(convert(n))
