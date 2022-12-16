'''Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной 
части элементов.

Пример:

- [1.1, 1.2, 3.1, 5, 10.01] => 0.19
'''

import random


print('Enter the size of the list: ')
list_length = int(input())


def new_real_list_creation(list_length):         #функция создает новый список дробных чисел
    lst = []
    for i in range(list_length):            
        new_number = round(random.random() * 10, 2)
        lst.append(new_number)
    return(lst) 

list = new_real_list_creation(list_length)
print('The list is: ')
print(list)


def fractional_output(list):                      #функция извлекает дробную часть и создает новый список
    lst2 = []
    for i in range(len(list)):
        res = round((list[i] % 1), 2)
        lst2.append(res)
    return lst2


lst2 = fractional_output(list)

max_ = 0
min_ = 1


for i in range(list_length):
    if lst2[i] >= max_ and lst2[i] != 0:
         max_ = lst2[i]
    elif lst2[i] <= min_ and lst2[i] != 0:
         min_ = lst2[i]   


result = round(max_ - min_, 2)
print(f'The difference between max fraction and min fraction is {result}')