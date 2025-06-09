import math


def is_power_of_four(n):
    return math.log(n, 4).is_integer()


print(is_power_of_four(16))
