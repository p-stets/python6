'''
Третий уровень ("Мистер Буль. Джордж Буль!"):
Решить задачу:

Задача fizz-buzz:
`
У вас есть три числа, они вводятся из консоли. Первое число называется fizz, второе называется buzz.
До третьего необходимо досчитать от единицы. Считая, надо выводить число.
Если число кратно fizz - надо выводить F вместо числа.
Если число кратно buzz - надо выводить B вместо числа.
Если число кратно и fizz и buzz, надо выводить FB. И так - пока не будет достигнуто третье введенное число.

Пример условия и результата:
Введены числа 2, 5, 18
Вывод должен быть таким:
1 F 3 F B F 7 F 9 FB 11 F 13 F B F 17 F
'''
fizz = int(input('\nInput \'fizz\': '))
buzz = int(input('Input \'buzz\': '))
third = int(input('And now the third one: '))

output = ''

for i in range(1, third + 1):
    result = ''
    if not i % fizz:
        result += 'F'
    if not i % buzz:
        result += 'B'
    if not result:
        result = i
    output += f'{result} '

print(f'\n The result is:\n {output}\n')
