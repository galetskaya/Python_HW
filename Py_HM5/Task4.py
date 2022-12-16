'''
Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
'''

# реалиован только для букв в строке

with open('file.txt', 'w') as data:
    data.write('aaaazzeeertyyyyyyy')

with open('file.txt', 'r') as data:
    string = data.readline()

def compress(txt):
    count = 1
    res = ''
    for i in range(len(txt)-1):
        if txt[i] == txt[i+1]:
            count += 1
        else:
            res = res + str(count) + txt[i]
            count = 1
    if count > 1 or (txt[len(txt)-2] != txt[-1]):
        res = res + str(count) + txt[-1]
    return res

def decompress(txt):
    number = ''
    res = ''
    for i in range(len(txt)):
        if not txt[i].isalpha():
            number += txt[i]
        else:
            res = res + txt[i] * int(number)
            number = ''
    return res


with open('file.txt', 'r') as file:
    start_string = file.read()

with open('file_encode.txt', 'w') as file:
    encoded_string = compress(start_string)
    file.write(encoded_string)

with open('file_encode.txt', 'r') as file:
    start_string = file.read()

with open('file_decode.txt', 'w') as file:
    start_string = decompress(encoded_string)
    file.write(start_string)

print('Compression: ', compress(string))
print('Decompression: ', decompress(compress(string)))