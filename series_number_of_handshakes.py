def number_of_handshakes(n):
    # n * (n - 1) // 2
    return n * n // 2 - n // 2


print(number_of_handshakes(5))  # 10
print(number_of_handshakes(6))  # 15
