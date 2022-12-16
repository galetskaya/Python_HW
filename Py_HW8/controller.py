
import model_convert
import model_choice
import model_changemark 
import model_readall
import model_readone


def programm():
    lesson = 0

    while lesson < 4:       
        lesson = int(input('Enter the lesson you are looking for: \n'
                    '1 - algebra \n'
                    '2 - literature \n'
                    '3 - chemistry \n'
                    '\n'
                    ))   
        if lesson == 1:
            #конвертируем файл text в словарь
            data = 'algebra.txt'
            algebra = model_convert.convert_to_dict(data)


            chosen = model_choice.choice()
            
            if chosen == 1:
                model_readall.read_all(algebra)
            elif chosen == 2:    
                model_readone.read_one(algebra)
            elif chosen == 3:
                model_changemark.change_mark(algebra, data)
            else:
                print('oopsie, your choice is incorrect')       
        
                


        elif lesson == 2:
            #конвертируем файл text в словарь
            data = 'literature.txt'
            literature = model_convert.convert_to_dict(data)


            chosen = model_choice.choice()
            
            if chosen == 1:
                model_readall.read_all(literature)
            elif chosen == 2:    
                model_readone.read_one(literature)
            elif chosen == 3:
                model_changemark.change_mark(chemistry, data)
            else:
                print('oopsie, your choice is incorrect')        
            
            
        elif lesson == 3:
            #конвертируем файл text в словарь
            data = 'chemistry.txt'
            chemistry = model_convert.convert_to_dict(data)


            chosen = model_choice.choice()
            
            if chosen == 1:
                model_readall.read_all(chemistry)
            elif chosen == 2:    
                model_readone.read_one(chemistry)
            elif chosen == 3:
                model_changemark.change_mark(chemistry, data)
            else:
                print('oopsie, your choice is incorrect')      


