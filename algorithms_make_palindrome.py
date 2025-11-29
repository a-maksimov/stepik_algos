from math import log10, floor


def reverse_number(n):
    res = 0
    digits = floor(log10(n)) + 1
    place = 10 ** (digits - 1)
    while n:
        digit = n % 10
        n //= 10
        res += digit * place
        place //= 10
    return res


def make_palindrome(n):
    for _ in range(6):
        reversed_n = reverse_number(n)
        if reversed_n == n:
            return n
        n += reversed_n

    return -1


print(make_palindrome(23))
print(make_palindrome(166))