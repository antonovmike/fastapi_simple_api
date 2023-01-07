from fastapi import FastAPI, Cookie
from fastapi.responses import JSONResponse
from datetime import datetime

app = FastAPI()

# Cookies as a Parameter
# @app.get("/")
# def root(response: Response):
    # now = datetime.now() # Get current Date and Time
    # response.set_cookie(key="last_visit", value=now)
    # return {"message": "Cookies are set"}


# Cookies as an Object
# @app.get("/")
# def root():
    # now = datetime.now() # Get current Date and Time
    # response = JSONResponse(content={"message": "Cookies are set"})
    # response.set_cookie(key="last_visit", value=now)
    # return response


# Get existing cookie
@app.get("/")
def root(last_visit = Cookie()):
    return  {"last visit": last_visit}
