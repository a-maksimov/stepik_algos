def snake(n):
    horizontal = "*" * n
    right = True
    for i in range(n):
        left_to_right = i % 2 == 0

        if left_to_right:
            print(horizontal)
        else:
            if right:
                print(" " * (n - 1) + "*")
                right = False
            else:
                print("*")
                right = True


snake(4)
snake(10)


# def snake(n):
#     for i in range(n):
#         if i % 2 == 0:
#             print('*' * n)
#         elif i % 4 == 1:
#             print(' ' * (n - 1) + '*')
#         else:
#             print('*')
