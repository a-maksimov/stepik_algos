import math


def count_digits(n):
    return math.floor(math.log10(n) + 1)


def count_powers(num):
    digits_in_num = count_digits(num)
    n = 1
    digits = 0
    while True:
        digits += count_digits(2**n)
        if digits == digits_in_num:
            break

        n += 1

    return n


print(count_powers(248))  # 3
