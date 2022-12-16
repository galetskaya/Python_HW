#Удалние записи из файла, работает только для строки


def delete_data(data):
    print('Введите данные для удаления: ')
    value_to_delete = input()


    with open(data, encoding='utf-8') as f:
        lines = f.readlines()
        
    with open(data, "w", encoding='utf-8') as f:
        for line in lines:
                if value_to_delete not in line:
                    f.write(line) 
    return(data)