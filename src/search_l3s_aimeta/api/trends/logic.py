import os
import json, requests
from requests.exceptions import JSONDecodeError
import sys
import unicodedata
import base64
import base64
import sys
from pathlib import Path

from urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)



sys.path.append(os.getcwd())
# sys.path.append('..')
# sys.path.append('.')


from dotenv import load_dotenv
load_dotenv()


API_KEY = os.getenv("OPENAI_API_KEY")
API_ENDPOINT = os.getenv("API_ENDPOINT")
                   


class Trends(object):

    def __init__(self) -> None:
        super().__init__()

    @classmethod
    def get_jwt(self):
        """fetch the jwt token object"""
        headers = {
            'User-Agent': 'Jobsuche/2.9.2 (de.arbeitsagentur.jobboerse; build:1077; iOS 15.1.0) Alamofire/5.4.4',
            'Host': 'rest.arbeitsagentur.de',
            'Connection': 'keep-alive',
            'Content-Type': 'application/x-www-form-urlencoded; charset=utf-8',
        }

        data = {
        'client_id': 'c003a37f-024f-462a-b36d-b001be4cd24a',
        'client_secret': '32a39620-32b3-4307-9aa1-511e3d7f48a8',
        'grant_type': 'client_credentials'
        }

        response = requests.post('https://rest.arbeitsagentur.de/oauth/gettoken_cc', headers=headers, data=data, verify=False)

        return response.json()    
    
    @classmethod
    def search(self, jwt, what, where, radius):
        """search for jobs. params can be found here: https://jobsuche.api.bund.dev/"""
        params = (
            ('angebotsart', '1'),
            ('page', '1'),
            ('pav', 'false'),
            #('size', '100'),
            ('umkreis', radius),
            ('was', what),
            ('wo', where),
        )

        headers = {
            'User-Agent': 'Jobsuche/2.9.2 (de.arbeitsagentur.jobboerse; build:1077; iOS 15.1.0) Alamofire/5.4.4',
            'Host': 'rest.arbeitsagentur.de',
            'OAuthAccessToken': jwt,
            'Connection': 'keep-alive',
            "Content-Type": "application/json"
        }

        response = requests.get('https://rest.arbeitsagentur.de/jobboerse/jobsuche-service/pc/v4/app/jobs',
                                headers=headers, params=params, verify=False)
        
        
        return response.json()
    
    @classmethod
    def job_details(self,jwt, job_ref):

        headers = {
            'User-Agent': 'Jobsuche/2.9.3 (de.arbeitsagentur.jobboerse; build:1078; iOS 15.1.0) Alamofire/5.4.4',
            'Host': 'rest.arbeitsagentur.de',
            'OAuthAccessToken': jwt,
            'Connection': 'keep-alive',
        }

        response = requests.get(
            f'https://rest.arbeitsagentur.de/jobboerse/jobsuche-service/pc/v2/jobdetails/{(base64.b64encode(job_ref.encode())).decode("UTF-8")}',
            headers=headers, verify=False)

        return response.json()
    
    @classmethod
    def formal_skills(self, jwt, offers):
        skills = {}
        for offer in offers:
            details = self.job_details(jwt, offer["refnr"])
            if "fertigkeiten" in details:
                skills[offer["refnr"]] = {"job_title" : details["beruf"], "skills" : details["fertigkeiten"]}
        return skills

    @classmethod
    def create_formal_skill_histogram(self, skills_compilation):
        """ key_format := <skill_name>|<skill_level>|<context>   

            value_format := <number_of_occurencies>"""
        histogram = {}
        for k, v in skills_compilation.items():
            for skills_container in v["skills"]:
                context = skills_container["hierarchieName"]
                skill_sets = skills_container["auspraegungen"]
                for level, skills in skill_sets.items():
                    for skill in skills:
                        entry = skill+"|"+level+"|"+context
                        if entry in histogram:
                            histogram[entry] += 1
                        else:
                            histogram[entry] = 1
        return histogram



    




        

# aims = Trends()

# job = "Elektrotechniker/in"
# city = "Berlin"
# radius = 30 #km
# if len(sys.argv) == 3:
#     job = sys.argv[1]
#     city = sys.argv[2]


# # Search for jobs
# jwt = aims.get_jwt()
# print(jwt)
# print('#'*50)
# results = aims.search(jwt["access_token"], job, city, radius)
# print("result", results)
# skills_compilation = aims.formal_skills(jwt["access_token"], results["stellenangebote"])
# print('#'*100)
#print(skills_compilation)
# with open('skills.json', 'w', encoding='utf-8') as f:
#     json.dump(skills_compilation, f, sort_keys=True, indent=2, ensure_ascii=False)


# hist = aims.create_formal_skill_histogram(skills_compilation)
# sorted_kv_list = sorted(hist.items(), key=lambda x:x[1], reverse=True)
# print("<skill>|<skill_level>|<context> --> <frequency>")
# for t in sorted_kv_list:
#     print(t[0] +" --> "+ str(t[1]))