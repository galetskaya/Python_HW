'''1 Вычислить число π c заданной точностью d
*Пример:* 

- при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$
'''

d = float(input('Enter "d": '))


def calc_pi(user_number):
    res_1 = 0
    res_2 = 0
    degree = 0
    while user_number != 1:
        user_number *= 10
        degree += 1
    for i in range(1, 10 ** degree, 2):
        res_1 = res_2 + (4 / (2 * i - 1))
        res_2 = res_1 - (4 / (2 * (i + 1) - 1))
    number_pi = str((res_1 + res_2) / 2)
    print(f'Result is : {number_pi[:degree + 2]}')


calc_pi(d)
