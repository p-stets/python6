'''
1.Создать класс  Employee. Хранить в нём данные о работнике
(
Имя,
почту,
ЗП за один рабочий день
). 
2.Создать метод work(...) который возвращает строку “I come to the office.”
3.Создать метод check_salary(...) - который позволит посчитать ЗП за указанное количество рабочих дней.
4.Создать классы Recruiter и Programmer, которые наследуются от Employee
5.Переопределить методы work() которые будут использовать метод родителя и возвращать:
    ◦“I come to the office and start to coding.” - для Programmer
    ◦“I come to the office and start to hiring.” - для Recruiter
6.Переопределить методы __str__ для классов-наследников, чтоб они возвращали строку: “Должность: Имя”
'''


class Employee(object):

    def __init__(self, name, email, daily_salary):
        self.name = name
        self.email = email
        self.daily_salary = daily_salary

    def work(self):
        return 'I come to the office'

    def check_salary(self, days_count):
        return days_count * self.daily_salary


class Recruiter(Employee):

    def __str__(self):
        return f'{self.__class__.__name__}: {self.name}'

    def work(self):
        return f'{super().work()} and start hiring'


class Programmer(Employee):

    def __str__(self):
        return f'{self.__class__.__name__}: {self.name}'

    def work(self):
        return f'{super().work()} and start coding'


# Creating a Recruiter instance
emp_1 = Recruiter('Jane', 'jane@compamy.com', 223)

# Printing class name
print(emp_1)

# Work execution
print(emp_1.work())

# Week (5 working days) salary calculation
print(emp_1.check_salary(5))
