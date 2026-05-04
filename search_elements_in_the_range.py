def elements_in_the_range(nums, start, end):
    nums_set = set(nums)
    for num in range(start, end + 1):
        if num not in nums_set:
            return False

    return True


print(elements_in_the_range([1, 3, 5, 2, 7, 8, 4], 2, 6))  # список не содержит число 6
print(elements_in_the_range([1, 1, 1, 1, 1, 1], 1, 1))  # список содержит все числа от 1 до 1
