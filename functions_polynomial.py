def polynomial(p):
    length = len(p)
    polynomial_str = ""
    for i in range(length, 0, -1):
        c = p[length - i]
        if c == 0:
            continue

        if abs(c) == 1:
            c_str = ""
        else:
            c_str = str(abs(c))

        sign = "-" if c < 0 else "+"

        if i - 1 == 0:
            value_str = str(1) if not c_str else ""
        elif i - 1 == 1:
            value_str = "x"
        else:
            value_str = f"x^{i - 1}"

        polynomial_str += f"{sign}{c_str}{value_str}"

    if polynomial_str.startswith("+"):
        polynomial_str = polynomial_str[1:]

    return polynomial_str


print(polynomial((1, 3, -1, 1, -2)))
# x^4+3x^3-x^2+x-2


print(polynomial((-2, 0, 1, -5)))
# -2x^3+x-5


print(polynomial((1, 1, 1)))
# x^2+x+1
