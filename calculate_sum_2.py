def calculate_sum(n):
    return int(((n ** 2) / 2) + (n / 2))


print(calculate_sum(10))   # 100 - 81 + 64 - 49 + 36 - 25 + 16 - 9 + 4 - 1 = 55
print(calculate_sum(5))    # 25 - 16 + 9 - 4 + 1 = 15


# def calculate_sum(n):
#     return n * (1 + n) // 2
