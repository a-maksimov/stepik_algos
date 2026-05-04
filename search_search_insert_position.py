def search_insert_position(nums, target):
    idx = 0
    if nums[0] > target:
        return idx

    for i, num in enumerate(nums):
        if num == target:
            return i
        else:
            if num <= target:
                idx = i

    return idx + 1


print(search_insert_position([1, 2, 3, 4, 5], 5))  # 4
print(search_insert_position([1, 2, 3, 4, 5], 6))  # 5
print(search_insert_position([2, 3, 4, 5, 6], 1))  # 0


# def search_insert_position(nums, target):
#     for idx, num in enumerate(nums):
#         if num >= target:
#             return idx
#     return len(nums)
