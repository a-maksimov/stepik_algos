def drop_one_and_five(n):
    res = 0
    place = 1
    while n:
        digit = n % 10
        n //= 10
        if digit in [1, 5]:
            continue
        res += place * digit
        place *= 10

    return res


print(drop_one_and_five(527012))
