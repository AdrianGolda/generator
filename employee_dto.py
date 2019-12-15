from random_data import education
import random
from random import randrange
from datetime import datetime
from faker import Faker
from faker.providers import date_time
from random_data import T1, T2
import uuid


class EmployeeDTO:
    def __init__(
        self,
        id,
        pesel=None,
        first_name=None,
        last_name=None,
        dob=None,
        gender=None,
        employment_date=None,
        dismissal_date=None,
        education=None,
        salary=None,
    ):
        self.id = id
        self.pesel=pesel
        self.first_name = first_name
        self.last_name = last_name
        self.dob = dob
        self.gender = gender
        self.employment_date = employment_date
        self.dismissal_date = dismissal_date
        self.education = education
        self.salary = salary


class EmployeeFactory:
    @staticmethod
    def generate_employee(gender_percent, dismissal_rate, min_salary, max_salary):
        faker = Faker()
        id = uuid.uuid4()
        pesel = str(randrange(30000000000, 99999999999))
        random_gender = randrange(0, 100)
        if random_gender <= gender_percent:
            gender = 1
            first_name = faker.first_name_male()
        else:
            gender = 0
            first_name = faker.first_name_female()
        last_name = faker.last_name()
        dob = faker.date_of_birth(minimum_age=18, maximum_age=50)
        employment_date = faker.date_between(start_date=T1, end_date=T2)
        random_dismissal = randrange(0,100)
        if random_dismissal <= int(dismissal_rate):
            dismissal_date = faker.date_between(
                start_date=T1, end_date=T2
            )
        else:
            dismissal_date = None
        return EmployeeDTO(
            id=id,
            pesel=pesel,
            first_name=first_name,
            last_name=last_name,
            gender=gender,
            dob=dob,
            employment_date=employment_date,
            dismissal_date=dismissal_date,
            education=random.choice(education),
            salary=randrange(min_salary, max_salary, 100),
        )
