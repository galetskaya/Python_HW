'''Задание 3 Задайте список из n чисел последовательности (1+1/n)^n и выведите на экран их 
сумму, округлённую до трёх знаков после точки.
Пример:
Для n = 6 -> 14.072
'''

print('Enter the length of the list: ')
user_length = int(input())

# old code
# def subsequence_sum(user_length):
#     sum = 0
#     for i in range(user_length):
#         print(f'Enter the number {i+1}')
#         number = int(input())
#         number = (1+1/number)**number
#         sum = sum + number
#         i = i + 1
#     print(f'The result is {round(sum, 2)}')    


# subsequence_sum(user_length)

#new code
new_list = [(round(((1 + 1 / i)**i), 3)) for i in range(1, user_length + 1)]
print(sum(new_list))