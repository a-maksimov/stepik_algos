def solve(a, b, c):
    def evaluate_d():
        _d = b ** 2 - 4 * a * c
        return _d

    d = evaluate_d()
    if d == 0:
        return {-b / (2 * a)}
    elif d > 0:
        x1 = (-b + d ** 0.5) / (2 * a)
        x2 = (-b - d ** 0.5) / (2 * a)
        return {x1, x2}
    else:
        return set()


print(solve(1, -5, 6))

