import os
import json, requests
from requests.exceptions import JSONDecodeError
import sys
import unicodedata
from pathlib import Path


# sys.path.append(os.getcwd())
# sys.path.append('..')
# sys.path.append('.')


from search_l3s_aimeta.api.dataset_preprocess.logic import Text_Preprocess

from dotenv import load_dotenv
load_dotenv()
load_dotenv(dotenv_path=Path("src/search_l3s_aimeta/.env_env"))


API_KEY = os.getenv("OPENAI_API_KEY")
API_ENDPOINT = os.getenv("API_ENDPOINT")
                   


class ContentKeywords(Text_Preprocess,object):

    def __init__(self) -> None:
        super().__init__()

    @classmethod
    def generate_chat_completion(self, messages, model="gpt-3.5-turbo", temperature=1, max_tokens=None):
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {API_KEY}",
        }

        data = {
            "model": model,
            "messages": messages,
            "temperature": temperature,
        }

        if max_tokens is not None:
            data["max_tokens"] = max_tokens

        response = requests.post(API_ENDPOINT, headers=headers, data=json.dumps(data))

        if response.status_code == 200:
            return response.json()["choices"][0]["message"]["content"]
        else:
            raise Exception(f"Error {response.status_code}: {response.text}")
        

    @classmethod
    def preprocess_text(self, text):
        text = text.replace('\n',' ')
        text = unicodedata.normalize("NFKD",text)

        return text
        

    @classmethod
    def generate_content_keywords(self, id):

        user_message =  "Extrahiere aus nachfolgender Lerneinheit die maximal zehn wichtigsten Schlüsselworte im comma separated list Format. Format: [<schlüsselwort>, <schlüsselwort>, ...]"

        system_messages = "Sie sind ein hilfreicher Assistent, der die Schlüsselwörter aus einer bestimmten Lerneinheit extrahiert."


        text = Text_Preprocess.pre_process_task(id)   

        max_tokens = 4096
        input_text = user_message + text['text']
        if len(input_text.split()) > max_tokens:
            input_text = ' '.join(input_text.split()[:max_tokens])


        messages = [
            {"role": "system", "content": system_messages},
            {"role": "user", "content": input_text}
        ]

        response_text = self.generate_chat_completion(messages)
        response_text = self.preprocess_text(response_text)
        

        

        return {"Content Keywords":response_text}

    




        

