def wave(nums):
    for i, num in enumerate(nums, start=1):
        if i % 2 == 0:
            continue

        if i == len(nums):
            break

        nums[i - 1], nums[i] = nums[i], nums[i - 1]

    return nums


data = [1, 2, 3, 4, 5]
wave(data)
print(data)