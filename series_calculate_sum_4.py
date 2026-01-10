def calculate_sum(n):
    if n % 2 == 0:
        return -n ** 2 // 2 - n // 2
    return n ** 2 // 2 + n // 2 + 1


print(calculate_sum(9))    # 1 - 4 + 9 - 16 + 25 - 36 + 49 - 64 + 81 => 45
print(calculate_sum(10))    # 1 - 4 + 9 - 16 + 25 - 36 + 49 - 64 + 81 - 100 => -55


def calculate_sum(n):
    if n % 2 == 0:
        return - n * (1 + n) // 2
    return n * n - n * (n - 1) // 2
