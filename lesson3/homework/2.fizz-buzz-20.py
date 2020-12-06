import sys

'''
Написать fizzbuzz для 20 троек чисел, которые записаны в файл.
Читаете из файла первую строку, берете из нее числа, считаете для них fizzbuzz, выводите.
'''

try:
    input_file = open(sys.argv[1], 'r')
except (IndexError, FileNotFoundError):
    print('Valid file should be given as an argument, try again.')
    exit()


def fizz_buzz(list):
    if len(list) > 3:
        print(f'\n Wrong number of elements, expected: 3, current: {len(list)}')
        exit()

    output = ''
    for i in range(1, list[2] + 1):
        result = ''
        if not i % list[0]:
            result += 'F'
        if not i % list[1]:
            result += 'B'
        if not result:
            result = i
        output += f'{result} '

    print(f'\n Fizz: {list[0]}, Buzz: {list[1]}, Third: {list[2]}')
    print(f' The result is:\n {output}\n', end='')


for i in input_file:
    numbers = list(map(int, i.split()))
    fizz_buzz(numbers)

input_file.close()
