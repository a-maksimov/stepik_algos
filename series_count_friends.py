def count_friends(k):
    D = 1 + 8 * k
    n1 = (1 + D ** 0.5) // 2
    return int(n1)


print(count_friends(21))  # 7
print(count_friends(45))  # 10
