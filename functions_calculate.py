def calculate(vars, values, exp):
    for var, value in zip(vars, values):
        exp = exp.replace(var, str(value))

    return eval(exp)


print(calculate('xyz', [1, 2, 3], 'x-y+z'))  # 1 - 2 + 3 = 2
