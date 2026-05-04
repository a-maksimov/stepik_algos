def count_numbers(n, k):
    result = 0
    for number in range(1, n + 1):
        s = sum(map(int, str(number)))
        if not number - s >= k:
            continue

        result += 1

    return result


print(count_numbers(13, 2))    # 10, 11, 12, 13
print(count_numbers(10, 15))
