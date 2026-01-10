def area_of_tree(n):
    branches = n * (n + 1)
    return branches + n * 2 + 1


print(area_of_tree(5))  # 41
