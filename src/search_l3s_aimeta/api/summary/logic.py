import os
import json, requests
from requests.exceptions import JSONDecodeError
import sys
import unicodedata
from pathlib import Path
from flask import abort
import tiktoken


# sys.path.append(os.getcwd())
# sys.path.append('..')
# sys.path.append('.')


from search_l3s_aimeta.api.dataset_preprocess.logic import Text_Preprocess

from dotenv import load_dotenv
load_dotenv()

API_KEY = os.getenv("OPENAI_API_KEY")
API_ENDPOINT = os.getenv("API_ENDPOINT")
                   
assert os.getenv("OPENAI_API_KEY") is not None, abort(501, "Environment variable 'OPENAI_API_KEY' is not defined. Please update/add env variable.")
assert os.getenv("API_ENDPOINT") is not None, abort(501, "Environment variable 'API_ENDPOINT' is not defined. Please update/add env variable.")


class Summary(Text_Preprocess,object):

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
    def num_tokens_from_text(self,text, encoding_name):
        """Returns the number of tokens in a text string."""
        encoding = tiktoken.encoding_for_model(encoding_name)
        num_tokens = len(encoding.encode(text))
        return num_tokens    
    

    @classmethod
    def generate_summary(self, id):
        model_name = "gpt-3.5-turbo"


        user_message =  "Formuliere für nachfolgende Lerneinheit eine kurze (maximal 200 Worte) aber motivierende Zusammenfassung :"

        system_messages = "Sie sind ein hilfreicher Assistent, der Lerninhalte zusammenfasst."

        text = Text_Preprocess.pre_process_task(id)['text']
        total_tokens = self.num_tokens_from_text(text,model_name) + self.num_tokens_from_text(user_message,model_name) + self.num_tokens_from_text(system_messages,model_name)


        max_tokens = 4096

        if total_tokens > max_tokens:
            model_name = "gpt-3.5-turbo-16k"
        elif total_tokens > 16000:
            model_name = "gpt-4-32k"
        elif total_tokens > 32000:
            abort(400, "Input text is too long to handle. Please use shorter text.")                    

        input_text = user_message + text


        messages = [
            {"role": "system", "content": system_messages},
            {"role": "user", "content": input_text}
        ]

        response_text = self.generate_chat_completion(messages=messages,model=model_name)
        response_text = self.preprocess_text(response_text)
        

        try:
            response = f"{response_text}"
            return response
        except:
                abort(400, 'Invalid response type. Please try Again.')   

        # else:
        #     response = f"{response_text}"
        #     abort(400, 'Invalid response type. Please try Again.')   


    




        

#aims = Summary()

# text = aims.summary('10')
# print(text)

