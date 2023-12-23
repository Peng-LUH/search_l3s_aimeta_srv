import os
import json, requests
from requests.exceptions import JSONDecodeError
import sys
import unicodedata
from pathlib import Path
from flask import abort
import tiktoken

from search_l3s_aimeta.api.dataset_preprocess.logic import Text_Preprocess

from dotenv import load_dotenv
load_dotenv()

API_KEY = os.getenv("OPENAI_API_KEY")
API_ENDPOINT = os.getenv("API_ENDPOINT")
                   

class Quiz(Text_Preprocess,object):

    def __init__(self) -> None:
        super().__init__()

    @classmethod
    def generate_chat_completion(self, messages, model="gpt-3.5-turbo", temperature=1, max_tokens=None):
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {API_KEY}",
        }

        assert API_KEY is not None, "Environment variable 'OPENAI_API_KEY' is not defined. Please update/add env variable."
        assert API_ENDPOINT is not None,  "Environment variable 'API_ENDPOINT' is not defined. Please update/add env variable."
            
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
            raise ValueError("Model did not generate output. Please try again with valid API_KEY and input data.")


    @classmethod
    def preprocess_text(self, text):
        text = text.replace('\n',' ')
        text = unicodedata.normalize("NFKD",text)

        return text
    
    @classmethod
    def post_process_text(self, text):
        json_start = text.find('```json')
        if json_start == -1:
            raise ValueError(" The output can not be converted into json fomat. Please try again.")
        else:
            json_start += 7  
            json_end = text.find('```', json_start)
            if json_end == -1:
                raise ValueError(" The output can not be converted into json fomat. Please try again.")
            else:
                json_content = text[json_start:json_end].strip()

        print(json_content)
        return json.loads(json_content)
    
    @classmethod    
    def num_tokens_from_text(self,text, encoding_name):
        """Returns the number of tokens in a text string."""
        encoding = tiktoken.encoding_for_model(encoding_name)
        num_tokens = len(encoding.encode(text))
        return num_tokens    
    


    @classmethod
    def generate_quiz(self, id):

        model_name = "gpt-3.5-turbo"


        user_message =  """Erstelle zu nachfolgendem Lerninhalt jeweils zwei Fragen auf bloomscher Taxonomiestufe "Wissen", "Verstehen" und "Anwenden" in dictionary Format. Format: {"Wissen": [<question>, <question>, ... , <question>], "Verstehen": [<question>, <question>, ... , <question>], "Anwenden": [<question>, <question>, ... , <question>]} """

        system_messages = "Sie sind ein hilfreicher Assistent, der Fragen aus einer bestimmten Lerneinheit generiert."

        text = Text_Preprocess.pre_process_task(id)['text']

        max_tokens = 4096

        total_tokens = self.num_tokens_from_text(text,model_name) + self.num_tokens_from_text(user_message,model_name) + self.num_tokens_from_text(system_messages,model_name)



        if total_tokens > max_tokens:
            model_name = "gpt-3.5-turbo-16k"
        elif total_tokens > 16000:
            model_name = "gpt-4-32k"
        elif total_tokens > 32000:
            raise ValueError("Input text is too long to handle. Please use shorter text.")                    


        input_text = user_message + text



        messages = [
            {"role": "system", "content": system_messages},
            {"role": "user", "content": input_text}
        ]

        response_text = self.generate_chat_completion(messages=messages,model=model_name)
        response_text = self.preprocess_text(response_text)

        try:
            quiz_questions = json.loads(response_text)
        except json.JSONDecodeError:
            try:
                quiz_questions = self.post_process_text(response_text)
            except  json.JSONDecodeError:
                raise ValueError('Invalid JSON response. Please try Again.')  
            except ValueError as e:
                raise ValueError(f"Error in post-processing: {e}")         

        return {"task_id":id, "quiz_questions":quiz_questions} 



