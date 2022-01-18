
from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()

@app.get('/')
def index():
    return {"data":{"name":"aditya"}}

class Test(BaseModel):
    name: str
    age: int
    gender: Optional[str] = None

@app.post('/modal')
def modal(request: Test):
    if request.age<10:
        return (f'Hi {request.name} you are not allowed in park because you are {request.age} year old only.')
    else:
        return (f'Hi {request.name} you are allowed in park as you are {request.age} years old.')
    # return request

@app.post('/blogs')
def blog():
    return {"data":"posting blog"}

@app.get('/greetings')
def greetings(name: Optional[str]= None):
    return(f'Hi How are you {name}')