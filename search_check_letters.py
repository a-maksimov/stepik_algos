import string


def check_letters(s):
    result = ['0'] * 26
    alphabet = string.ascii_lowercase
    for sym in s:
        norm_sym = sym.lower()
        if norm_sym not in alphabet:
            continue

        num = ord(norm_sym) - 97
        result[num] = '1'

    return ''.join(result)


print(check_letters('b*e*e*g*e*e*k'))


# def check_letters(s):
#     result = ''
#     s = s.lower()
#     for letter in 'abcdefghijklmnopqrstuvwxyz':
#         if letter in s:
#             result += '1'
#         else:
#             result += '0'
#     return result
