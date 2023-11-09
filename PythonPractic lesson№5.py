## ЗАДАНИЕ 1

##val = int(input())
#
#if val == 0:
#    print('нулевое значение')
#elif val > 0 :
#    if val % 2 == 0 :
#        print(val, '- положительное четное число')
#    else:
#        print(val, '- положиетльное нечетное число')
#else:
#    if val % 2 ==0 :
#        print(val, '- отрицательное четное число')
#    else:
#        print(val, '- отрицательное нечетное число')

## ЗАДАНИЕ 2

## непонимаю как решить

## ЗАДАНИЕ 3

print('Введите минимальную сумму инвестиций')
min_sum = int(input())
print('Введите сумму Майкла')
a = int(input())
print('Введите сумму Ивана')
b = int(input())

if (a >= min_sum) and (b >= min_sum) :
    print(2)
elif ((a + b) < min_sum) :
    print(0)
elif (a < min_sum) and (b < min_sum) and ((a + b) >= min_sum) :
    print(1)
elif (a >= min_sum) and (b < min_sum) :
    print('Mike') 
else:
    (a < min_sum) and (b >= min_sum)
    print('Ivan')
