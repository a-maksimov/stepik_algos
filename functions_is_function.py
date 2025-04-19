def is_function(pairs):
    results = {}
    for arg, value in pairs:
        results[arg] = value

    return len(results) == len(pairs)


print(is_function([(1, 3), (2, 5), (3, 7)]))
