# def count_solutions(n):
#     counter = 0
#     for x in range(1, n + 1):
#         for y in range(1, n + 1):
#             for z in range(1, n + 1):
#                 if 3*x + 2*y + z == n:
#                     counter += 1
#     return counter


def count_solutions(n):
    counter = 0
    for x in range(1, n + 1):
        for y in range(1, n + 1):
            if n - 3 * x - 2 * y > 0:
                counter += 1
    return counter


print(count_solutions(8))    # 3x + 2y + z = 8 -> 2


def count_solutions(n):
    count = 0
    for x in range(1, n // 3 + 1):
        for y in range(1, (n - 3 * x) // 2 + 1):
            z = n - 3 * x - 2 * y
            if z > 0:
                count += 1
    return count


# O(1)
# def s3(k):
#     """ calculate k + (k-3) + (k-6) + ... as long as the summands remain positive """
    # последнее слагаемое: k % 3 (ничего страшного, если оно равно нулю, а не больше нуля)
    # полусумма первого и последнего слагаемых: (k + k%3) / 2
    # число слагаемых (включая k % 3, даже если оно нулевое): 1 + k // 3
#     return (1 + k // 3) * (k + k%3) // 2
#
#
# def count_solutions(n):
#     a = (n - 4) // 2
#     b = (n - 7) // 2
#     return s3(a) + s3(b)
