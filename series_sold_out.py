# def sold_out(n, m):
#     i = 1
#     p = n
#     s = m
#
#     sm = s - p
#     while sm >= 0:
#         sm += m
#         p = n + i
#         sm = sm - p
#         i += 1
#
#     return i


def sold_out(n, m):
    if m < n:
        return 1
    return 2 * (m - n) + 2


print(sold_out(10, 5))  # 1
print(sold_out(1, 10))  # 20
print(sold_out(4, 5))  # 4
