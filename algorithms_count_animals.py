def count_animals(heads, legs):
    if not heads and not legs:
        return 0, 0

    if heads and not legs or legs and not heads:
        return None

    if legs % 2 != 0:
        return None

    for x_ducks in range(heads + 1):
        x_rabbits = heads - x_ducks
        x_ducks = (legs - x_rabbits * 4) // 2
        if x_ducks < 0:
            continue

        if x_ducks + x_rabbits == heads:
            return x_ducks, x_rabbits

    return None


print(count_animals(10, 30))  # (5, 5)
print(count_animals(0, 100))  # None
