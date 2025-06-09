import math


def iterated_log(n):
    def do_iterate_log(_n, count):
        if _n <= 1:
            return _n, count

        count += 1
        new_n = math.log2(_n)
        return do_iterate_log(new_n, count)

    _, result = do_iterate_log(n, 0)

    return result


print(iterated_log(3))