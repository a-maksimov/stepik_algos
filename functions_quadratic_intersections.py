def quadratic_intersections(a1, b1, c1, a2, b2, c2):
    result = set()
    A = a1 - a2
    B = b1 - b2
    C = c1 - c2

    if A == 0:
        if B == 0:
            return result

        x = -C / B
        y = a1 * x**2 + b1 * x + c1
        result.add((x, y))
        return result

    D = B * B - 4 * A * C
    if D < 0:
        return result

    elif D == 0:
        x = -B / (2 * A)
        y = a1 * x**2 + b1 * x + c1
        result.add((x, y))
        return result
    else:
        sqrtD = D ** 0.5
        x1 = (-B + sqrtD) / (2 * A)
        x2 = (-B - sqrtD) / (2 * A)
        y1 = a1 * x1**2 + b1 * x1 + c1
        y2 = a1 * x2**2 + b1 * x2 + c1
        result.add((x1, y1))
        result.add((x2, y2))
        return result


print(quadratic_intersections(-1, 0, 2, 3, 0, 2))
