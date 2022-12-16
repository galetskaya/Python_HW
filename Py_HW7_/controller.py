import model_read as mr
import model_add as ma
import model_delete as md
import model_search as ms
import model_import as mi
import model_export as me

data = 'phone_book.txt'

def button_click():

        task = 0
        while task < 8:
            try:
                task = int(input("Выбери что нужно сделать: \n"
                "1 - Чтение \n"
                "2 - Запись \n"
                "3 - Импорт \n"
                "4 - Экспорт \n"
                "5 - Удаление \n"
                "6 - Поиск \n"
                "7 - Выход \n"
                "Введи нужную цифру \n"))
                if task == 1:
                    mr.read(data)
                elif task == 2:
                    ma.add_new_data(data)
                elif task == 3:
                    mi.file_imp(data)
                elif task == 4:
                    me.file_exp(data)
                elif task == 5:
                    md.delete_data(data)
                elif task == 6:
                    ms.search_data(data)
                elif task == 7:
                    break


            except:
                print("НЕ то ввели, попробуйте еще раз")
        else:
            print("Вы вышли из программы, запустите еще раз")