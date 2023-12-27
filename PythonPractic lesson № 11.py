# ЗАДАНИЕ 1

# def factorial(n):
#     f = 1
#     while n > 1:
#         f *= n
#         n -= 1
#     return f

# def fac(x):
#     f = 1
#     s = []
#     while x > 0:
#         s.insert(0, f)
#         f *= x 
#         x -=1
#     return s

# n = int(input('Введите положительное целое число: '))
# a = factorial(n)
# print(f'Факториал числа {n} равен {a}')
# print(fac(a))


# ЗАДАНИЕ 2

import sys
import pprint
#import collections
#pets = {1:{"Мухтар": {"Вид питомца": "Собака","Возраст питомца": 9,"Имя владельца": "Павел"},},
#        2:{"Каа": {"Вид питомца": "желторотый питон","Возраст питомца": 14,"Имя владельца": "Саша"},},}

def get_suffix(a):
    # адаптация год, года или лет для возраста
    if (a % 10) == 1 :
        ag = str(a) + ' год'
    elif a >= 10 and a <= 20:
        ag = str(a) + ' лет'
    elif (a % 10) > 1 and a % 10 < 5 :
        ag = str(a) + ' года'
    else:
        ag = str(a) + ' лет'
    return ag

def create():
    name = input('Имя питомца: ')
    vid = input('Вид питомца: ')
    age = int(input('Возраст питомца: '))
    vlad = input('Имя владельца: ')
    # заполнение словаря
    pets[name] = {'Вид питомца': vid, 'Возраст питомца': age, 'Имя владельца': vlad}
    #last = collections.deque(pets, maxlen = 1)[0]  # непонимаю как с этим работать = IndexError: deque index out of range

    print(f'Питомец {name} успешно добавлен в базу!')


def read():
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

            print(f'Это {v} по кличке {n}. Возраст питомца: {get_suffix(a)} . Имя владельца: {vl}.')
        else:
            print('Такого питомца нет в базе. Введите add для добавления!')

def update():
    read()
    print('Введите новые данные o питомце:')
    name = input('Имя питомца: ')
    vid = input('Вид питомца: ')
    age = int(input('Возраст питомца: '))
    vlad = input('Имя владельца: ')
    pets[name] |= {'Вид питомца': vid, 'Возраст питомца': age, 'Имя владельца': vlad}
    if name in pets:
        print(f'Данные питомца {name} изменены!')
    else:
        print('Такого питомца нет в базе!')

def delete():
    if len(pets) == 0:
        print('Нет питомцев!')
    else:
        inf = list(pets.keys())
        print(*inf,sep=', ')
        print('Введите имя питомца для удаления: ')
        kl = input()
        if kl in pets:
            pets.pop(kl)
            print(f'Питомец {kl} удален из базы.')
        else:
            print('Такого питомца нет в базе.')


# def get_pet(ID):




def pets_list():
    for key, val in pets.items():
        pp = pprint.PrettyPrinter(indent=4)
        pp.print(key, val)


pets = dict()
n = 1000
for i in range(n):
    print('Введите команду:')
    print('create - добавить питомца, read - просмотр информации o питoмцe, update - обновить информацию o питомце, delete - удалить питомца, list - просмотр всей базы, stop - завершить программу')

    command = input()
    if command == 'create' :
        create()
    elif command == 'read':
        read()
    elif command == 'update':
         update()
    elif command == 'delete':
        delete()
    elif command == 'list':
        pets_list()
    elif command == 'stop':
        sys.exit('Завершение программы')
