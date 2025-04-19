def draw_graph(f):
    size = 10
    step = 3

    values = []
    for x in range(1, size):
        value = f(x)
        if value > size - 1:
            continue
        values.append((value, x))

    print("y ^")
    for i in range(size - 1, 0, -1):
        print(f"{i} |", end="")
        shift = 0
        j = 0
        for pair in values:
            if not pair[0] == i:
                continue
            shift = ((step * pair[1]) - 1) - shift
            print(" " * shift + "*", end="")
            j += 1
            shift += 1
            shift *= j
        print()

    print(" " * (step - 1) + "+", end="")
    for i in range(1, size):
        print("---", end="")
    print(" > x")

    print(" " * step, end="")
    for i in range(1, size):
        print(" " * (step - 1) + str(i), end="")
    print()


draw_graph(lambda x: x)

draw_graph(lambda x: x ** 2 - 10 * x + 26)


def f(x):
    if x <= 5:
        return x
    return x - 2 * (x % 5)


draw_graph(f)

draw_graph(lambda x: 2)
