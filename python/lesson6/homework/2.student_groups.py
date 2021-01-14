'''
Создать структуру данных для студентов из имен и фамилий, можно случайных.
Придумать структуру данных, чтобы указывать, в какой группе учится студент (Группы Python, FrontEnd, FullStack, Java).
Студент может учиться в нескольких группах. Затем вывести:
- студентов, которые учатся в двух и более группах
- студентов, которые не учатся на фронтенде
- студентов, которые изучают Python или Java
'''

students = {
    'Michelle Choi': ['Python', 'FrontEnd', 'FullStack', 'Java'],
    'Joanna Montes': ['Python'],
    'Sara Harmon': ['FrontEnd'],
    'Kathryn Brown': ['FullStack'],
    'Jerry Atkinson': ['Java'],
    'Jeffrey Wilson': ['Java'],
    'Benjamin Saunders': ['Python'],
    'Amanda Gonzalez': ['FullStack'],
    'Andrew Robinson': ['Python', 'FrontEnd'],
    'Claudia Figueroa': ['Java', 'FrontEnd']
}


# Студенты, которые учатся в двух и более группах
def two_or_more_groups(students):
    return [student for student in students if len(students[student]) > 1]


# Студенты, которые не учатся на фронтенде
def not_included(students, the_class):
    return [student for student in students if the_class not in students[student]]


# Студенты, которые изучают Python или Java
def find_classes(students, the_classes):
    # Return results list with removed duplicates
    return list(dict.fromkeys([student for student in students if lambda i: i for i in the_classes if i in students[student]]))


print('Student that are in 2 or more groups: ', two_or_more_groups(students))
print('Student that areen\'t taking the \'FrontEnd\' class', not_included(students, 'FrontEnd'))
print('Students that are in \'Python\' or \'Java\': ', find_classes(students, ['Java', 'Python']))
