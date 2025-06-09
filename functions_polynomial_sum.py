from itertools import zip_longest


def polynomial_sum(p1, p2):
    result = []
    for c1, c2 in zip_longest(reversed(p1), reversed(p2), fillvalue=0):
        result.append(c1 + c2)

    result.reverse()
    while result[0] == 0:
        result.pop(0)
    return tuple(result)


p1 = (2, -4, 5)                  # P1(x) = 2x^2 - 4x + 5
p2 = (3, 2)                      # P2(x) = 3x + 2

print(polynomial_sum(p1, p2))    # P1(x) + P2(x) = 2x^2 - x + 7

p1 = (1, 7, 0, -4)               # P1(x) = x^3 + 7x^2 - 4
p2 = (-1, 0, 0, 2)               # P2(x) = -x^3 + 2

print(polynomial_sum(p1, p2))    # P1(x) + P2(x) = 7x^2 - 2

