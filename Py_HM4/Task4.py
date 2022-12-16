'''4. Задана натуральная степень k. Сформировать случайным образом список коэффициентов 
(значения от 0 до 100) многочлена и записать в файл многочлен степени k.
*Пример:* 

- k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
'''

import random


k = int(input('Введите степень: '))


def create_ratio(k):
    lst = []
    for i in range(k, -1, -1):
        d = random.randint(0, 100)
        if i == 0:
            lst.append(f'{d}')
        elif i == 1:
            lst.append(f'{d}x')
            lst.append('+')
        else:
            lst.append(f'{d}x^{i}')
            lst.append('+')
    lst.append('= 0')
    a = " ".join(map(str, lst))
    return(a)


new_a = create_ratio(k)
with open('Py_HM4/file1.txt', 'w', encoding='utf8') as file:
    file.write(new_a)