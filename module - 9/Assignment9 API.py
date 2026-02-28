#Daniel Fryer
#Assignment 9
#2/28/2026

import requests
import json

def jprint(obj):
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

def main():
    response = requests.get("https://www.dnd5eapi.co/api/2014/")
    #print(response.json())
    jprint(response.json())


if __name__ == "__main__":
    main()