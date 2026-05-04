def max_consecutive_elements(n):
    if not n:
        return 0

    current_res = 1
    res = 1
    for sym1, sym2 in zip(n, n[1:]):
        if sym1 == sym2:
            current_res += 1
        else:
            current_res = 1

        if current_res > res:
            res = current_res

    return res


print(max_consecutive_elements('pyyythoooon'))  # oooo
print(max_consecutive_elements('bee'))  # ee
