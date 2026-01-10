def count_days(cur):
    if cur % 2 == 0:
        return 0

    days = 0
    while cur > 1:
        cur = (cur - 1) / 2

        days += 1

        if cur % 2 == 0:
            break

    return days


print(count_days(2))  # 0
print(count_days(5))  # 1
print(count_days(23))  # 3
print(count_days(10))  # 0
print(count_days(25))  # 1
