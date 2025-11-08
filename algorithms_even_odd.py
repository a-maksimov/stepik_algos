def even_odd(nums):
    if all(num % 2 == 0 for num in nums) or all(num % 2 != 0 for num in nums):
        return True
    return False


print(even_odd([1, 3, 5, 7]))
