#   Пользователь вводит число, Вам необходимо вывести число Пи с той точностью знаков после запятой,
#   сколько указал пользователь(БЕЗ ИСПОЛЬЗОВАНИЯ МОДУЛЕЙ/БИБЛИОТЕК)


n = int(input('Введите число знаков после запятой: '))

Pi = (1/16**0) * (4/(8 * 0 + 1) - 2/(8 * 0 + 4) - 1/(8 * 0 + 5) - 1/(8 * 0 + 6))

for i in range(1, n):
    Pi += (1/16**i) * (4/(8 * i + 1) - 2/(8 * i + 4) - 1/(8 * i + 5) - 1/(8 * i + 6))
print(round(Pi, n))