from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from time import time
from services.parser import embedding_css
import json


server = FastAPI()
server.mount("/frontend/static", StaticFiles(directory="frontend/static"), "frontend/static")
ACCOUNTS = {"Luca": "Hello World!"}

# get APIs for the browser to get the websites information
# ----------------------------------------------------------------------------
@server.get("/", response_class=HTMLResponse)
def root():
    return embedding_css("frontend/index.html", "frontend/css/format.css", "<link rel=\"stylesheet\" href=\"format.css\">")

# ----------------------------------------------------------------------------
@server.get("/training/", response_class=HTMLResponse)
def training():
    return embedding_css("frontend/training.html", "frontend/css/format.css", "<link rel=\"stylesheet\" href=\"format.css\">")

# ----------------------------------------------------------------------------
@server.get("/diet/", response_class=HTMLResponse)
def diet():
    return embedding_css("frontend/diet.html", "frontend/css/format.css", "<link rel=\"stylesheet\" href=\"format.css\">")

# ----------------------------------------------------------------------------
@server.get("/rest/", response_class=HTMLResponse)
def rest():
    return embedding_css("frontend/rest.html", "frontend/css/format.css", "<link rel=\"stylesheet\" href=\"format.css\">")

# ----------------------------------------------------------------------------



@server.get("/api_test", response_class=HTMLResponse)
def fapi(username: "str", password: "str"):
    if username in ACCOUNTS.keys():
        if ACCOUNTS[username] == password:
            pass
        else:
            raise HTTPException(status_code=404, detail="Invalid Password!")
    else:
        raise HTTPException(status_code=404, detail="Invalid Username!")

    content = ""
    with open("test.json", "r+") as file:
        data = json.loads(file.read())
        el = {"time" : time(), "name" : username}        
        data["items"].append(str(el))
        d = json.dumps(data, indent=4)
        content = d
    with open("test.json", "w"): pass
    with open("test.json", "w") as file:
        file.write(content)
    return rest()

# ----------------------------------------------------------------------------

@server.get("/get_data", response_class=HTMLResponse)
def data_getter(name: "str"):
    return "gg"
    



