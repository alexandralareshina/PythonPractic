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
from collections import deque

#pets = {1:{"Мухтар": {"Вид питомца": "Собака","Возраст питомца": 9,"Имя владельца": "Павел"},},
#        2:{"Каа": {"Вид питомца": "желторотый питон","Возраст питомца": 14,"Имя владельца": "Саша"},},}

def info(a):
    for key, value in a.items():
        if isinstance(value, dict):
            print(key)
            info(value)

def get_suffix(a):
    # адаптация год, года или лет для возраста
    if a >= 10 and a <= 20 and a == 11:
        ag = str(a) + ' лет'
    elif (a % 10) == 1 :
        ag = str(a) + ' год'
    elif (a % 10) > 1 and a % 10 < 5 :
        ag = str(a) + ' года'
    else:
        ag = str(a) + ' лет'
    return ag

def create():
    last.append(last[0] + 1)
    id = last[0]
    name = input('Имя питомца: ')
    vid = input('Вид питомца: ')
    age = int(input('Возраст питомца: '))
    vlad = input('Имя владельца: ')
    # заполнение словаря
    pets[id] ={name : {'Вид питомца': vid, 'Возраст питомца': age, 'Имя владельца': vlad}}
    print(f'Питомец {name} успешно добавлен в базу!')


def read():
    if len(pets) == 0:
        print('Нет питомцев!')
    else:
        info(pets)
        print('Введите id питомца для просмотра информации: ')
        kl = int(input())
        if kl in pets.keys():
            # присвоение значений словаря переменным для вывода
            m = list(pets.get(kl).keys())
            n = m[0]
            res = list(pets[kl][n].values())
            v = res[0]
            a = res[1]
            vl = res[2]
            print(f'Это {v} по кличке {n}. Возраст питомца: {get_suffix(a)} . Имя владельца: {vl}.')
        else:
            print('Такого питомца нет в базе. Введите add для добавления!')

def update():
    if len(pets) == 0:
        print('Нет питомцев!')
    else:
        info(pets)
        print('Введите id питомца для изменения информации: ')
        kl = int(input())
        if kl in pets.keys():
            del pets[kl]
            print('Введите новые данные o питомце:')
            name = input('Имя питомца: ')
            vid = input('Вид питомца: ')
            age = int(input('Возраст питомца: '))
            vlad = input('Имя владельца: ')
            pets[kl] = {name :{'Вид питомца': vid, 'Возраст питомца': age, 'Имя владельца': vlad}} 
            print(f'Данные питомца {kl} изменены!')
        else:
            print('Такого питомца нет в базе!')

def delete():
    if len(pets) == 0:
        print('Нет питомцев!')
    else:
        info(pets)
        print('Введите id питомца для удаления: ')
        kl = int(input())
        if kl in pets.keys():
            pets.pop(kl)
            print(f'Питомец {kl} удален из базы.')
        else:
            print('Такого питомца нет в базе.')


def get_pet():
    if len(pets) == 0:
        print('Нет питомцев!')
    else:
        print('Введите id питомца:')
        print(pets.keys())
        kl = int(input())
        if kl in pets.keys():
            print(pets.items())
        else:
            print(False)




def pets_list():
    if len(pets) == 0:
        print('Нет питомцев!')
    else:
        for i in pets.keys():
            for j in pets[i].keys():
                for p in pets[i].values():
                    print(i,' - ', j,'\n', p, '\n')



last = deque([0], maxlen=1)
pets = dict()
n = 1000
for i in range(n):
    print('Введите команду:')
    print('create - добавить питомца, read - просмотр информации o питoмцe, update - обновить информацию o питомце, delete - удалить питомца, get - получить инфоормвцию по id, list - просмотр всей базы, stop - завершить программу')

    command = input()
    if command == 'create' :
        create()
    elif command == 'read':
        read()
    elif command == 'update':
         update()
    elif command == 'delete':
        delete()
    elif command == 'get':
        get_pet()
    elif command == 'list':
        pets_list()
    elif command == 'stop':
        sys.exit('Завершение программы')
    else:
        print('Неверная команда!')
