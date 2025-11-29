def divisible(n):
    res = 0
    current_n = n
    while current_n:
        digit = current_n % 10
        current_n //= 10
        if digit:
            if n % digit == 0:
                res += 1
    return res


print(divisible(2340))
