from random_data import education
import random
from random import randrange
from datetime import datetime
from faker import Faker
from faker.providers import date_time
import uuid


class ClientDTO:
    def __init__(
        self,
        id,
        first_name=None,
        last_name=None,
        dob=None,
        gender=None,
        profession=None,
        has_kids=None,
        education=None,
        email=None,
        phone = None,
        last_called= None,
        is_married=None
    ):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.dob = dob
        self.gender = gender
        self.profession = profession
        self.has_kids = has_kids
        self.education = education
        self.email = email
        self.phone = phone
        self.last_called = last_called
        self.is_married = is_married


class ClientFactory:
    @staticmethod
    def generate_client():
        faker = Faker()
        id = uuid.uuid4()
        random_gender = randrange(0, 2)
        if random_gender:
            gender = 1
            first_name = faker.first_name_male()
            # first_name = random.choice(male_first_names)
        else:
            gender = 0
            # first_name = random.choice(female_first_names)
            first_name = faker.first_name_female()
        last_name = faker.last_name()
        dob = faker.date_of_birth(minimum_age=18, maximum_age=50)
        profession = faker.job()
        email = faker.email()
        phone = faker.phone_number()
        last_called = faker.date_this_year(before_today=True, after_today=False)
        is_married = randrange(0, 2)
        has_kids = randrange(0, 2)
            
        return ClientDTO(
            id=id,
            first_name=first_name,
            last_name=last_name,
            gender=gender,
            dob=dob,
            profession=profession,
            has_kids=has_kids,
            education=random.choice(education),
            email=email,
            phone=phone,
            last_called=last_called,
            is_married=is_married
        )
