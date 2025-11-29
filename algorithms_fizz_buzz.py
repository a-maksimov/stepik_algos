def fizz_buzz(n):
    res = []
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            res.append("FizzBuzz")
        elif i % 3 == 0:
            res.append("Fizz")
        elif i % 5 == 0:
            res.append("Buzz")
        else:
            res.append(i)
    return res


print(fizz_buzz(15))


# def fizz_buzz(num):
#     res = []
#     for i in range(1, num+1):
#         s = ''
#         if i % 3 == 0:
#             s += 'Fizz'
#         if i % 5 == 0:
#             s += 'Buzz'
#         res.append(s if s else i)
#     return res
