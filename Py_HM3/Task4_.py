'''Напишите программу, которая будет преобразовывать десятичное число в двоичное.

Пример:

- 45 -> 101101
- 3 -> 11
- 2 -> 10
'''

print('Enter the value')
user_value = int(input())

binary_number = []

while user_value > 0:
    temp = user_value % 2
    user_value = user_value//2
    binary_number.append(temp)


binary_number.reverse()
a = "".join(map(str,binary_number))
print(a)