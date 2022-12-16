'''Задание 5 Реализуйте алгоритм перемешивания списка.
'''

import random


print('Enter the size of the list: ')
list_length = int(input())

list_new = []

def new_list_creation(lst, list_length):
    for i in range(list_length):            
        new_number = random.randint(0,30)
        lst.append(new_number) 

new_list_creation(list_new, list_length)
print(f'The list is: {list_new}')


def shuffle_list(list_length, list):
    for i in range(list_length):
        index = random.randint(0, list_length - 1)
        temp = list[i]
        list[i] = list[index]
        list[index] = temp 
    return list

shuffle_list(list_length, list_new)
print(f'The result of the shuffle is: {list_new}')