def swap_digits(num):
    return int(''.join(reversed(str(num))))


# def swap_digits(number):
#     a = number // 100
#     b = number // 10 % 10
#     c = number % 10
#     new_number = c * 100 + b * 10 + a
#     return new_number