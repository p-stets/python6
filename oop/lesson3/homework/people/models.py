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


class Candidate(object):

    def __init__(self, full_name, email, technologies, main_skill, main_skill_grade):
        self.full_name = full_name
        self.email = email
        self.technologies = technologies
        self.main_skill = main_skill
        self.main_skill_grade = main_skill_grade


class Vacancy(object):

    def __init__(self, title, main_skill, main_skill_level):
        self.title = title
        self.main_skill = main_skill
        self.main_skill_level = main_skill_level
