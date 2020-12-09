import requests
import random
from bs4 import BeautifulSoup
from fake_exmoslem_questions.template import terms, question_templates


def generate_question():
    working_question = []
    session = requests.session()

    while not working_question:
        term_list = terms
        term1_index = random.randrange(len(term_list))
        term1 = term_list[term1_index]
        term_list.pop(term1_index)

        term2 = term_list[random.randrange(len(term_list))]
        question = question_templates[random.randrange(
            len(question_templates))].format(term1, term2)

        response = session.get(
            "https://google.com/search", params={"q": question})
        soup = BeautifulSoup(response.text, "html.parser")
        working_question = soup.select(
            "div.Ap5OSd > div.BNeawe.s3v9rd.AP7Wnd > span.FCUp0c.rQMQod")

    return (question, working_question[0].text)


def main():
    print(generate_question())
