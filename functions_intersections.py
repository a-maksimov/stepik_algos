def intersections(a, b, c, k, m):
    result = set()
    A = a
    B = b - k
    C = c - m

    if A == 0:
        if B == 0:
            return result

        x = -C / B
        y = a * x**2 + b * x + c
        result.add((x, y))
        return result

    D = B * B - 4 * A * C
    if D < 0:
        return result

    elif D == 0:
        x = -B / (2 * A)
        y = a * x**2 + b * x + c
        result.add((x, y))
        return result
    else:
        sqrtD = D ** 0.5
        x1 = (-B + sqrtD) / (2 * A)
        x2 = (-B - sqrtD) / (2 * A)
        y1 = a * x1**2 + b * x1 + c
        y2 = a * x2**2 + b * x2 + c
        result.add((x1, y1))
        result.add((x2, y2))
        return result


print(intersections(1, -3, 2, 1, -1))     # f(x) = x^2 - 3x + 2, g(x) = x - 1
