def linear_coefficients(p1, p2):
    k = (p2[1] - p1[1]) / (p2[0] - p1[0])
    b = (p1[1] * p2[0] - p1[0] * p2[1]) / (p2[0] - p1[0])
    return k, b


def equation_of_line(values):
    k1, b1 = None, None
    for i, value in enumerate(values):
        if i + 2 == len(values):
            break

        k1, b1 = linear_coefficients((i, value), (i + 1, values[i + 1]))
        k2, b2 = linear_coefficients((i + 1, values[i + 1]), (i + 2, values[i + 2]))

        if not (k1 == k2 and b1 == b2):
            return

    k1, b1 = int(k1), int(b1)

    string = "y = "
    if k1:
        if abs(k1) != k1:
            if abs(k1) > 1:
                string += f"{k1}x "
            else:
                string += f"-x "
        else:
            if abs(k1) > 1:
                string += f"{k1}x "
            else:
                string += f"x "

    if b1:
        if abs(b1) != b1:
            if k1:
                string += f"- {abs(b1)}"
            else:
                string += f"-{abs(b1)}"
        else:
            if k1:
                string += f"+ {b1}"
            else:
                string += f"{b1}"

    if not k1 and not b1:
        string += f"{b1}"

    return string


print(equation_of_line([0, 1, 2, 3, 4]))

print(equation_of_line([0, -1, -2, -3, -4]))

print(equation_of_line([1, 3, 5, 7, 9]))

print(equation_of_line([6, 6, 6, 6, 6]))

print(equation_of_line([0, -2, -4, -6, -8]))

print(equation_of_line([1, 1, 2, 2, 2]))  # None

print(equation_of_line([-1, -2, -3, -4, -5]))  # y = -x - 1

print(equation_of_line([0, 0, 0, 0, 0]))  # y = 0

