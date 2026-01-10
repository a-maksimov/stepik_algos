# def calculate_sum(n):
#     result, cur_value = 0, 1
#     for _ in range(n):
#         for _ in range(n):
#             result += cur_value
#             cur_value += 1
#     return result


def calculate_sum(n):
    return int(((1 + n ** 2) / 2) * (n ** 2))


print(calculate_sum(100))   # 1 + 2 + 3 + ... + 10000
print(calculate_sum(10))    # 1 + 2 + 3 + ... + 100
