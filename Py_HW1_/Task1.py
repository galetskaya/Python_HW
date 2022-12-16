# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, 
# является ли этот день выходным.
# Пример:
# - 6 -> да
# - 7 -> да
# - 1 -> нет

print('Enter the number from 1 to 7, corresponding to a week day')
user_number = int(input())

def Weekend_Day(user_number):
    if user_number == 6 or user_number == 7:
        print('Yes, it is weekend! Grab a beer!')
    elif user_number >= 1 and user_number <= 5:
        print('Nope, it is a workday :(')
    else:
        print('Your number is out of 1-7 range')
    
Weekend_Day(user_number)

