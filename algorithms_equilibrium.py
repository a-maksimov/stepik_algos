def equilibrium(nums):
    res = -1
    if not nums:
        return res

    if len(nums) == 1:
        return 0

    for i, num in enumerate(nums):
        left_sum = sum(nums[:i])
        right_sum = sum(nums[i + 1:])
        if left_sum == right_sum:
            res = i
            break

    return res


print(equilibrium([1, 1, 1, 1, 1]))  # 2
print(equilibrium([1, 3, 5, 2, 2]))  # 2
print(equilibrium([1]))  # 0
print(equilibrium([1, 2]))  # -1
print(equilibrium([4, 0, 0]))  # 0

data = [0, 0, 0]
print(equilibrium(data))  # 0

data = [1, 0]
print(equilibrium(data))  # 0

data = [0, 10]
print(equilibrium(data))  # 1

