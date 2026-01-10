# def get_exam_position(n, k):
#     queue = list(range(1, n + 1, 2)) + list(range(2, n + 1, 2))
#     return queue.index(k) + 1


def get_exam_position(n, k):
    if k % 2 == 0:
        return k // 2 + (n + 1) // 2
    return (k + 1) // 2


print(get_exam_position(10, 10))    # очередность: 1 3 5 7 9 2 4 6 8 10
