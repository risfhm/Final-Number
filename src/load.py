# Obter e atualizar o nome no arquivo de configuração JSON
# Tratar os parâmetros passados pelo usuário

import json
import argparse

PATH="config/config.json"

def get_name():
    
    with open(PATH, "r") as file:
        dict_json = json.load(file)
        
    return dict_json["name"]

def update_name(new_name):
    
    dict_json = {"name":new_name}
    
    with open(PATH, "w") as file:
        json.dump(dict_json, file, indent=2)
        
    return True
        

def parsing():
    
    parser = argparse.ArgumentParser(prog="final-number")
    parser.add_argument("-n", "--name", help="get your new name", type=str)
    
    args = parser.parse_args()
    
    if args.name:
        return update_name(args.name)
    
    return False
