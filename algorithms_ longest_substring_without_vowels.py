def longest_substring_without_vowels(s):
    vowels = "aeiou"
    max_length = 0
    res = ""
    for sym in s:
        if sym in vowels:
            if len(res) > max_length:
                max_length = len(res)
            res = ""
        else:
            res += sym

    if len(res) > max_length:
        max_length = len(res)

    return max_length


# import re
#
# def longest_substring_without_vowels(s):
#     vowels = r'[aeiou]'
#     max_consonant = max(re.split(vowels, s), key=len)
#     return len(max_consonant)


print(longest_substring_without_vowels('ab'))
print(longest_substring_without_vowels('bcdgf'))
print(longest_substring_without_vowels('abecidofug'))
