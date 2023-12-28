# ЗАДАНИЕ 1

def rec(x):
    if len(x) == 0:
        print('Конец списка')
    else:
        print(x[0])
        rec(x[1:])

my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
rec(my_list)