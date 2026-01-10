def diff_even_odd(a, b):
    if a == b:
        if a % 2 == 0:
            return a
        else:
            return -b

    # even sum
    if a % 2 == 0:
        a1 = a
    else:
        a1 = a + 1

    if b % 2 == 0:
        an = b
    else:
        an = b - 1

    n_even = len(range(a1, an + 1, 2))
    even_sum = ((a1 + an) // 2) * n_even

    # odd sum
    if a % 2 == 0:
        a1 = a + 1
    else:
        a1 = a

    if b % 2 == 0:
        an = b - 1
    else:
        an = b

    n_odd = len(range(a1, an + 1, 2))
    odd_sum = ((a1 + an) // 2) * n_odd

    return even_sum - odd_sum


print(diff_even_odd(23, 42))   # (24 + 26 + 28 + ... + 42) - (23 + 25 + 27 + ... + 41) => 10
print(diff_even_odd(1, 1))  # 0 - 1 => -1
print(diff_even_odd(10, 10))  # 10 - 0 => 10
print(diff_even_odd(3, 5))  # -4


def diff_even_odd(a, b):
    a_even = a + a % 2
    b_even = b - b % 2
    even_sum = (b_even + a_even) // 2 * ((b_even - a_even) // 2 + 1)

    a_odd = a + (1 - a % 2)
    b_odd = b - (1 - b % 2)
    odd_sum = (b_odd + a_odd) // 2 * ((b_odd - a_odd) // 2 + 1)

    return even_sum - odd_sum
