def is_point_in_rectangle(p, rect):
    x1, y1 = rect[0]
    x2, y2 = rect[1]
    x, y = p
    if x1 < x < x2 and y1 < y < y2:
        return True

    return False


print(is_point_in_rectangle((2, 2), [(1, 1), (3, 4)]))
