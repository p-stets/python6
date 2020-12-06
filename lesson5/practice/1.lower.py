'''
Задание 1
Написать 2 функции. Первая функция будет принимать строку и приводить ее к нижнему регистру.

Вторая функция будет принимать строку и проводить ее к верхнему регистру.

После чего с помощью map применить ваши функции к списку строк. Отдельно каждую функцию к отдельному списку строк!
'''


# Приведение к нижнему регистру
def to_lower(str):
    return str.lower()


# Приведение к верхнему регистру
def to_upper(str):
    return str.upper()


# Приведение списка к верхнему и нижнему
def apply_to_one(list_of_strings, to_lower=to_lower, to_upper=to_upper):
    lower_results = list(map(to_lower, list_of_strings))
    upper_results = list(map(to_upper, list_of_strings))
    return [lower_results, upper_results]


print(apply_to_one(['SsS', 'ZzZ']))
