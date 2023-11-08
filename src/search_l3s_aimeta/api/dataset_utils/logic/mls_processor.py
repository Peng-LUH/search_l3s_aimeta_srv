import os
import json, requests
from requests.exceptions import JSONDecodeError
from flask import abort


# LOGIN_PAYLOAD = {
#   "client_id": os.getenv("MLS_CLIENT_ID"),
#   "client_secret": os.getenv("MLS_CLIENT_SECRET"),
#   "username": os.getenv("MLS_USERNAME"),
#   "password": os.getenv("MLS_PASSWORD"),
#   "grant_type": os.getenv("MLS_GRANT_TYPE")
# }

from dotenv import load_dotenv

load_dotenv()





class MLSConnector(object):
    
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
    def get_dataset_response(self, dataset_name, parameters=None):
        ## input validation
        # if parameters is not None:
        #     for p in parameters:
        #         for key in p.keys():
        #             if key not in self.VALID_PARAMETER_NAME:
        #                 raise ValueError(f"Invalid Parameter: {key}")
                    
        auth_header = self.__get_auth_header()
        base_url = os.getenv("MLS_BASE_URL")
        
        print(f"parameters: {parameters}")
        
        
        if "/mls-api" in dataset_name:
            dataset_name_url = dataset_name
        else:
            dataset_name_url = "/mls-api/" + dataset_name
        
        # url = base_url+"/mls-api/"+dataset_name
        if parameters is None or parameters == [] or parameters == [{}] or parameters == [{"parameter_name": "string"}]:
            url = base_url + dataset_name_url + "?pagination=false"
        else:
            param_url = ""
            for p in parameters:
                # url_param += p.key()+"="+p.value()
                for key, value in p.items():
                    param_url += key+"="+value+"&"
                
            # print(param_url)
            url = base_url + dataset_name_url + "?" + param_url

        response = requests.get(url, headers=auth_header)
        return response
    
    @classmethod
    def get_object_response(self, object_id):
        auth_header = self.__get_auth_header()
        base_url = os.getenv("MLS_BASE_URL")
        
        url = base_url + object_id
        response = requests.get(url, headers=auth_header)
        
        return response
    

    @classmethod
    def get_task_steps_response(self, object_id):
        auth_header = self.__get_auth_header()
        taskstep_response = requests.get(os.getenv("MLS_BASE_URL") + "/mls-api/task-steps/" + object_id, headers=auth_header)
    

        assert taskstep_response.json()['@context'].split("/")[-1]!="Error", abort(400, "Invalid TaskStep ID.")

        return taskstep_response

    @classmethod
    def get_task_response(self, object_id):
        auth_header = self.__get_auth_header()
        task_response = requests.get(os.getenv("MLS_BASE_URL") + "/mls-api/tasks/" + object_id, headers=auth_header)
    
        assert task_response.json()['@context'].split("/")[-1]!="Error", abort(400, "Invalid Task ID.")

        return task_response
    
    

class MLSCorpus(object):
    
    @classmethod
    def corpus_generator(self, response_json):
        """Generate a corpus in json format"""
        corpus_context = response_json.get("@context")
        corpus_id = response_json.get("@id")
        corpus_data = response_json.get("hydra:member")
        
        if corpus_data is None:
            raise ValueError(description="input is not a collection")
        
        corpus_json = []
        # for data in corpus_data:
            # temp = {}
            # temp["id"] = data["@id"]
            # if data["creator"]:
            #     response = MLSConnector.get_response(data["creator"])
            #     temp["content"] = self.__creator_extractor(response.json())

            # corpus_json.append(temp)
            # for key, value in data.items():
            #     if "/mls-api" in value:
            #         temp_response = MLSConnector.get_response(value)
        
        
        return corpus_json
    
    
    def __creator_extractor(self, response_json):
        """extract information of creator object"""
        if response_json is None:
            raise ValueError("input is none")
        
        
        firstname = response_json.get("firstname")
        lastname = response_json.get("lastname")
        email = response_json.get("email")
        
        creator_info = f"{firstname}; {lastname}; {email}; "
        if response_json.get("organizations"):
            list_orgs = response_json.get("organizations")
            org_info = ""
            for org in list_orgs:
                response_json = MLSConnector.get_response(org).json()
                info = self.__organization_extractor(response_json)
                org_info += info
        
        creator_info += org_info
        return creator_info
    
    
    def __organization_extractor(self, response_json):
        """extract information of organization"""
        name = response_json.get("name")
        streetno = response_json.get("streetno")
        zip = response_json.get("zip")
        city = response_json.get("city")
        country = response_json.get("country")
        
        return f"Organization: {name}, Address: {streetno}, {zip}, {city}, {country}. "
    
    
