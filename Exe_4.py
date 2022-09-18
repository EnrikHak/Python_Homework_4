#   Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100)
#   многочлена и записать в файл многочлен степени k.

#   Пример:
#   k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

#   !!! Эту задачу я совсем не понял. Искал и брал с готового решения !!!
 
from random import randint

k = int(input('Введите натуральную степень: '))
polynom = ''
for i in range(k, -1, -1):
    koeficient = randint(0, 100)
    if koeficient != 0:
        if i == 1:
            polynom += f'{koeficient} * x + '
        elif i > 1:
            polynom += f'{koeficient} * x ** {i} + '
        else:
            polynom += f'{koeficient}'
polynom += ' = 0'
print(polynom)