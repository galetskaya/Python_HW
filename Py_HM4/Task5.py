'''5 Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать 
файл, содержащий сумму многочленов. 
Коэффициенты могут быть как положительными, так и отрицательными. 
Степени многочленов могут отличаться.
'''
 
polinom_1 = '5*x^2 + 3*x^6 - 15*x**3 + 66'
polinom_2 = '13*x^3 + 3*x^4 - 15*x^8 - 99'
 
polinom_1 = polinom_1.replace(' ', '').replace('**', '^').replace('*', '')
polinom_2 = polinom_2.replace(' ', '').replace('**', '^').replace('*', '')
 
 
def get_dict_from_polinom(str_pol):
    lst = []
    last_index = -1
    neg = False
    for i, char in enumerate(str_pol):
        if char == '+' or char == '-':
            if neg:
                lst.append('-' + str_pol[last_index + 1:i])
            else:
                lst.append(str_pol[last_index + 1:i])
            last_index = i
            neg = char == '-'
    if neg:
        lst.append('-' + str_pol[last_index + 1:])
    else:
        lst.append(str_pol[last_index + 1:])
 
    print(lst)
    dct = {}
    for item in lst:
        for i, char in enumerate(item):
            if not char.isdigit() and char != '.' and char != '-':
                dct[item[i:]] = float(item[:i])
                break
        else:
            dct[''] = float(item)
 
    return dct
 
 
dct1 = get_dict_from_polinom(polinom_1)
dct2 = get_dict_from_polinom(polinom_2)
 
set1 = set(dct1.keys())
set2 = set(dct2.keys())
 
itog_dct = {}
 
for key in set1.intersection(set2):
    itog_dct[key] = dct1[key] + dct2[key]
 
for key in set1.symmetric_difference(set2):
    if key in dct1:
        itog_dct[key] = dct1[key]
    else:
        itog_dct[key] = dct2[key]
 
 
print(itog_dct)
 
print([f'{itog_dct[key]}{key}' for key in sorted(itog_dct.keys(), reverse=True)])
 
