import sys
from pprint import pprint as print

'''
Задание 3
Вспоминаем работу с файлом.
Есть файл, в котором много англоязычных текстовых строк.
Считаем частоту встретившихся слов в файле, но через функции и map, без единого цикла!
'''

REDUNDANT_CHARS = '~01234567890!@#$%^&*()-=,./\\`|<>'

try:
    input_file = open(sys.argv[1], 'r')
    text = input_file.read()
except (IndexError, FileNotFoundError, UnicodeDecodeError):
    print('Valid input and file required, try again.')
    exit()


# Removing numbers and other redundant characters from the text
def prepare_text(text, excuded_characters=REDUNDANT_CHARS):

    for i in excuded_characters:
        if i in text:
            text = text.replace(i, '')
    # return list of words
    return sorted(text.lower().strip().split())

# Calculating words count
def count_words(text, prepare_text=prepare_text):

    words_list = prepare_text(text)
    words_dict = {key: words_list.count(key) for key in words_list}
    return words_dict


# Pretty printing the result
print(count_words(text), width=1)
input_file.close()
