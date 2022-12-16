#To make a choice in the dictionary
import model_admin

def choice():
    role = model_admin.find_login()
    if role == 1 or role == 2:
        choice = int(input('Choose your option: \n'
                    '1 - read all records \n'
                    '2 - read 1 student record \n'
                    '3 - update student record \n'
                    '\n'))
        return(choice)
    else:
        choice = int(input('Choose your option: \n'
                    '2 - read 1 student record \n'
                    '\n'))
        return(choice)