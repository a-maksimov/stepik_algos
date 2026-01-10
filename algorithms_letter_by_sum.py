def letter_by_sum(letters):
    ref = ord("a") - 1
    ord_sum = 0
    for letter in letters:
        num = ord(letter) - ref
        ord_sum += num

        if ord_sum > 26:
            ord_sum -= 26

    return chr(ord_sum + ref)


print(letter_by_sum(['b', 'y']))
print(letter_by_sum(['z', 'z']))