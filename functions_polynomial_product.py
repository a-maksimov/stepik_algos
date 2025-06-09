from collections import defaultdict
from itertools import zip_longest, product


def polynomial_product(p1, p2):
    first_elements = []
    second_elements = []
    for c1, c2 in zip_longest(reversed(p1), reversed(p2), fillvalue=0):
        first_elements.append(c1)
        second_elements.append(c2)
    first_elements.reverse()
    second_elements.reverse()

    length = max(len(p1), len(p2))
    i = length + 1
    j = 0
    k = 0
    exponents_dict = defaultdict(int)
    for item1, item2 in product(first_elements, second_elements):
        c = item1 * item2
        exponents_dict[i] += c

        if j == length - 1:
            k += 1
            i = length + 1 - k
            j = 0
        else:
            i -= 1
            j += 1

    result = list(exponents_dict.values())
    while result[0] == 0:
        result.pop(0)

    return tuple(result)


p1 = (2, -4, 5)                      # P1(x) = 2x^2 - 4x + 5
p2 = (3, 2)                          # P2(x) = 3x + 2

print(polynomial_product(p1, p2))    # P1(x) * P2(x) = 6x^3 - 8x^2 + 7x + 10
# (6, -8, 7, 10)
