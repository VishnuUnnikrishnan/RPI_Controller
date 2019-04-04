#Needs to be updated with error catching logic

import json

def readAttribute(module):
    with open("settings/settings.json", "r") as f:
        data = json.load(f)
        return data[module]



if __name__ == '__main__':
    pass