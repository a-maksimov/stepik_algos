def avg_values(nums):
    if not nums:
        return []

    avg_values_list = [nums[0]]
    current_sum = nums[0]
    for i, num in enumerate(nums[1:], start=1):
        current_sum += nums[i]
        avg_value = current_sum / (i + 1)
        avg_values_list.append(avg_value)

    return avg_values_list


print(avg_values([10, 20, 30, 40, 50]))
