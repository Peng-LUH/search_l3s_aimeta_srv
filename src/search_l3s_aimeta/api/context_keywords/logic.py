import os
import json, requests
from requests.exceptions import JSONDecodeError
import sys
import unicodedata


sys.path.append(os.getcwd())
# sys.path.append('..')
# sys.path.append('.')


from api.dataset_preprocess.logic import Text_Preprocess

from dotenv import load_dotenv
load_dotenv()

API_KEY = os.getenv("OPENAI_API_KEY")
API_ENDPOINT = os.getenv("API_ENDPOINT")
                   


class ContextKeywords(Text_Preprocess,object):

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
    def generate_context_keywords(self, id):

        user_message =  "In welchen fachlichen Kontext passt die nachfolgende Lerneinheit? Antworte im comma separated list Format. Format: [<kontext>, <kontext>, ...]"

        system_messages = "Sie sind ein hilfreicher Assistent, der aus einer gegebenen Lerneinheit Schlüsselwörter für den fachlichen Kontext extrahiert."


        text = Text_Preprocess.pre_process_task(id)   

        max_tokens = 4096
        input_text = user_message + text['text']
        if len(input_text.split()) > max_tokens:
            input_text = ' '.join(input_text.split()[:max_tokens])


        messages = [
            {"role": "system", "content": system_messages},
            {"role": "user", "content": input_text}
        ]

        #response_text = self.generate_chat_completion(messages)
        #response_text = self.preprocess_text(response_text)

        response_text = "testing"

        
        return {"Context Keywords":response_text}

    




        

#aims = Summary()

# text = aims.summary('10')
# print(text)

