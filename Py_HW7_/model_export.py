def file_exp(data):
    print('Если вы хотите добавить запись в строку - выберите 1, если в столбик - 2')
    user_choice = int(input())
    if user_choice == 2:
        with open(data, encoding='utf-8') as f:
            lines = f.readlines()

        with open('phone_book_exp.txt', "w", encoding='utf-8') as g:
            for each in lines:
                if each.__contains__(','):
                    str = each.split(', ')
                    g.writelines('\n'.join(str))
                    g.writelines('\n')
    elif user_choice == 1:
        with open(data, "r", encoding='utf-8') as f:
            with open('phone_book_exp.txt', "w", encoding='utf-8') as g:
                for line in f:
                    g.write(line)
    else:
        print("Некорректный выбор")



