'''Напишите программу, которая найдёт произведение пар чисел списка. 
Парой считаем первый и последний элемент, второй и предпоследний и т.д.

Пример:

- [2, 3, 4, 5, 6] => [12, 15, 16];
- [2, 3, 5, 6] => [12, 15]
'''

import random

print('Enter the size of the list: ')
list_length = int(input())


def new_list_creation(lst_length):
    lst = []
    for i in range(lst_length):            
        new_number = random.randint(0,15)
        lst.append(new_number) 
    return lst

list = new_list_creation(list_length)
print('The list is: ')
print(list)


def multip_two_oppose_numbers(list, list_length):
    if list_length % 2 == 0:
        for i in range(list_length//2):
            result = list[i] * list[list_length - 1 - i]
            print(f'The result is: {result}')
    else: 
        for i in range((list_length + 1)//2):
            result = list[i] * list[list_length - 1 - i]
            print(f'The result is: {result}')   


multip_two_oppose_numbers(list, list_length)