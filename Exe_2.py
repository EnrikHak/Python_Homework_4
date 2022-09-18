#   Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.


N = int(input('Введите натуральное число: '))

#   Делим число на 2, полученное число тоже делим на 2 и так далее...пока не наткнемся на число которое не делится на 2
#   Если число не делится на 2, то добавляем +1 от 2 до самого числа.

spisokOfNumber = []
divid = 2
while N >= divid:
    if N % divid == 0:
        spisokOfNumber.append(divid)
        N = N / divid
    else:
        divid += 1
if N > 1:
    spisokOfNumber.append(N)
print(spisokOfNumber)