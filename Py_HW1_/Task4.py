# Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных 
# координат точек в этой четверти (x и y).

print('Enter the coordinate quarter: 1, 2, 3 or 4')
quarter = int(input())

def Coordinate_range (number):
    if number == 1:
        print('Coordinates are x > 0 and y > 0')
    elif number == 2:
        print('Coordinates are x < 0 and y > 0')  
    elif number == 3:
        print('Coordinates are x < 0 and y < 0')  
    elif number == 4:
        print('Coordinates are x > 0 and y < 0')  
    else:
        print('Your number is out of 1-4 range')        
        
Coordinate_range(quarter)        