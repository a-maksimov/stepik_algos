def training_time(n, m, s, b):
    total_seconds = n * (m * 60) + n * s + (n - 1) * b
    minutes = total_seconds // 60
    seconds = total_seconds % 60
    return minutes, seconds


print(training_time(3, 2, 10, 90))
