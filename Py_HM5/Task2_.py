'''Создайте программу для игры с конфетами человек против человека.
Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. 
Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. 
Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому
игроку, чтобы забрать все конфеты у своего конкурента?
a) Добавьте игру против бота
b) Подумайте как наделить бота ""интеллектом""
'''


from random import randint

def robot_choice(total_num):
    pick = total_num % 29
    return pick


def human_data(name):
    num_sweets = int(input(f"{name}, eneter the amount of candies from 1 to 28: "))
    while num_sweets < 1 or num_sweets > 28:
        num_sweets = int(input(f"{name}, the amount is wrong. Enter the correct amount, please: "))
    return num_sweets


def result_print(name, candy, tot_amount):
    print(f"{name} took {candy}. Left {tot_amount} in stock.")


player1 = 'Human'
player2 = 'Terminator'

tot_amount = int(input("How many candies we play with: "))

flag = randint(0,2)                 #choose who goes first
if flag:
    print(f"The first is {player1}")
else:
    print(f"The first is {player2}")

counter1 = 0 
counter2 = 0

while tot_amount > 28:
    if flag:
        candy = human_data(player1)
        counter1 += candy
        tot_amount -= candy
        flag = False
        result_print(player1, candy, tot_amount)
    else:
        candy = robot_choice(tot_amount)
        counter2 += candy
        tot_amount -= candy
        flag = True
        result_print(player2, candy, tot_amount)

if flag:
    print(f"The winner is {player1}")
else:
    print(f"The winner is {player2}")