def sum_of_squares(n):
    res = 0
    for i in range(1, n + 1):
        square = i*i
        res += square
    return res

