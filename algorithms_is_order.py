def is_order(nums, strict=True):
    decreasing = True
    increasing = True

    for i, num in enumerate(nums[1:], start=1):
        previous = nums[i - 1]

        if strict:
            increasing_condition = num > previous
            decreasing_condition = num < previous
        else:
            increasing_condition = num >= previous
            decreasing_condition = num <= previous

        if not decreasing_condition:
            decreasing = False
        if not increasing_condition:
            increasing = False

        if not (increasing or decreasing):
            return False

    return increasing or decreasing


print(is_order([1, 2, 3, 4, 5], strict=True))
print(is_order([-2, -1, 1, 2, 2, 3, 5], strict=False))  # True


