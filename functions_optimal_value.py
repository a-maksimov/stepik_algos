def optimal_value(nums):
    return sum(nums) / len(nums)


print(optimal_value([1, 2, 9, 2, 6]))  # (1 - 4)^2 + (2 - 4)^2 + (9 - 4)^2 + (2 - 4)^2 + (6 - 4)^2 = 46
