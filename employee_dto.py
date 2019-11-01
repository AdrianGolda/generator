from random_data import education
import random
from random import randrange
from datetime import datetime
from faker import Faker
from faker.providers import date_time
import uuid


class EmployeeDTO:
    def __init__(
        self,
        id,
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
    def generate_employee():
        faker = Faker()
        id = uuid.uuid4()
        random_gender = randrange(0, 2)
        if random_gender:
            gender = 1
            first_name = faker.first_name_male()
        else:
            gender = 0
            first_name = faker.first_name_female()
        last_name = faker.last_name()
        dob = faker.date_of_birth(minimum_age=18, maximum_age=50)
        employment_date = faker.date_between(start_date=dob, end_date="today")
        dismissal_date = faker.date_between(
            start_date=employment_date, end_date="today"
        )
        return EmployeeDTO(
            id=id,
            first_name=first_name,
            last_name=last_name,
            gender=gender,
            dob=dob,
            employment_date=employment_date,
            dismissal_date=dismissal_date,
            education=random.choice(education),
            salary=randrange(2000, 5000, 100),
        )
