def find_peaks(nums):
    result = 0
    length = len(nums)
    for i, num in enumerate(nums):
        if i == 0:
            continue

        if i + 1 == length:
            break

        prev_number = nums[i - 1]
        next_number = nums[i + 1]

        if not (num > prev_number and num > next_number):
            continue

        result += 1

    return result


print(find_peaks([16, 7, 18, 12, 13, 11, 19, 9, 10, 6]))  # 18, 13, 19 и 10
