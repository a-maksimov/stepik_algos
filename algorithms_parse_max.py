def parse_max(s):
    num_string = ""
    max_number = -1
    for sym in s:
        if sym.isdigit():
            num_string += sym
        else:
            if num_string:
                number = int(num_string)
                if number > max_number:
                    max_number = number
                num_string = ""
    if num_string:
        return max(max_number, int(num_string))
    return max_number


print(parse_max('100klh564abc365bg'))
print(parse_max('0'))


# import re
#
# def parse_max(line):
#     nums = re.findall(r'\d+', line)
#     if nums:
#         return max(map(int, nums))
#     return -1