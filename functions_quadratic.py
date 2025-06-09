def quadratic(x1, x2):
    b = -(x1 + x2)
    c = x1 * x2

    parts = ["x^2"]  # стартуем с "x^2"

    if b:
        if b == 1:
            parts.append(" + x")
        elif b == -1:
            parts.append(" - x")
        elif b > 0:
            parts.append(f" + {b}x")
        else:  # b < 0 и |b| != 1
            parts.append(f" - {-b}x")

    if c:
        if c > 0:
            parts.append(f" + {c}")
        else:  # c < 0
            parts.append(f" - {-c}")

    equation = "".join(parts) + " = 0"

    return equation


print(quadratic(-3, 4))