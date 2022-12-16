'''2 Задайте натуральное число N. Напишите программу, которая составит список простых 
множителей числа N.
*Пример*

- при N=236     ->        [2, 2, 59]
'''

user_number = int(input('Enter the value: '))


def num_multipliers(user_number):
    result_list = []
    div = 2
    while user_number / div != 1:
        if user_number % div == 0:
            user_number = user_number // div
            result_list.append(div)
        else:
            div += 1
    else:
        result_list.append(div)
    return result_list


res_nums = num_multipliers(user_number)
print(f'List of prime factors of a number {user_number} is {res_nums}')