import random
from random import randrange
from datetime import datetime
from faker import Faker
from faker.providers import date_time
import uuid
from json_generator import write_survey, write_answer
import json
import os
import csv
from random_data import T1,T2
class ConductedSurveyDTO:
    def __init__(
        self,
        id,
        fk_employee=None,
        fk_client=None,
        fk_survey=None,
        id_answers=None,
        datetime=None,
        email_or_phone=None,
        is_completed=None,
    ):
        self.id = id
        self.fk_employee = fk_employee
        self.fk_client = fk_client
        self.fk_survey = fk_survey
        self.id_answers = id_answers
        self.datetime = datetime
        self.email_or_phone = email_or_phone
        self.is_completed = is_completed



class ConductedSurveyFactory:
    @staticmethod 
    def get_existing_survey():
        surveys = os.listdir('./surveys')
        survey = random.choice(surveys)
        survey_json = json.load(open('./surveys/' + survey))
        number_of_answers = survey_json['number_of_questions']
        return survey, number_of_answers
    @staticmethod
    def generate_conducted_survey(employees_ids, clients_ids, completion_percentage=60):
        faker = Faker()
        id = uuid.uuid4()
        
        fk_client = random.choice(clients_ids)
        survey, number_of_answers = ConductedSurveyFactory.get_existing_survey()
        fk_survey = survey
        while True:
            try:
                with open("./employee_file.csv", mode="r") as employee_file: 
                    csv_reader = csv.reader(employee_file, delimiter=",", quotechar='"')
                    chosen_row = random.choice(list(csv_reader)[1:])

            except Exception as e:
                print(e, 'no employee_file.csv') 
                exit()
            fk_employee = chosen_row[0]
            employment_date = chosen_row[6]
            dismissal_date = chosen_row[7]
            try:        
                start_date = max(datetime.strptime(employment_date, "%Y-%m-%d"), T1)
                if dismissal_date != "":
                    end_date = min(datetime.strptime(dismissal_date, "%Y-%m-%d"), T2)
                else:
                    end_date = T2
                if end_date > start_date:
                    date_time = str(faker.date_between(start_date, end_date).strftime("%m/%d/%Y"))
                    break
            except Exception:
                pass
                # else: 
                #     continue
            # except Exception as e:
            #     print(e)
            #     print(start_date, end_date)            
            #     exit()
        email_or_phone = randrange(0,2)
        if completion_percentage > randrange(0,100):
            is_completed = True
            id_answers = uuid.uuid4()
            write_answer(str(id_answers),save_path='./answers/',number_of_questions=number_of_answers)
        else: 
            is_completed = False
            id_answers = None
        return ConductedSurveyDTO(
            id=id,
            fk_employee=fk_employee,
            fk_client=fk_client,
            fk_survey=fk_survey,
            id_answers=id_answers,
            datetime=date_time,
            email_or_phone=email_or_phone,
            is_completed=is_completed,
        )

class SurveyDTO:
    def __init__(
        self,
        id,
        survey_content=None,
        title=None,
        company_name=None,
        survey_html=None,
    ):
        self.id = id
        self.survey_content = survey_content
        self.title = title
        self.company_name = company_name
        self.survey_html = survey_html


class SurveyFactory:
    @staticmethod
    def generate_survey():
        faker = Faker()
        id = uuid.uuid4()
        survey_content = uuid.uuid4()
        title = faker.bs()
        company_name = faker.company()
        survey_html = None
        file_name = id
        write_survey(filename=str(survey_content))


        return SurveyDTO(
            id,
            survey_content=survey_content,
            title=title,
            company_name=company_name,
            survey_html=survey_html
        )

