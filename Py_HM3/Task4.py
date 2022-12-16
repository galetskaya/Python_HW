'''Напишите программу, которая будет преобразовывать десятичное число в двоичное.

Пример:

- 45 -> 101101
- 3 -> 11
- 2 -> 10
'''

print('Enter the value')
user_value = int(input())

binary_number = ''

while user_value > 0:
    binary_number = str(user_value % 2) + binary_number
    user_value = user_value//2

print(binary_number)