import uuid
from fastapi import FastAPI, Body, status
from fastapi.responses import JSONResponse, FileResponse


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.id = str(uuid.uuid4()) # guid value


# Some kind of "data base" - just a Person objects
people = [Person("Alice", 38), Person("Bruce", 42), Person("Samir", 28)]


# Search user in "people" list
def find_person(id):
    for person in people:
        if person.id == id:
            return person
    return None


app = FastAPI()


@app.get("/")
async def main():
    return FileResponse("public/index.html")


@app.get("/api/users")
def get_people():
    return people


@app.get("/api/users/{id}")
def get_person(id):
    # Get user by ID
    person = find_person(id)
    print(person)
    # Error message if user not found
    if person == None:
        return JSONResponse(
            status_code=status.HTTP_404_NOT_FOUND,
            content={"message": "User not found"}
        )
    return person


@app.post("/api/users")
def create_person(data=Body()):
    person = Person(data["name"], data["age"])
    # Add an object to "people" list
    people.append(person)
    return person


@app.put("/api/users")
def edit_person(data=Body()):
    # Get user by ID
    person = find_person(data["id"])
    # Error message if user not found
    if person == None:
        return JSONResponse(
            status_code=status.HTTP_404_NOT_FOUND,
            content={"message": "User not found"}
        )
    # Change user's data
    person.age = data["age"]
    person.name = data["name"]
    return person


@app.delete("/api/users/{id}")
def delete_person(id):
    # Get user by ID
    person = find_person(id)
    # Error message if user not found
    if person == None:
        return JSONResponse(
            status_code=status.HTTP_404_NOT_FOUND,
            content={"message": "Пользователь не найден"}
        )

    # Remove user
    people.remove(person)
    return person
