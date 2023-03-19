import json
import modules.find_path as f_p 

def create_json(name_dict):
    with open("json.json","w") as file:
        #json.dump([],file)
        file.write(json.dumps(name_dict, ensure_ascii=False, indent=4))

def read_json(name_dict):
    with open(f_p.find_path("json.json"),"r") as file:
        name_dict = json.load(file)