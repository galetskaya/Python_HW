# работает только для строчного типа, не работает для повторений


def search_data(data):
    print("Введите данные для поиска: ")
    search_value = input()

    with open(data,'r', encoding='utf-8') as file:
        for line in file:
            if search_value in line:
                print(line, end='')


