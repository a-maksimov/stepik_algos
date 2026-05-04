def nine_divisors(n):
    result = 0
    for number in range(1, n + 1):
        divisors_num = 2
        for i in range(2, number):
            if number % i:
                continue

            divisors_num += 1

        if not divisors_num == 9:
            continue

        result += 1

    return result


print(nine_divisors(100))     # 36, 100
print(nine_divisors(500))
