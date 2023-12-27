# ЗАДАНИЕ 1

import random

def create_matrix(x, y):
    return [[random.randint(-200, 200) for i in range(y)] for j in range(x)]

def pl(t):
    for i in t:
        print(i)

x = int(input('Введите первое число: '))
y = int(input('Введите второе число: '))
matrix_1 = create_matrix(x, y)
matrix_2 = create_matrix(x, y)

print('Матрица 1:')
pl(matrix_1)
print('Матрица 2:')
pl(matrix_2)

matrix_3 = create_matrix(x, y)
for i in range(len(matrix_1)):
    for j in range(len(matrix_1[0])):
        matrix_3[i][j] = matrix_1[i][j] + matrix_2[i][j]

print('Матрица 3:')
pl(matrix_3)