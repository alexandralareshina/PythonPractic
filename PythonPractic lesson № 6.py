 ## ЗАДАНИЕ 1

#print('Введите количество чисел')
#n = int(input())
#cnt = 0
#print('Введите', n, 'чисел')
#for i in range(n) :
#    m = int(input())
#    if m == 0:
#        cnt+=1
#print("Количество нулей -", cnt)

## ЗАДАНИЕ 2

#print('Введите число больше 0')
#x = int(input())
# ## cnt счетчик чисел равно 2 т.к. уже туда уже учтены 1 и само число
#cnt = 2
#for i in range(2, int((x/2)+1)) :
#    if x % i ==0:
#        cnt += 1
#print('Количество делителей числа', x , '-', cnt)

## ЗАДАНИЕ 3

print('Введите число А:')
a = int(input())
print('Введите число В:')
b = int(input())
if a < b :
    for i in range(a, b):
        if i % 2 == 0 :
            print(i, end=' ')
elif a == b :
    print('Числа равны')
else:
    print('Ошибка. Число А должно быть меньше или равно В')   
            