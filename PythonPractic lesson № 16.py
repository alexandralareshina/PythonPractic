# ЗАДАНИЕ 1

# class Kassa(object):
#     cash = 0
#     def top(self, x):
#         self.cash += x
#     def count_1000(self):
#         return self.cash // 1000
#     def take_away(self, x):
#         if self.cash < x:
#             print('Недостаточно средств!')
#         else:
#             self.cash -= x

# kas = Kassa()
# n = 1000
# for i in range(n):
#     print('Введите команду : top - пополнить кассу, count - узнать сколько целых тысяч в кассе, take - взять из кассы, cash - остаток в кассе')
#     com = input()
#     if com == 'top':
#         x = int(input('Введите сумму для пополнения: '))
#         kas.top(x)
#     elif com == 'count':
#         print(kas.count_1000())
#     elif com == 'take':
#         x = int(input('Введите сумму, сколько хотите взять: '))
#         kas.take_away(x)
#     elif com == 'cash':
#         print(kas.cash)
#     else:
#         print('Неверная команда!')

# ЗАДАНИЕ 2
import sys

class Cherepashka(object):
    x = 1
    y = 1
    s = 1
    cnt = 0
    
    def go_up(self):
        self.y += self.s
        print(f'x = {self.x}, y = {self.y}, ход - {self.s}')
    def go_down(self):
        self.y -= self.s
        print(f'x = {self.x}, y = {self.y}, ход - {self.s}')
    def go_left(self):
        self.x -= self.s
        print(f'x = {self.x}, y = {self.y}, ход - {self.s}')
    def go_right(self):
        self.x += self.s
        print(f'x = {self.x}, y = {self.y}, ход - {self.s}')
    def evolve(self):
        self.s +=1
        print(f'x = {self.x}, y = {self.y}, ход - {self.s}')
    def degrade(self):
        if self.s == 1:
            print('Ошибка! количество клеток за 1 ход не может быть меньше 1!')
        else:
            self.s -= 1
            print(f'x = {self.x}, y = {self.y}, ход - {self.s}')
    def count_moves(self):
        while self.x < (self.x * 2) and (self.y < self.y):
            self.cnt = 0
            if self.s > self.x:
                for i in range(self.s - self.x):
                    self.s.degrade()
                    self.cnt += 1
            if self.s > self.y:
                for i in range(self.s - self.y):
                    self.s.degrade()
                    self.cnt += 1
            if self.s == self.x:
                self.cnt += 1
            if self.s == self.y:
                self.cnt += 1
            if self.s + self.x < self.x * 2:
                self.x.go_right()
                self.cnt += 1
            if self.s + self.y < self.y * 2:
                self.y.go_up()
                self.cnt += 1
            if self.s + self.x > self.x * 2:
                for i in range((self.x * 2) - self.x):
                    self.s.degrade()
                    self.cnt += 1
            if self.s + self.y > self.y * 2:
                for i in range((self.y * 2) - self.y):
                    self.s.degrade()
                    self.cnt += 1
        return print(f'Необходимо ходов - {self.cnt} ')


game = Cherepashka()
n = 1000
for i in range(n):
    print('Введите команду: up - вверх, down - вниз, left - в лево, right - в право, h+ - увеличить число клеток за один ход на 1, h- - уменьшить число клеток за один ход на 1, count - минимальное количество ходов до х2 у2, exit - завершить программу')
    com = input()
    if com == 'up':
        game.go_up()
    elif com == 'down':
        game.go_down()
    elif com == 'left':
        game.go_left()
    elif com == 'right':
        game.go_right()
    elif com == 'h+':
        game.evolve()
    elif com == 'h-':
        game.degrade()
    elif com == 'count':
        game.count_moves()
    elif com == 'exit':
        sys.exit('Завершение программы')
    else:
        print('Неверная команда!')