'''Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов 
списка, стоящих на нечётной позиции.

Пример:

- [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
'''

import random

print('Enter the size of the list: ')
list_length = int(input())

list = []


def new_list_creation(lst, list_length):
    for i in range(list_length):            
        new_number = random.randint(0,15)
        lst.append(new_number) 

new_list_creation(list, list_length)
print(f'The list is: {list}')

#old code
# def sum_of_odds(list, list_length):
#     sum = 0
#     for i in range(1,list_length,2):
#         sum = sum + list[i]
#     return sum    


# summa = sum_of_odds(list, list_length)  
# print('The result is', summa)

#new code (v.1)
odds_list = list[1::2]
odds_sum = sum(odds_list)
print(odds_sum)

#or this one (v. 2)
odds = sum([x for i, x in enumerate(list) if i % 2])
print(odds)