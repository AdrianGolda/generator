import argparse
from random_data import education
import csv
from faker import Faker
import random
from employee_dto import EmployeeFactory
from client_dto import ClientFactory
from survey_dto import ConductedSurveyFactory, SurveyFactory
import logging
import pyodbc
import os

NUMBER_OF_RECORDS: int = 10
CHANGE_PERCENT = 5
GENDER_PERCENT = 50
KIDS_PERCENT = 50
LAST_CALLED = 1
DISMISSAL_RATE = 20
COMPLETED_PERCENT = 60
PHONE_PERCENT = 80
MINIMUM_SALARY = 2000
MAXIMUM_SALARY = 5000


def change_history_data(str_data_type):
    faker = Faker()
    if str_data_type == 'employee':
        with open('employee_file.csv', newline='', mode='r') as csvfile:
            logging.basicConfig(filename="changes.log",
                                level=logging.INFO,
                                format="Change info: employee's %(message)s")
            possible_changes = ['first_name', 'last_name', 'gender', 'education', 'salary']
            reader = csv.DictReader(csvfile)
            employee_data = []
            for row in reader:
                employee_data.append(row)
            nr_of_records = len(employee_data)
            for i in range(int(float(CHANGE_PERCENT) / 100.0 * float(nr_of_records))):
                changed_employee = random.choice(employee_data)
                value_to_change = random.choice(list(changed_employee.keys()))
                while value_to_change not in possible_changes:
                    value_to_change = random.choice(list(changed_employee.keys()))
                if value_to_change == 'first_name':
                    old_name = changed_employee['first_name']
                    if changed_employee['gender'] == 1:
                        changed_employee['first_name'] = faker.first_name_male()
                    else:
                        changed_employee['first_name'] = faker.first_name_female()
                    logging.info(f"(id: {changed_employee['employee_id']}) first name changed: {old_name} => {changed_employee['first_name']}")
                elif value_to_change == 'last_name':
                    old_last = changed_employee['last_name']
                    changed_employee['last_name'] = faker.last_name()
                    logging.info(f"(id: {changed_employee['employee_id']}) last name changed: {old_last} => {changed_employee['last_name']}")
                elif value_to_change == 'gender':
                    changed_employee['gender'] = int(changed_employee['gender']).__xor__(1)
                    logging.info(f"(id: {changed_employee['employee_id']}) gender changed: {int(changed_employee['gender']).__xor__(1)} => {changed_employee['gender']}")
                elif value_to_change == 'education':
                    old_education = changed_employee['education']
                    changed_employee['education'] = random.choice(education)
                    logging.info(f"(id: {changed_employee['employee_id']}) education degree changed: {old_education} => {changed_employee['education']}")
                elif value_to_change == 'salary':
                    old_salary = changed_employee['salary']
                    changed_employee['salary'] = random.randrange(2000, 5000, 100)
                    logging.info(f"(id: {changed_employee['employee_id']}) salary changed: {old_salary} => {changed_employee['salary']}")
        with open('employee_file.csv', newline='', mode='w') as csvfile:
            writer = csv.writer(
                csvfile, delimiter=",", quotechar='"', quoting=csv.QUOTE_MINIMAL
            )
            writer.writerow(
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
            for employee in employee_data:
                writer.writerow(employee.values())
    if str_data_type == 'client':
        logging.basicConfig(filename="changes.log",
                            level=logging.INFO,
                            format="Change info: client's %(message)s")
        with open('clients_file.csv', newline='', mode='r') as csvfile:
            possible_changes = ['first_name', 'last_name', 'gender', 'profession', 'has_kids', 'education', 'is_married']
            reader = csv.DictReader(csvfile)
            client_data = []
            for row in reader:
                client_data.append(row)
            nr_of_records = len(client_data)
            for i in range(int(float(CHANGE_PERCENT) / 100.0 * float(nr_of_records))):
                changed_client = random.choice(client_data)
                value_to_change = random.choice(list(changed_client.keys()))
                while value_to_change not in possible_changes:
                    value_to_change = random.choice(list(changed_client.keys()))
                if value_to_change == 'first_name':
                    old_name = changed_client['first_name']
                    if changed_client['gender'] == 1:
                        changed_client['first_name'] = faker.first_name_male()
                    else:
                        changed_client['first_name'] = faker.first_name_female()
                    logging.info(
                        f"(id: {changed_client['client_id']}) first name changed: {old_name} => {changed_client['first_name']}")
                elif value_to_change == 'last_name':
                    old_last = changed_client['last_name']
                    changed_client['last_name'] = faker.last_name()
                    logging.info(
                        f"(id: {changed_client['client_id']}) last name changed: {old_last} => {changed_client['last_name']}")
                elif value_to_change == 'gender':
                    changed_client['gender'] = int(changed_client['gender']).__xor__(1)
                    logging.info(
                        f"(id: {changed_client['client_id']}) gender changed: {int(changed_client['gender']).__xor__(1)} => {changed_client['gender']}")
                elif value_to_change == 'education':
                    old_education = changed_client['education']
                    changed_client['education'] = random.choice(education)
                    logging.info(
                        f"(id: {changed_client['client_id']}) education degree changed: {old_education} => {changed_client['education']}")
                elif value_to_change == 'profession':
                    old_job = changed_client['profession']
                    changed_client['profession'] = faker.job()
                    logging.info(
                        f"(id: {changed_client['client_id']}) job changed: {old_job} => {changed_client['profession']}")
                elif value_to_change == 'has_kids':
                    changed_client['has_kids'] = int(changed_client['has_kids']).__xor__(1)
                    logging.info(
                        f"(id: {changed_client['client_id']}) kids status changed: {int(changed_client['has_kids']).__xor__(1)} => {changed_client['has_kids']}")
                elif value_to_change == 'is_married':
                    changed_client['is_married'] = int(changed_client['is_married']).__xor__(1)
                    logging.info(
                        f"(id: {changed_client['client_id']}) marriage status changed: {int(changed_client['is_married']).__xor__(1)} => {changed_client['is_married']}")
        with open('clients_file.csv', newline='', mode='w') as csvfile:
            writer = csv.writer(
                csvfile, delimiter=",", quotechar='"', quoting=csv.QUOTE_MINIMAL
            )
            writer.writerow(
                [
                    "client_id",
                    "first_name",
                    "last_name",
                    "dob",
                    "gender",
                    "profession",
                    "has_kids",
                    "education",
                    "email",
                    "phone",
                    "last_called",
                    "is_married"
                ]
            )
            for client in client_data:
                writer.writerow(client.values())


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Generate information for Employees, Clients, Survey to insert into database"
    )
    parser.add_argument('type', help="employee, client, conductedsurvey or survey")
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
    PHONE_PERCENT = args.phone
    MINIMUM_SALARY = args.min_salary
    MAXIMUM_SALARY = args.max_salary

    if args.type == 'employee':
        print('generating employees...')
        if int(CHANGE_PERCENT) > 0:
            change_history_data('employee')
        employees = [EmployeeFactory.generate_employee(GENDER_PERCENT,DISMISSAL_RATE, MINIMUM_SALARY, MAXIMUM_SALARY) for i in range(int(NUMBER_OF_RECORDS))]
        with open("employee_file.csv", mode="a",newline="") as employee_file:
            employee_writer = csv.writer(
                employee_file, delimiter=",", quotechar='"', quoting=csv.QUOTE_MINIMAL
            )
            if int(CHANGE_PERCENT) == 0:
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
        if int(CHANGE_PERCENT) > 0:
            change_history_data('client')
        clients = [ClientFactory.generate_client(GENDER_PERCENT,KIDS_PERCENT) for i in range(int(NUMBER_OF_RECORDS))]
        with open("clients_file.csv", mode="a", newline="") as clients_file:
            clients_writer = csv.writer(
                clients_file, delimiter=",", quotechar='"', quoting=csv.QUOTE_MINIMAL
            )
            if int(CHANGE_PERCENT) == 0:
                clients_writer.writerow(
                    [
                        "client_id",
                        "first_name",
                        "last_name",
                        "dob",
                        "gender",
                        "profession",
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
        conducted_surveys = [ConductedSurveyFactory.generate_conducted_survey(employees_ids, clients_ids) for i in range(int(NUMBER_OF_RECORDS))]
        with open("conductedsurvey.csv", mode="w",newline="") as survey_file:
            survey_writer = csv.writer(
                survey_file, delimiter=",", quotechar='"', quoting=csv.QUOTE_MINIMAL
            )
            survey_writer.writerow(
                [
                    "conducted_survey_id",
                    "employees_id",
                    "clients_id",
                    "survey_id",
                    "answers",
                    "datetime",
                    "email_or_phone",
                    "is_completed"
                    # "survey_html",
                   
                ]
            )
            for survey in conducted_surveys:
                survey_writer.writerow(vars(survey).values())
    elif args.type == 'survey':
        print('generating surveys...')
        surveys = [SurveyFactory.generate_survey() for i in range(int(NUMBER_OF_RECORDS))]
        with open("survey.csv", mode="w",newline="") as survey_file:
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








    try:
        connection = pyodbc.connect(driver='{SQL Server}',
                               server='DESKTOP-R4RQFGR\MSSQLSERVER02',
                               database='datawarehouses',
                                
                               

        )
        # (1) Execution Example with MySQL ODBC
        sql = """
            BULK INSERT datawarehouses.dbo.Employee
            FROM 'C:\\Users\\adrgo\\generator\\employee_file.csv' WITH (
                FIELDTERMINATOR='\\t',
                ROWTERMINATOR='\\n'
                );
            """
        with connection.cursor() as cursor:
            base = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
            fixture_path = os.path.join(base, "generator/employee_file.csv")
            with open(fixture_path) as f:
                try:
                    next(f)
                    cursor.execute(sql)
                    # cursor.copy_from(f, "employee", sep=",")
                    connection.commit()
                except Exception as e:
                    print("Error while copying to MSSQL", e)
            print("copied")
    except (Exception) as e:
        print("Error while connecting to MSSQL", e)
 

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
