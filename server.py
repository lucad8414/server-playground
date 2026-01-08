from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from time import time
from parser import embedding_css
import json


server = FastAPI()


# get APIs for the browser to get the websites information
# ----------------------------------------------------------------------------
@server.get("/", response_class=HTMLResponse)
def root():
    return embedding_css("index.html", "format.css", "<link rel=\"stylesheet\" href=\"format.css\">")

# ----------------------------------------------------------------------------
@server.get("/training/", response_class=HTMLResponse)
def training():
    return embedding_css("training.html", "format.css", "<link rel=\"stylesheet\" href=\"format.css\">")

# ----------------------------------------------------------------------------
@server.get("/diet/", response_class=HTMLResponse)
def training():
    return embedding_css("diet.html", "format.css", "<link rel=\"stylesheet\" href=\"format.css\">")

# ----------------------------------------------------------------------------
@server.get("/rest/", response_class=HTMLResponse)
def training():
    return embedding_css("rest.html", "format.css", "<link rel=\"stylesheet\" href=\"format.css\">")

# ----------------------------------------------------------------------------

@server.get("/api_test/")
def fapi(name: "str"):
    content = ""
    with open("test.json", "r+") as file:
        data = json.loads(file.read())
        el = {"time" : time(), "name" : name}        
        data["items"].append(str(el))
        d = json.dumps(data, indent=4)
        content = d
    with open("test.json", "w"): pass
    with open("test.json", "w") as file:
        file.write(content)
    return "Succesfull"



