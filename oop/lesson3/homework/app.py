from .people.models import Recruiter, Programmer, Candidate

def main():

    recruiter_1 = Recruiter(
        name='Jane Doe',
        email='jane@company.com',
        daily_salary=223
    )

    coder_1 = Programmer(
        name='Will Smith',
        email='w.s@company.com',
        daily_salary=308
    )
    coder_2 = Programmer(
        name='Mel Gibson',
        email='gibbs@company.com',
        daily_salary=303
    )

    candidate_1 = Candidate(
        full_name='Margot Robbie',
        email='maggie@company.com',
        technologies=['HTML', 'CSS', 'ReactJS'],
        main_skill='ReactJS',
        main_skill_grade=4
    )
    candidate_2 = Candidate(
        full_name='Leonardo DiCaprio',
        email='oscar@company.com',
        technologies=['Python', 'Django', 'Docker'],
        main_skill='Python',
        main_skill_grade=5
    )
    candidate_3 = Candidate(
        full_name='Daniel Defoe',
        email='oscar@company.com',
        technologies=['Python', 'Flask', 'Angular', 'JS'],
        main_skill='JS',
        main_skill_grade=4
    )
