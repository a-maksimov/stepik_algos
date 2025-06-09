import math


def is_power_of_two(n):
    return math.log2(n).is_integer()


print(is_power_of_two(16))
