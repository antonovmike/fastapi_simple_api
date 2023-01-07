from fastapi import FastAPI, Form
from fastapi.responses import FileResponse


app = FastAPI()


@app.get("/")
def root():
    return FileResponse("public/index.html")
 
 # Send form
# @app.post("/postdata")
# def postdata(username = Form(), userage=Form()):
    # return {"name": username, "age": userage}

# Send form + Validation
# @app.post("/postdata")
# def postdata(username: str = Form(min_length=2, max_length=9), userage: int = Form(ge=18, lt=111)):
    # return {"name": username, "age": userage}

# Default value
# @app.post("/postdata")
# def postdata(username: str = Form(default ="Undefined", min_length=2, max_length=9), userage: int = Form(default=18, ge=18, lt=111)):
    # return {"name": username, "age": userage}
    
# Send list
@app.post("/postdata")
def postdata(username: str = Form(), 
            languages: list =Form()):
    return {"name": username, "languages": languages}
