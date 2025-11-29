def time_zone(h, a, b):
    total_hours = h - a + b
    return total_hours % 24


print(time_zone(12, 3, 7))

print(time_zone(12, -4, 4))

print(time_zone(6, -11, 12))