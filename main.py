#Python
from uuid import UUID
from datetime import date
from datetime import datetime
from typing import Optional, List

#Uvicorn
import uvicorn

#FastAPI
from fastapi import FastAPI
from fastapi import status

#Pydantic
from pydantic import BaseModel
from pydantic import EmailStr
from pydantic import Field



app = FastAPI()

#Models

class UserBase(BaseModel):
    user_id: UUID = Field(...) #Universal Unit Identifier. Es una clase especial de Python que permite permite ponerle un identificador único a cada usuario cada vez que nosotros queramos en a app.permite ponerle un identificador único a cada usuario cada vez que nosotros queramos en a app.
    email: EmailStr = Field(...)

class UserLogin(UserBase):
    password: str = Field(
        ...,
        min_length=8,
        max_length=64
    )

class User(UserBase):
    first_name: str = Field(
        ...,
        min_length=1,
        max_length=50
    )
    last_name: str = Field(
        ...,
        min_length=1,
        max_length=50
    )
    birthday: Optional[date] = Field(default=None)  
     
class Tweet(BaseModel):
    tweet_id: UUID = Field(...)
    content: str = Field(
        ...,
        min_length=1,
        max_length=256
    )
    created_at: date = Field(default=datetime.now())
    update_at: Optional[date] = Field(default=None)
    by: User = Field(...)


#Path Operations

@app.get(
    "/", 
    status_code=status.HTTP_200_OK,
    tags=["Home"],
    summary="Home")
def home():
    """_summary_

    Returns:
        _type_: _description_
    """
    return {"api":"twitter"}

##Users

@app.post(
    "/signup",
    response_model=User,
    status_code=status.HTTP_201_CREATED,
    tags=["Users"],
    summary="Register a User"
)
def signup():
    pass

@app.post(
    "/login",
    response_model=User,
    status_code=status.HTTP_200_OK,
    tags=["Users"],
    summary="Login a User"
)
def login():
    pass

@app.get(
    "/users",
    response_model=List[User],
    status_code=status.HTTP_200_OK,
    tags=["Users"],
    summary="Show all Users"
)
def show_all_users():
    pass

@app.get(
    "/users/{user_id}",
    response_model=User,
    status_code=status.HTTP_200_OK,
    tags=["Users"],
    summary="Show a Users"
)
def show_a_user():
    pass

@app.delete(
    "/users/{user_id}/delete",
    response_model=User,
    status_code=status.HTTP_200_OK,
    tags=["Users"],
    summary="Delete a User"
)
def delete_a_user():
    pass

@app.put(
    "/users/{user_id}/update",
    response_model=User,
    status_code=status.HTTP_200_OK,
    tags=["Users"],
    summary="Update a User"
)
def update_a_user():
    pass

##Tweets



if __name__ == "__main__":
    uvicorn.run(
        "__main__:app",
        host="localhost",
        port=8000,
        reload=True,
        workers=2
    )