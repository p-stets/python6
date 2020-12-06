'''
Создать словарь оценок предполагаемых студентов
(Ключ - ФИ студента, значение - список оценок студентов).
Найти самого успешного и самого отстающего по среднему баллу.
'''

students = {
    'Doe John': {
        'Math': [2, 7, 6, 8],
        'Biology': [2, 7, 6, 8, 1],
        'History': [2, 7, 6, 8]
    },
    'Smith Will': {
        'Math': [1, 1, 2, 7, 6, 8],
        'Biology': [2, 7, 6, 8],
        'History': [2, 7, 6, 8]
    },
    'Brown Alex': {
        'Math': [2, 7, 6, 8],
        'Biology': [2, 4, 6, 8],
        'History': [2, 7, 6, 8]
    }
}


# Calculating weighted average for every student and sorting ASC by student name
def find_average(students_dict):
    results = {}
    for key in students_dict:
        total = 0
        for science in students_dict[key]:
            total += (sum(students_dict[key][science]) / len(students_dict[key][science]))
            # print(len(students_dict[key][pre]))
        results[key] = round(total, 2)
    # Sorting the results ASC
    results_sorted = {key: results[key] for key in sorted(results.keys())}
    return results_sorted


# Finding the most successful student
def the_one(dict_with_grades, best=True):
    for k in sorted(dict_with_grades, key=dict_with_grades.get, reverse=not best):
        result = {k: dict_with_grades[k]}
    return result


print(f'The most successfull is: {the_one(find_average(students))}')
print(f'The less successull is: {the_one(find_average(students), False)}')
