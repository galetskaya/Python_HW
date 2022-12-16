# Задание 2 Напишите программу, которая принимает на вход число N и выдает набор произведений 
# чисел от 1 до N.
# Пример:
# пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)


print('Enter you value: ')
user_number = int(input())

def factorial(num):
    result = 1
    if num == 1 or num == 0:
        print(1)
    else:
        for i in range(1, num + 1):
            result = result*i
            print(result, end = ',')


print('The result is: ')        
factorial(user_number)

   
