def linear_coefficients(p1, p2):
    k = (p2[1] - p1[1]) / (p2[0] - p1[0])
    b = (p1[1] * p2[0] - p1[0] * p2[1]) / (p2[0] - p1[0])
    return k, b


def on_one_line(p1, p2, p3):
    k1, b1 = linear_coefficients(p1, p2)
    k2, b2 = linear_coefficients(p2, p3)
    return k1 == k2 and b1 == b2


print(on_one_line((1, 1), (2, 2), (3, 3)))

print(on_one_line((1, 1), (2, 2), (3, 4)))
