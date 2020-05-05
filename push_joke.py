import requests
import random
import json

def open_joke_file(file_path: str):
    with open(file_path,"r") as file:
        jokes = json.load(file)
    return jokes