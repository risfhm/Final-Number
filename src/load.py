import json
import argparse
from os import path

PATH="config.json"

def get_name():
    
    if not path.exists(PATH):
        update_name("Unknown_Player")
    
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
