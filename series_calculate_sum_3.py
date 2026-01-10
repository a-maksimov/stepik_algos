# def calculate_sum(n):
#     result = 0
#     for i in range(1, n + 1):
#         result += i**3
#     return result


def calculate_sum(n):
    s = n * (n + 1) // 2
    return s * s


print(calculate_sum(10))    # 1 + 8 + 27 + 64 + 125 + ... + 1000
print(calculate_sum(10**5))  # 25000500002500000000
