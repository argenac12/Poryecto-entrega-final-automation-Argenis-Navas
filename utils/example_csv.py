
import os 
import csv
import json

def get_login_csv(csv_file="data/data_login.csv"):

    current_file = os.path.dirname(__file__)
    csv_file = os.path.join(current_file,"..","data",csv_file)
    #../data/data_login.csv
    csv_file = os.path.abspath(csv_file)

    casos = []

    with open(csv_file, newline="") as h:
        read = csv.DictReader(h)

        for i in read:
            username = i["username"]
            password = i["password"]
            login_example = i["login_example"].lower() =="true"
            casos.append((username,password,login_example))

        return casos
    
def get_login_json(json_file="data_login.json"):
    current_file = os.path.dirname(__file__)
    json_file = os.path.join(current_file,"..","data",json_file)
        #../data/data_login.csv
    json_file = os.path.abspath(json_file)

    casos = []

    with open(json_file) as j:
        datos = json.load(j)
        for i in datos:
         username = i["username"]
         password = i["password"]
         login_example = i["login_example"]
        casos.append((username, password, login_example))
        return casos

            
        
                 

