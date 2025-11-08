def mystery(n):
    nums = ['0', '6', '9']
    nums_2 = ['8']
    res = 0
    for digit in str(n):
        if digit in nums:
            res += 1
        elif digit in nums_2:
            res += 2

    return res

