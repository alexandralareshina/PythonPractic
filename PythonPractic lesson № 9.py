# ЗАДАНИЕ 1

# n = int(input('Введите число от 1 до 100000 :'))
# print(f'Введите {n} чисел через пробел:')
# a = set(map(int,input().split(maxsplit=n)))
# print(f'В множестве различных чисел - {len(a)} ')

# ЗАДАНИЕ 2

# print('Введите числа в первый список:')
# f = set(map(int,input().split()))
# print('Введите числа во второй список:')
# s = set(map(int,input().split()))
# print(len(f & s))

# ЗАДАНИЕ 3

print('Введите числа через пробел: ')
f = list(map(int,input().split()))
s = set()
for i in range(len(f)):
    if f[i] in s :
        print(f'{f[i]} - yes')
    else:
        print(f'{f[i]} - no')
    s.add(f[i])



