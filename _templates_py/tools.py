def gcd(a, b):
    if a < b:
        return gcd(b, a)
    if b == 0:
        return a
    while b:
        a, b = b, a % b
    return a


def gcd_(list):
    result = list[0]
    for el in list[1:]:
        result = gcd(result, el)
    return result


def lcm(a, b):
    return a * b // gcd(a, b)


def lcm_(list):
    result = list[0]
    for el in list[1:]:
        result = lcm(result, el)
    return result
