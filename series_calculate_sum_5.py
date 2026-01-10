def calculate_sum(n):
    return 2 ** (n + 1) - 1


print(calculate_sum(6))    # 1 + 2 + 4 + 8 + 16 + 32 + 64 => 127
print(calculate_sum(10))    # 1 + 2 + 4 + 8 + 16 + 32 + 64 + 128 + 256 + 512 + 1024 => 2047


def calculate_sum(n: int) -> int:
    return (1 << n + 1) - 1
