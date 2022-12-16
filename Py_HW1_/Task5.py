# Напишите программу, которая принимает на вход координаты двух точек и находит 
# расстояние между ними в 2D пространстве.
# Пример:
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

print("Enter the points' coordinates")
print('Enter x/y coordinates for point A')
x1 = int(input())
y1= int(input())
print('Enter x/y coordinates for point B')
x2 = int(input())
y2 = int(input())

def Find_Dis(arg1, arg2):          
    dis = (arg1 - arg2) ** 2
    return dis

def Math_Square(arg1, arg2):
    square = round((arg1 + arg2) ** 0.5, 2)
    return square
    
x_distance = Find_Dis(x1,x2)
y_distance = Find_Dis(y1,y2)

distance = Math_Square(x_distance, y_distance)
print(f'The distance is {distance}')
