
## ЗАДАНИЕ 1

# n = int(input('Введите число: '))
# # создаем список
# s = []
# if n >= 1 and n <= 10000:
#     # заполняем список числами
#     print(f'Введите {n} чисел :')
#     for i in range(n) :
#        a = int(input())
#        s.append(a)
#     s.reverse()
#     print(*s)
# else:
#     print('Ошибка. Введите число от 1 до 10000')

## ЗАДАНИЕ 2

# n = int(input('Введите число: '))
# if n >= 1 and n <= 10000 :
#     print(f'Введите {n} чисел от 1 до 10000:')
#     sp = list(map(int, input().split()))
#     if len(sp) != n:
#         print(f'Нужно было ввести {n} чисел от 1 до 10000:')
#     else:
#         a = sp[-1]
#         sp.insert(0, a)
#         sp.pop()
#         print(*sp)
# else:
#     print('Ошибка. Нужно было ввести число от 1 до 10000')   


# ЗАДАНИЕ 3

print('Введите максимальную грузоподьемность лодки:')
m = int(input())
print('Введите количество рыбаков:') 
n = int(input())
s = [int(input(f'Введите вес рыбака {i + 1}: ')) for i in range(n)]
s.sort(reverse=True)
lodki = 0
i = 0
if m >= 1 and m <= 10000 and n >= 1 and n <= 100 :
    if s[i] >= 1 and s[i] <= m :
        while i < n :
            if (i + 1) < n and (s[i] + s[i + 1]) <= m:
                i +=2
            else:
                i +=1
            lodki +=1
    else:
        print('Ошибка! Введены некорректные значения веса рыбаков!')   
else:
    print('Ошибка! Введены некорректные значения грузоподъемности или количества рыбаков!')

print(lodki)

## Работает некорректно. не получается сделать
