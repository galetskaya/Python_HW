'1. Создайте программу для игры в ""Крестики-нолики"" при помощи виртуального окружения и PIP'

import emoji



board = list(range(1, 10))

winner_combinations = [(1, 2, 3), (4, 5, 6), (7, 8, 9), (1, 4, 7), (2, 5, 8), (3 ,6 ,9), (1, 5, 9), (3, 5, 7)]


def draw_board():
    print('------------------')
    for i in range(3):
        print('| ', board[0 + i * 3], ' | ', board[1 + i * 3], ' | ', board[2 + i * 3], ' |')
    print('------------------')


def take_input(player_token):
    while True:
        value = input(f'Where would you put {player_token} ? ')
        if not (value in '123456789'):
            print('Input is out of range. Please, repeat.')
            continue
        value = int(value)
        # if str(board[value - 1]) in 'xo':
        if str(board[value - 1]) not in '123456789':
            print('This cell is already taken')
            continue
        board[value - 1] = player_token
        break


def check_winners():
    for each in winner_combinations:
        if (board[each[0] - 1]) == (board[each[1] - 1]) == (board[each[2] - 1]):
            return board[each[1] - 1]
    else:
        return False
        
        
def main():
    counter = 0
    while True:
        draw_board()
        if counter % 2 == 0:
            take_input(emoji.emojize(':goat:'))
        else:
            take_input(emoji.emojize(':egg:'))
        if counter > 3:
            winner = check_winners()
            if winner:
                draw_board()
                print(winner, 'won!', emoji.emojize(':1st_place_medal:'))
                break   
        counter += 1
        if counter > 8:
            draw_board()
            print('Standoff', emoji.emojize(':grimacing_face:'))  
            break                


main()