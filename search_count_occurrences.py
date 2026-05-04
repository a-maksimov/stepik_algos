def count_occurrences(nums, target, start, end):
    result = 0
    for i, num in enumerate(nums):
        if i < start:
            continue

        if i >= end:
            break

        if not num == target:
            continue
        result += 1

    return result


# print(count_occurrences([7, 2, 7, 1], 7, 0, 4))  # число 7 в подсписке [7, 2, 7, 1]
print(count_occurrences([4, 2, 1, 5, 7], 4, 0, 0))  # число 4 в подсписке []