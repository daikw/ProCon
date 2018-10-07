class FutureMath:
    def gcd(self, a, b):
        if a < b:
            return self.gcd(b, a)
        if b == 0:
            return a
        while b:
            a, b = b, a % b
        return a

    def gcd_(self, list):
        result = list[0]
        for el in list[1:]:
            result = self.gcd(result, el)
        return result

    def lcm(self, a, b):
        return a * b // self.gcd(a, b)

    def lcm_(self, list):
        result = list[0]
        for el in list[1:]:
            result = self.lcm(result, el)
        return result


future_math = FutureMath()
