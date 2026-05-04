def find_number(nums):
    length = len(nums)
    for i, num in enumerate(nums):
        if (i + 1) % 2 == 0:
            continue

        if i + 1 == length:
            return num

        next_num = nums[i + 1]
        if not num == next_num:
            return num


print(find_number([1, 1, 2, 3, 3]))
print(find_number([1, 1, 5, 5, 40, 60, 60]))
print(find_number([1, 1, 2, 2, 3, 3, 4]))
