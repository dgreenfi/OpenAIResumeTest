# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

#important packages to load key and call API
import os
import openai
from dotenv import load_dotenv
from pathlib import Path


def test_auth():
    dotenv_path = Path('OAI.env')
    load_dotenv(dotenv_path=dotenv_path)
    openai.api_key = os.getenv('OPENAI_API_KEY')
    openai.Model.list()
    return openai

def auth_openai():
    print("Do Later")

def example_query():
    # where my key is stored
    dotenv_path = Path('OAI.env')
    load_dotenv(dotenv_path=dotenv_path)
    openai.api_key = os.getenv('OPENAI_API_KEY')
    resp = openai.Completion.create(
        model="text-davinci-003",
        prompt="write a poem about trying the Open AI API",
        max_tokens=128,
        temperature=0.5)
    print(resp)


def basequery():
    dotenv_path = Path('OAI.env')
    load_dotenv(dotenv_path=dotenv_path)
    openai.api_key = os.getenv('OPENAI_API_KEY')
    resp = openai.Completion.create(
        model="davinci:ft-personal-2022-12-22-19-32-33",
        prompt="write a cover lever for David Greenfield highlighting his work at Veeva and Komodo",
        max_tokens=128,
        temperature=0.9)
    print(resp)

def train_model(basemodel,trainset,num_epochs):
    dotenv_path = Path('OAI.env')
    load_dotenv(dotenv_path=dotenv_path)
    openai.api_key = os.getenv('OPENAI_API_KEY')
    response = openai.Completion.create(
        engine=basemodel,
        prompt="Summarize eqloquently David Greenfield's contributions at Veeva and Komodo",
        max_tokens=None,
        temperature=None,
        top_p=None,
        frequency_penalty=0,
        presence_penalty=0,
        best_of=1,
        n=1,
        data=trainset,
    )



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    #train_model('text-davinci-003', 'resume_train.JSONL',3)
    #example_query()
    basequery()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
