'''3 Задайте последовательность чисел. Напишите программу, которая выведет список 
неповторяющихся элементов исходной последовательности.
*Пример*
- при [1, 1, 2, 3, 3, 4, 1, 5, 7, 8, 8, 7, 9]     ->        [2, 4, 5, 9]
'''

import random

print('Enter the size of the list: ')
list_length = int(input())


def new_list_creation(list_length):
    lst = []
    for i in range(list_length):            
        new_number = random.randint(0,15)
        lst.append(new_number) 
    return lst


list = new_list_creation(list_length)
print(f'The list is: {list}')

#old code
# new_list = []

# for i in list:
#     count = 0
#     for j in list:
#         if i == j:
#             count += 1
#     if count == 1:
#         new_list.append(i)      
   
# print(f'Exclusive numbers in the list are {new_list}')           

#new code
new_list = [i for i in list if list.count(i) == 1]
print(new_list)