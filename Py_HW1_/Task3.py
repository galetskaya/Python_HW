# Напишите программу, которая принимает на вход координаты точки (X и Y), 
# причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка 
# (или на какой оси она находится).
# Пример:
# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

print('Enter the point coordinates: ')
print('enter x')
x = int(input())
print('enter y')
y = int(input())

def Quarter (x,y):
    if x > 0 and y > 0:
        print('Point is in quarter I')
    elif x < 0 and y > 0:
        print('Point is in quarter II')
    elif x < 0 and y < 0:
        print('Point is in quarter III')
    elif x == 0 and y == 0:
        print('Point is not in quarter')      
    else:
        print('Point is in quarter IV')      
        
Quarter(x,y)        