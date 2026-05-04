def equal(nums):
    for i, num in enumerate(nums):
        if num == i:
            return i
    return -1


print(equal([2, 9, 4, 8]))  # -1
print(equal([10, 7, 2]))  # 2


