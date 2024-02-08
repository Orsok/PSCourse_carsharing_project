from datetime import datetime

import uvicorn
from fastapi import FastAPI, HTTPException

app = FastAPI()

db = [  # my car database
    {"id": 1, "size": "s", "fuel": "gasoline", "doors": 3, "transmission": "auto"},
    {"id": 2, "size": "s", "fuel": "electric", "doors": 3, "transmission": "auto"},
    {"id": 3, "size": "s", "fuel": "gasoline", "doors": 5, "transmission": "manual"},
    {"id": 4, "size": "m", "fuel": "electric", "doors": 3, "transmission": "auto"},
    {"id": 5, "size": "m", "fuel": "hybrid", "doors": 5, "transmission": "auto"},
    {"id": 6, "size": "m", "fuel": "gasoline", "doors": 5, "transmission": "manual"},
    {"id": 7, "size": "l", "fuel": "diesel", "doors": 5, "transmission": "manual"},
    {"id": 8, "size": "l", "fuel": "electric", "doors": 5, "transmission": "auto"},
    {"id": 9, "size": "l", "fuel": "hybrid", "doors": 5, "transmission": "auto"}
]

# Exercise
# Please add an operation called get_cars(
# That is served at /api/cars
# And that returns all car data
#


@app.get("/")  # @app.get = decorator | ("/") = Path Operator
def welcome(name):  # (def) = function definition | (welcome) = function name | (name) = path parameter
    """Return a friendly welcome message."""
    return {"message": f"Welcome {name}, to the Car Sharing service!"}


@app.get("/date")
def date():
    """Return date"""
    return {"date": datetime.now()}


@app.get("/api/cars")
def get_cars(size: str|None = None, doors: int|None = None) -> list:  # (size: str|None = None) = "size should be string
                                                                      # OR none with a default value of none"
    """Return cars."""
    result = db
    if size:
        result = [car for car in result if car['size'] == size]
    if doors:
        result = [car for car in result if car['doors'] >= doors]
    return result


@app.get("/api/cars/{id}")
def cr_by_id(id: int|None = None) -> dict:
    """Return car by ID."""
    result = [car for car in db if car['id'] == id]
    if result:
        return result[0]
    else:
        raise HTTPException(status_code=404, detail=f"No car with this ID was found! ID={id}")


if __name__ == "__main__":
    uvicorn.run("carsharing:app", reload=True)