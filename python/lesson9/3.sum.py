import sys

'''
Задача 3. Файл-тест. Есть файл, в котором хранятся числа в следующем формате:

2 4 5;3 2
3 2 1;2 0
6 5 2 1 2;3 1
.....

Цифры до точки с запятой надо суммировать,
потом делить на их количество. В первой строке сумма будет 11,
разделить на их количество, т.е. на 3, получается 3 целых и в остатке 2.
Аналогичным образом во второй строке 6 делим на три, ровно два и в сотатке ноль, в третьей строке сумма 16, на 5 делим,
получаем 3 и 1 в остатке. Вот так:

2 4 5;3 2                 2+4+5/3 = 3, в остатке 1
3 2 1;2 0                 3+2+1/3 = 2, в остатке 0
6 5 2 1 2;3 1         6+5+2+1+2/5 = 3, в остатке 1

Задача: проверить каждую строку файла, если строка записана верно, вывести ее и после написать True,
если строка не верна, вывести результат с пометкой False.
'''

try:
    input_file = open(sys.argv[1], 'r')
except (IndexError, FileNotFoundError):
    print('Valid file should be given as an argument, try again.')
    exit()

for i in input_file:
    left_list = i.split(';')[0].split()
    right_list = i.split(';')[1].split()
    left_list_int = list(map(int, left_list))
    right_list_int = list(map(int, right_list))
    list_sum = [sum(left_list_int) // len(left_list_int), sum(left_list_int) % len(left_list_int)]
    if list_sum == right_list_int:
        print(f'{i}\nTrue\n')
    else:
        print(f'{list_sum}; {right_list_int}\nFalse\n')
