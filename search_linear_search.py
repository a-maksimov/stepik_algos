def linear_search(nums, target, reverse=False):
    if reverse:
        start, end, step = len(nums) - 1, -1, -1
    else:
        start, step, end = 0, 1, len(nums)

    for i in range(start, end, step):
        if nums[i] == target:
            return i

    return -1


# print(linear_search([-2, 1, 7, -2], -2, reverse=True))  # 3
# print(linear_search([2, 1, 7, 2], 2))  # 0
# print(linear_search([2, 3], 3, reverse=False))  # 1
# print(linear_search([1], 1, reverse=True))  # 0
print(linear_search([2, 3], 2, reverse=True))  # 0
