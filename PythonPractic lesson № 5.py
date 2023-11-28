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

print('Введите слово латинскими буквами:')
slovo = input()
slovo = slovo.lower()
vse_gls = ["a", "e", "i", "o", "u", "y"]
gls = 0
sgls = 0
a = e = i = o = u = y = 0
for j in slovo :
    if j in vse_gls:
        gls += 1
    else:
        sgls += 1
    if j == vse_gls[0] :
        a += 1
    elif j == vse_gls[1] :
        e += 1
    elif j == vse_gls[2] :
        i += 1
    elif j == vse_gls[3] :
        o += 1
    elif j == vse_gls[4] :
        u += 1
    elif j == vse_gls[5] :
        y += 1
if a == 0 :
    a = False
if e == 0 :
    e = False
if i == 0 :
    i = False
if o == 0 :
    o = False
if u == 0 :
    u = False
if y == 0 :
    y = False
print (f'a - {a},e - {e}, i - {i},o - {o}, u - {u}, y - {y}')
print(f'В слове {slovo} гласных - {gls}, согласных - {sgls}')

## ЗАДАНИЕ 3

# print('Введите минимальную сумму инвестиций')
# min_sum = int(input())
# print('Введите сумму Майкла')
# a = int(input())
# print('Введите сумму Ивана')
# b = int(input())

# if (a >= min_sum) and (b >= min_sum) :
#     print(2)
# elif ((a + b) < min_sum) :
#     print(0)
# elif (a < min_sum) and (b < min_sum) and ((a + b) >= min_sum) :
#     print(1)
# elif (a >= min_sum) and (b < min_sum) :
#     print('Mike') 
# else:
#     (a < min_sum) and (b >= min_sum)
#     print('Ivan')
