def determine_digit(digit_num, acm, n):
    mod = 2 ** (digit_num + 1)
    if (n - acm) % mod:
        return 1
    else:
        return 0


def convert(n):
    result = ''
    acm = 0
    digit_num = 0
    while n != acm:
        print(digit_num, acm, result)
        d = determine_digit(digit_num, acm, n)
        print('d: ', d)
        digit_num += 1
        acm += d * 2**digit_num
        result += str(d)
        if digit_num > 10:
            break

    return result


if __name__ == "__main__":
    n = int(input())

    print(convert(n))
