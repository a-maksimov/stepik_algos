from itertools import dropwhile


def one_truth(flags):
    res = False
    drop = dropwhile(lambda f: f is False, flags)
    flag = next(drop, False)
    if not flag:
        return res

    for flag in drop:
        if flag:
            return res

    return not res


print(one_truth([True, False, False]))
print(one_truth([False, False, False, False, False]))
print(one_truth([True, True, True, True, True, True]))