def quadratic_values(a, b, c, start=0, step=1):
    def evaluate(_x):
        return a * _x**2 + b * _x + c

    results = []
    for x in range(start, start + step * 10, step):
        results.append((x, evaluate(x)))

    return results


print(quadratic_values(1, 0, 0, start=2))

