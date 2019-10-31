import argparse
import uuid
# import psycopg2
import csv
import os
from employee_dto import EmployeeFactory
from client_dto import ClientFactory
from survey_dto import ConductedSurveyFactory, SurveyFactory

NUMBER_OF_RECORDS : int = 10
CHANGE_PERCENT = 0
GENDER_PERCENT = 50
KIDS_PERCENT = 50
LAST_CALLED = 1
DISMISSAL_RATE = 20
COMPLETED_PERCENT = 60
PHONE_PRECENT = 80
MINIMUM_SALARY = 2000
MAXIMUM_SALARY = 5000

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Generate information for Employees, Clients, Survey to insert into database"
    )
    parser.add_argument('type', help="employee, client or survey")
    parser.add_argument('-n', help="number of records", default=10)
    parser.add_argument('--change', help='change percent (default = 0)', default=0)
    parser.add_argument('--gender', help='percent of males (default = 50)', default=50)
    parser.add_argument('--kids', help='percent of peoples having kids (default = 50)',default=50)
    parser.add_argument('--last-called', help='when was the last call maximum in years (default = 1)',default=1)
    parser.add_argument('--dismissal', help='dismissal percent (default = 20)',default=20)
    parser.add_argument('--completed', help='surveys completed percent (default = 60',default=60)
    parser.add_argument('--phone', help='what is the percent of surveys conducted by calls',default=80)
    parser.add_argument('--min-salary', help='minimum salary of the employees', default=2000)
    parser.add_argument('--max-salary', help='maximum salary of the employees', default=5000)


    args=(parser.parse_args()) 
    NUMBER_OF_RECORDS = args.n
    CHANGE_PERCENT = args.change
    GENDER_PERCENT = args.gender
    KIDS_PERCENT = args.kids
    LAST_CALLED = args.last_called
    DISMISSAL_RATE = args.dismissal
    COMPLETED_PERCENT = args.completed
    PHONE_PRECENT = args.phone
    MINIMUM_SALARY = args.min_salary
    MAXIMUM_SALARY = args.max_salary
    if args.type == 'employee':
        print('generating employees...')
        employees = [EmployeeFactory.generate_employee() for i in range(int(NUMBER_OF_RECORDS))]
        with open("employee_file.csv", mode="w") as employee_file:
            employee_writer = csv.writer(
                employee_file, delimiter=",", quotechar='"', quoting=csv.QUOTE_MINIMAL
            )
            employee_writer.writerow(
                [
                    "employee_id",
                    "first_name",
                    "last_name",
                    "dob",
                    "gender",
                    "employment_date",
                    "dismissal_date",
                    "education",
                    "salary",
                ]
            )
            for employee in employees:
                employee_writer.writerow(vars(employee).values())
    elif args.type == 'client':
        print('generating clients...')
        clients = [ClientFactory.generate_client() for i in range(int(NUMBER_OF_RECORDS))]
        with open("clients_file.csv", mode="w") as clients_file:
            clients_writer = csv.writer(
                clients_file, delimiter=",", quotechar='"', quoting=csv.QUOTE_MINIMAL
            )
            clients_writer.writerow(
                [
                    "client_id",
                    "first_name",
                    "last_name",
                    "dob",
                    "gender",
                    "profession",
                    "dismissal_date",
                    "has_kids",
                    "education",
                    "email",
                    "phone",
                    "last_called",
                    "is_married"
                ]
            )
            for client in clients:
                clients_writer.writerow(vars(client).values())
    elif args.type == 'conductedsurvey':
        print('generating conduted surveys')
        with open("employee_file.csv", mode="r") as employee_file: 
            csv_reader = csv.reader(employee_file, delimiter=",", quotechar='"')
            csv_headings = next(csv_reader)
            employees_ids = []
            for line in csv_reader:
                employees_ids.append(line[0])        
        with open("clients_file.csv", mode="r") as clients_file: 
            csv_reader = csv.reader(clients_file, delimiter=",", quotechar='"')
            csv_headings = next(csv_reader)
            clients_ids = []
            for line in csv_reader:
                clients_ids.append(line[0])

                  
        conducted_surveys = [ConductedSurveyFactory.generate_conducted_survey() for i in range(NUMBER_OF_RECORDS)]

    elif args.type == 'survey':
        print('generating surveys...')

        surveys = [SurveyFactory.generate_survey() for i in range(int(NUMBER_OF_RECORDS))]
        with open("survey.csv", mode="w") as survey_file:
            survey_writer = csv.writer(
                survey_file, delimiter=",", quotechar='"', quoting=csv.QUOTE_MINIMAL
            )
            survey_writer.writerow(
                [
                    "survey_id",
                    "survey_content",
                    "title",
                    "company_name",
                    # "survey_html",
                   
                ]
            )
            for survey in surveys:
                survey_writer.writerow(vars(survey).values())

        
        
    else:
        print('Wrong option type --help for usage')
   
        
    









    # try:
    #     connection = psycopg2.connect(
    #         user="datawarehouses",
    #         password="datawarehouses",
    #         host="127.0.0.1",
    #         port="5432",
    #         database="datawarehouses",
    #     )
    #     with connection.cursor() as cursor:
    #         base = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    #         fixture_path = os.path.join(base, "generator/employee_file.csv")
    #         with open(fixture_path) as f:
    #             try:
    #                 next(f)
    #                 cursor.copy_from(f, "employee", sep=",")
    #                 connection.commit()
    #             except UniqueViolation:
    #                 pass
    #         print("copied")
    # except (Exception, psycopg2.Error) as error:
    #     print("Error while connecting to PostgreSQL", error)
