def min_digit_sum(a, b):
    res = 0
    min_sum = 1 << 30
    for num in range(a, b + 1):
        current_sum = 0
        while num:
            digit = num % 10
            num //= 10
            current_sum += digit
        if current_sum < min_sum:
            min_sum = current_sum
            res = 1
        elif current_sum == min_sum:
            res += 1
        else:
            continue

    return res


print(min_digit_sum(1, 50))

# from math import log10
#
#
# def min_digit_sum(a, b):
#     # сразу обработаем случай a = b
#     if a == b:
#         return 1
#
#     # если числа a и b разной длины, между ними есть степень десятки 10..00 с суммой цифр 1
#     # тогда возвращаем количество степеней 10 между (включительно!!) a и b
#     if int(log10(a)) != int(log10(b)):
#         return int(log10(b)) - int(log10(a)) + log10(a).is_integer()
#
#     # отбросим общий префикс чисел a и b; уже гарантировали a != b, поэтому что-то останется
#     pow10 = 10 ** int(log10(a))
#     while a // pow10 == b // pow10:
#         a %= pow10
#         b %= pow10
#         pow10 //= 10
#
#     # числа a и b одной длины и их первые цифры разные
#     # теперь если, например, a = 5**** и b = 6**** или 7**** или больше, есть два случая:
#     #   Case 1: a = 50000, минимальная сумма цифр равна 5, и только в одном варианте: 50000
#     #   Case 2: a > 50000, минимальная сумма равна 6,
#     # достигается на вариантах 60000 и, возможно, 51000, 50100, 50010, 50001
#
#     a %= pow10
#
#     # Case 1:
#     if a == 0:
#         return 1
#
#     # Case 2:
#     return int(log10(b)) - int(log10(a)) + log10(a).is_integer()
