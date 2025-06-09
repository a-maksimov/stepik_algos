def polynomial_creator(p):
    length = len(p)

    def calculate_polynomial(n):
        result = 0
        for i in range(length, 0, -1):
            c = p[length - i]
            if c == 0:
                continue

            e = i - 1
            result += c * n**e

        return result

    return calculate_polynomial


p = polynomial_creator((2, 0, 0, 5, -3))    # P(x) = 2x^4 + 5x - 3

print(p(1))                                 # P(1) = 2*1^4 + 5*1 - 3
print(p(2))                                 # P(2) = 2*2^4 + 5*2 - 3
print(p(3))                                 # P(3) = 2*3^4 + 5*3 - 3
