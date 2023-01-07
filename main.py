from fastapi import FastAPI, Response
from datetime import datetime

app = FastAPI()

@app.get("/")
def root(response: Response):
    now = datetime.now() # Get current Date and Time
    response.set_cookie(key="last_visit", value=now)
    return {"message": "cookie are set"}
