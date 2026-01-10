# def calculate_sum(n):
#     result, cur_value = 0, 1
#     for _ in range(n):
#         result += cur_value
#         cur_value += 2
#     return result


def calculate_sum(n):
    an = 1 + (n - 1) * 2
    return int(((1 + an) / 2) * n)


print(calculate_sum(100))   # 1 + 3 + 5 + 7 + 9 + ... + 199
