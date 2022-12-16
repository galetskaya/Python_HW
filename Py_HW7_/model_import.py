
import os

def file_imp(data):
    print('Поместите файл из которого нужно импортировать данные в папку')
    file_name = input('Введите название файла, который нужно импортировать \n')
    if os.path.isfile(file_name):
        with open(file_name, "r", encoding='utf-8') as f, open(data, "a", encoding='utf-8') as g:
            g.writelines('\n')
            for line in f:
                if len(line) > 20:
                    g.writelines(line)
                    g.writelines('\n')
            if len(line) < 20:
                with open(file_name, encoding='utf-8') as k:
                    lines = k.readlines()
                with open(data, "a", encoding='utf-8') as l:
                    j = 0
                    lst1 = []
                    for each in lines:
                        if not each.__contains__(','):
                            if each != '\n':
                                lst1.append(each.replace("\n", ""))
                                j += 1
                                if j == 4:
                                    l.writelines(', '.join(lst1))
                                    l.writelines('\n')
                                    j = 0
                                    lst1 = []

    else:
        print('Объект не найден')