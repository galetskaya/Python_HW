#To change the mark
# import model_convert


def change_mark(dict, data):
    key = input('Name: ')
    new_mark = int(input('New mark: '))
        
    if key in dict:
        dict[key] = new_mark
    else:
        print('No student found')  

    with open(data, 'w', encoding='utf-8') as f2:
        for key,val in dict.items():
            f2.write('{}\n{}\n'.format(key,val))