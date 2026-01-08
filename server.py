from fastapi import FastAPI
from time import time
import json


server = FastAPI()

@server.get("/")
def root():
    return {"Item": "Hello World!"}



@server.get("/api_test/")
def fapi(name: "str"):
    content = ""
    with open("test.json", "r+") as file:
        data = json.loads(file.read())
        el = {"time" : time(), "name" : name}        
        data["items"].append(str(el))
        print(data)
        d = json.dumps(data, indent=4)
        content = d
    with open("test.json", "w"): pass
    with open("test.json", "w") as file:
        file.write(content)
    return "Succesfull"



