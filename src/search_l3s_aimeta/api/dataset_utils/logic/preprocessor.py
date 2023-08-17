import os
import sys
import json
from http import HTTPStatus



# 1. sys.path.append(".") and
# 2. sys.path.append(os.getcwd()) both add current wd to sys.path and current wd works as importable moudule/package
# Also, since cwd = "/home/rathee/search/aims/search_l3s_aimeta_srv/src/search_l3s_aimeta" so 
#sys.path.append("/home/rathee/search/aims/search_l3s_aimeta_srv/src/search_l3s_aimeta") will do same thing


sys.path.append(os.getcwd())
from search_l3s_aimeta.util.path import get_dataset_path



def dataset_json2jsonl(dataset_name):
    
    dataset_dir_path = get_dataset_path(dataset_name)
    dataset_json_file = os.path.join(dataset_dir_path, "json/data.json")
    dataset_jsonl_dir = os.path.join(dataset_dir_path, "jsonl")
    
    try:
        with open(dataset_json_file) as f:
                data = json.load(f)
    except FileNotFoundError as e:
            result = {"error": f"File not found: {e}", "code": HTTPStatus.NOT_FOUND}
            return result
        
    
    if not os.path.exists(dataset_jsonl_dir):
        os.makedirs(dataset_jsonl_dir)
    
    for d in data:
        d["@id"] = d["id"]
        d["id"] = int(d["id"].split("/")[-1])

        with open(f"{dataset_dir_path}/jsonl/data.jsonl", "w") as jsonl_file:
                for d in data:
                    json.dump(d, jsonl_file)
                    jsonl_file.write('\n')
    
    return 1