#добавление записи в файл


def add_new_data(data):
    print('Если вы хотите добавить запись в строку - выберите 1, если в столбик - 2')
    user_choice = int(input())
    if user_choice == 2:
        with open(data, 'a', encoding='utf-8') as f:
            temp1 = (input('Введите фамилию \n'))
            temp2 = (input('Введите Имя \n'))
            temp3 = (input('Введите номер телефона \n'))
            temp4 = (input('Введите комментарий \n') )
            lst1 = [temp1, temp2, temp3, temp4]
            lst2 = []
            for each in lst1:
                if each != '\n':
                    lst2.append(each.replace("\n", ""))

            str1 = ', '.join(map(str, lst2))
            f.writelines(str1)
            f.writelines('\n')

    elif user_choice == 1:
        with open(data, 'a', encoding='utf-8') as f:
            value = ('\n' + input('Введите данные через запятую \n'))
            if value.__contains__(', '):
                f.writelines(value)
                f.writelines('\n')
            else:
                x = value.replace(',', ', ')
                f.writelines(x)
                f.writelines('\n')

    else:
        print("Некорректный выбор")