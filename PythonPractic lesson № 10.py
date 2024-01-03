# ЗАДАНИЕ 1

import sys
pets = dict()
n = 100  # количество операций
for i in range(n):
    print('Введите команду: add - добавить питомца, info - просмотр питомцев, exit - завершить : ')
    zapros = input()
    if zapros == 'add':
        # ввод нового питомца
        name = input('Имя питомца: ')
        vid = input('Вид питомца: ')
        age = int(input('Возраст питомца: '))
        vlad = input('Имя владельца: ')
        # заполнение словаря
        pets[name] = {'vid': vid, 'age': age, 'vlad': vlad}
    elif zapros == 'info':
        # просмотр информации
        if len(pets) == 0:
            print('Нет питомцев!')
        else:
            inf = list(pets.keys())
            print(*inf,sep=', ')
            print('Введите имя питомца для просмотра информации: ')
            kl = input()
            if kl in pets:
                # присвоение значений словаря переменным для вывода
                m = list(pets.get(kl).values())
                n = kl
                v = m[0]
                a = m[1]
                vl = m[2]
                # адаптация год, года или лет для возраста
                if a >= 10 and a <= 20 and a == 11:
                    ag = str(a) + ' лет'
                elif (a % 10) == 1 :
                    ag = str(a) + ' год'
                elif (a % 10) > 1 and a % 10 < 5 :
                    ag = str(a) + ' года'
                else:
                    ag = str(a) + ' лет'
                print(f'Это {v} по кличке {n}. Возраст питомца: {ag} . Имя владельца: {vl}.')
            else:
                print('Такого питомца нет в базе. Введите add для добавления!')
    elif zapros == 'exit':
        sys.exit('Завершение программы')
    else:
        print('Неверная команда! Введите add, info или exit!')


# ЗАДАНИЕ 2

# s = {}
# for i in range(10, -6, -1):
#     s[i] = pow(i, i)
# print(s)