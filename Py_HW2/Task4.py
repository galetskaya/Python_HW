'''Задание 4 Задайте список из N элементов, заполненных числами из промежутка [-N, N].
Найдите произведение элементов на позициях a и b.
Значения N, a и b вводит пользователь с клавиатуры.
'''

print('Enter the value: ')
user_number = int(input())
list_length = int((user_number*2)+1)


list = []
new_number = -user_number
for i in range(list_length):
    number = new_number
    new_number = new_number + 1
    list.append(number)
print('The list is: ')    
print(list)    


a = int(input(f'Enter value "a" in range from 0 to {list_length - 1}: '))
b = int(input(f'Enter value "b" in range from 0 to {list_length - 1}: '))

if a>=0 and a<list_length and b>=0 and b<list_length:
    result = list[a]*list[b]
    print(f'The result is: {result}')
else:
    print('Value a or b is out of range.')  
      
