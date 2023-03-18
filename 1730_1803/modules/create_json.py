import json



with open("json.json","w") as file:
    #json.dump([],file)
    file.write(json.dumps(file, ensure_ascii=False, indent=4))


with open("json.json","r") as file:
   json.load(file)