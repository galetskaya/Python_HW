'''5. Дан список чисел. Создайте список, в который попадают числа, 
описываемые возрастающую последовательность. Порядок элементов менять нельзя.
[1, 5, 2, 3, 4, 6, 1, 7] => [1, 2, 3] или [1, 7] или [1, 6, 7] и т.д.
Входные и выходные данные хранятся в отдельных текстовых файлах.

Решение Акопяна'''

itog = set()


def f(lst, cur=None, i=0):
    
    cur = [] if cur is None else cur
    if i == len(lst):
        if len(cur) > 1:
            itog.add(tuple(cur))
        return 
    f(lst, cur, i + 1)
    for index in range(i, len(lst)):
        if cur and cur[-1] < lst[index]:
            f(lst, cur + [lst[index]], index + 1)
        elif not cur:
            f(lst, [lst[index]], index + 1)
            

f([1, 5, 2, 3, 4, 6, 1, 7])
print(*sorted(itog), sep='\n')

                    