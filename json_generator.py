import json
import random
from faker import Faker

MAX_DURATION = 15


""" Makes single survey file + all of the answers files to that survey. """
def write_survey_and_answers_files(filename,
                                   save_path="./surveys/",
                                   number_of_questions=10, nr_of_completed_surveys=100):
    write_survey(filename, save_path, number_of_questions)
    for i in range(nr_of_completed_surveys):
        write_answer(str(i), filename, save_path, number_of_questions)


def write_survey(filename, save_path="./surveys/", number_of_questions=10):
    fake = Faker()
    survey_data = return_survey_data(fake.bs(), fake.company(), number_of_questions)
    create_json_file(save_path + filename, survey_data)


def write_answer(filename, save_path="./survey/", number_of_questions=10):
    fake = Faker()
    answer_data = return_client_answers(fake.uuid4(),
                                        filename,
                                        random.random()*MAX_DURATION,
                                        random.randint(0, number_of_questions))
    create_json_file(save_path + filename, answer_data)


def create_json_file(filename, data):
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)


def return_survey_data(topic, company, number_of_questions):
    return {
        "topic": topic,
        "company": company,
        "number_of_questions": number_of_questions,
        "questions": return_list_of_questions(number_of_questions)
    }


def return_list_of_questions(number_of_questions):
    container = []
    for i in range(number_of_questions):
        container.append({"question": str(i),
                     "possible_answers": ["a", "b", "c", "d"]})
    return container


def return_client_answers(client_id, survey_data_filename, minutes, number_of_answers):
    return {
        "client_id": client_id,
        "duration": minutes,
        "number_of_answers": number_of_answers,
        "questions": return_list_of_answers(number_of_answers)
    }


def return_list_of_answers(number_of_answers):
    list = []
    possible_answers = ["a", "b", "c", "d"]
    for i in range(number_of_answers):
        list.append({"question": str(i),
                     "answer": possible_answers[random.randint(0, 3)]})
    return list
