def hamming_distance(s1, s2):
    result = len(s1)
    for sym1, sym2 in zip(s1, s2):
        if sym1 == sym2:
            result -= 1

    return result


print(hamming_distance('abbcace', 'abacacc'))
