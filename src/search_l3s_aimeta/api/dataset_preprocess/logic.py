import os
import json, requests
from requests.exceptions import JSONDecodeError
import unicodedata
import sys
from pathlib import Path
from flask import abort
import re


from bs4 import BeautifulSoup
sys.path.append(os.getcwd())


# LOGIN_PAYLOAD = {
#   "client_id": os.getenv("MLS_CLIENT_ID"),
#   "client_secret": os.getenv("MLS_CLIENT_SECRET"),
#   "username": os.getenv("MLS_USERNAME"),
#   "password": os.getenv("MLS_PASSWORD"),
#   "grant_type": os.getenv("MLS_GRANT_TYPE")
# }

from dotenv import load_dotenv

load_dotenv()


class Text_Preprocess(object):

    def __init__(self) -> None:
        pass
 
    VALID_CONTENT_TYPE = {
        "DOCUMENTS": "documents",
        "EXTERNAL_EUROPATHEK_BOOK": "external-europathek-books",
        "FILE_RESOURCES": "file-resources",
        "FORM_FILE": "form-files"
    }
        
    VALID_PARAMETER_NAME = [
            "page", "itemsPerPage", "pagination", "id", "title", "lifecycle", "taskSet",
            "taskSet.title", "taskSet.organization", "appTags", "appTags.context",
            "groupTaskTodos", "originalTask", "externalContents", "externalContentOrganizations",
            "taskTodos.user.organizations", "taskTodos.taskTodoInfo.status", "taskSteps.connectedForms",
            "mls1Id", "userNameOrFilter", "todoOrFilter", "orFilter", "creatorNameOrFilter", "isNewestVersion", "order[title]", "order[taskSet.title]", "order[creator.username]", "taskTodos.archived"
        ]
        
    LOGIN_PAYLOAD = {
            "client_id": os.getenv("MLS_CLIENT_ID"),
            "client_secret": os.getenv("MLS_CLIENT_SECRET"),
            "username": os.getenv("MLS_USERNAME"),
            "password": os.getenv("MLS_USER_PASSWORD"),
            "grant_type": os.getenv("MLS_GRANT_TYPE")
            }
    
    @classmethod
    def __get_auth_header(self):
        base_url = os.getenv("MLS_BASE_URL")
        login_server_url = os.getenv("MLS_LOGIN_SERVER_URL")
        realm = os.getenv("MLS_REALM")

        assert os.getenv("MLS_BASE_URL") is not None, "Environment variable 'MLS_BASE_URL' is not defined. Please update/add env variable."
        assert os.getenv("MLS_LOGIN_SERVER_URL") is not None, "Environment variable 'MLS_LOGIN_SERVER_URL' is not defined. Please update/add env variable."
        assert os.getenv("MLS_REALM") is not None, "Environment variable 'MLS_REALM' is not defined. Please update/add env variable."
        assert os.getenv("MLS_CLIENT_ID") is not None, "Environment variable 'MLS_CLIENT_ID' is not defined. Please update/add env variable."
        assert os.getenv("MLS_CLIENT_SECRET") is not None,  "Environment variable 'MLS_CLIENT_SECRET' is not defined. Please update/add env variable."
        assert os.getenv("MLS_USERNAME") is not None,  "Environment variable 'MLS_USERNAME' is not defined. Please update/add env variable."
        assert os.getenv("MLS_USER_PASSWORD") is not None,  "Environment variable 'MLS_USER_PASSWORD' is not defined. Please update/add env variable."
        assert os.getenv("MLS_GRANT_TYPE") is not None,  "Environment variable 'MLS_GRANT_TYPE' is not defined. Please update/add env variable."

        # get login response
        login_response = requests.post(login_server_url + "/realms/" + realm + "/protocol/openid-connect/token",
                data = self.LOGIN_PAYLOAD,
                headers =  {
                "Content-Type": "application/x-www-form-urlencoded",
                # "Content-Type": "application/json",
                }
            )

        # get access token
        access_token = login_response.json()["access_token"]
        # create authenication header
        auth_header = {
            "Authorization": "Bearer " + access_token,
            "Content-Type": "application/json"
            }
        return auth_header
    


    @classmethod
    def get_taskstep_response(self, object_id):
        auth_header = self.__get_auth_header()

        try: 
            assert int(object_id)>0, "Invalid value of taskstep ID. Please try with a positive integer."
        except ValueError:
            raise ValueError(" This format of task step id is not accepted. Please provide the task step ID in correct foramt.")            

        taskstep_response = requests.get(os.getenv("MLS_BASE_URL") + "/mls-api/task-steps/" + object_id, headers=auth_header)
    
        assert taskstep_response.json()['@context'].split("/")[-1]!="Error", "Invalid taskstep ID. The taskstep ID does not exist."

        return taskstep_response

    @classmethod
    def get_all_tasksteps_response(self, task):
        auth_header = self.__get_auth_header()
        all_tasksteps_response = requests.get(os.getenv("MLS_BASE_URL") + "/mls-api/task-steps?task=" + task["@id"],
            headers =  auth_header
        )

        return all_tasksteps_response

    @classmethod
    def get_task_response(self, object_id):
        auth_header = self.__get_auth_header()

        try:           
            assert int(object_id)>0, "Invalid value for task ID. Please try with a positive integer."
        except ValueError:
            raise ValueError(" This format of task id is not accepted. Please provide the task ID in correct foramt.")
            
        task_response = requests.get(os.getenv("MLS_BASE_URL") + "/mls-api/tasks/" + object_id, headers=auth_header)


        assert task_response.json()['@context'].split("/")[-1]!="Error", "Invalid Task ID. The task ID does not exist in MLS."

        return task_response

    @classmethod
    def preprocess_text(self, text):
        text = text.replace('\n','')
        text = unicodedata.normalize("NFKD",text)

        return text
    

    @classmethod
    def read_a_taskstep(self, task_step):
        
        assert 'id' in task_step.keys(), "Invalid Task Step ID."

        text = ' '  
        if not len(task_step['content'])>0:
            return text
        
        for i in range(len(task_step['content'])):
            if task_step["content"][i]['type']==1:
                task_step_html = task_step['content'][i]['value']
                soup = BeautifulSoup(task_step_html, 'html.parser')    
                sub_text = soup.get_text(strip=True,separator=' ') #(separator='\n')

                double_title = task_step["title"] + ' ' + task_step["title"]
                if double_title in sub_text:
                    sub_text = sub_text.replace(double_title, task_step["title"] )
                sub_text = self.preprocess_text(sub_text)
                text+=sub_text
             

        return text


    @classmethod
    def read_a_task(self, task):
        assert 'id' in task.keys(), "Invalid Task ID."
            
        task_id = task["id"]
        task_title = task["title"]

        if 'taskSet' in task.keys():    
            task_set_id = task['taskSet'].split("/")[-1]
        else:
            task_set_id = None                

        task_steps_response  = self.get_all_tasksteps_response(task)

        text = ' '
        task_step_ids = []
        i=1  
        for task_step in task_steps_response.json()["hydra:member"]:
            task_step_text = ' '+str(i)+ '. '+ task_step["title"]+": "+ self.read_a_taskstep(task_step) #
            text +=task_step_text
            i+=1
            task_step_ids.append(task_step["id"])

        return task_id, task_title, text, task_step_ids, task_set_id        


    @classmethod
    def pre_process_taskstep(self, id):
        taskstep_response = self.get_taskstep_response(id)
        task_step = taskstep_response.json()
        text = self.read_a_taskstep(task_step)
        result = {'taskstep_id':id, 'taskstep_text':text}

        return result
    
    @classmethod
    def pre_process_task(self, id):
        task_response = self.get_task_response(id)
        
        task_response = task_response.json()


        task_id, task_title, text, task_step_ids, task_set_id  = self.read_a_task(task_response)

        result = {'task_id':task_id,
                  'task_title':task_title,
                  'text':text,
                  'tasksteps_ids':task_step_ids,
                  'task_set_id':task_set_id
                  }

        return result


