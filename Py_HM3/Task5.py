'''Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

Пример:

- для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] 
Негафибоначчи
'''

print('Enter the number')
user_value = int(input())


def negafibonacci(num):
    fibonacci_lst = []
    a = 1
    b = 1
    for i in range(num - 1):
        fibonacci_lst.append(a)
        temp = a
        a = b
        b = temp + b

    a = 0
    b = 1

    for i in range(num):
        fibonacci_lst.insert(0, a)
        temp = a
        a = b
        b = temp - b
    print(fibonacci_lst)  

negafibonacci(user_value)