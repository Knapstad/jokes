import requests
import random
import json

from typing import List, Dict

def open_joke_file(file_path: str) -> List:
    with open(file_path,"r") as file:
        jokes = json.load(file)
    return jokes

def push_joke(joke: Dict, hook: str):
    requests.post(hook, json.dumps(joke))

if __name__ == "__main__":
    joke = random.choice(open_joke_file("jokes.json"))[1]
    joke = {"text": joke.replace("\n","\n\n")}
    push_joke(joke, "yourhook")

