#To read just 1 specific record from the dict
def read_one(dic):
    student = input('Enter full student name you are looking for: \n')
    if student in dic:
        print(f'{student}, mark {dic[student]}')
    else:
        print('No such student')  