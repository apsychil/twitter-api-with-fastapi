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


# Path Operations

## Users

### Registrar el usuario
@app.post(
    "/signup",
    response_model=User,
    status_code=status.HTTP_201_CREATED,
    tags=["Users"],
    summary="Register a User"
)
def signup():
    pass

### Login el usuario
@app.post(
    "/login",
    response_model=User,
    status_code=status.HTTP_200_OK,
    tags=["Users"],
    summary="Login a User"
)
def login():
    pass

### Muestra todos los usuarios
@app.get(
    "/users",
    response_model=List[User],
    status_code=status.HTTP_200_OK,
    tags=["Users"],
    summary="Show all Users"
)
def show_all_users():
    pass

### Muestra un usuario
@app.get(
    "/users/{user_id}",
    response_model=User,
    status_code=status.HTTP_200_OK,
    tags=["Users"],
    summary="Show a Users"
)
def show_a_user():
    pass

### Borra un usuario
@app.delete(
    "/users/{user_id}/delete",
    response_model=User,
    status_code=status.HTTP_200_OK,
    tags=["Users"],
    summary="Delete a User"
)
def delete_a_user():
    pass

### Actualiza un usuario
@app.put(
    "/users/{user_id}/update",
    response_model=User,
    status_code=status.HTTP_200_OK,
    tags=["Users"],
    summary="Update a User"
)
def update_a_user():
    pass


## Tweets

### Show all tweets
@app.get(
    "/",
    response_model=List[Tweet], 
    status_code=status.HTTP_200_OK,
    tags=["Tweets"],
    summary="Show all tweets")
def home():
    return {"api":"twitter"}

### Show a tweet
@app.get(
    "/tweets/{tweet_id}",
    response_model=Tweet, 
    status_code=status.HTTP_200_OK,
    tags=["Tweets"],
    summary="Show a tweet")
def show_a_tweet():
    pass

### Post a tweet
@app.post(
    "/post",
    response_model=Tweet, 
    status_code=status.HTTP_201_CREATED,
    tags=["Tweets"],
    summary="Post a tweet")
def post_a_tweet():
    pass

### Delete a tweet
@app.delete(
    "/tweets/{tweet_id}/delete",
    response_model=Tweet, 
    status_code=status.HTTP_200_OK,
    tags=["Tweets"],
    summary="Delete a tweet")
def delete_a_tweet():
    pass

### Update a tweet
@app.put(
    "/tweets/{tweet_id}/update",
    response_model=Tweet, 
    status_code=status.HTTP_200_OK,
    tags=["Tweets"],
    summary="Update a tweet")
def update_a_tweet():
    pass

#Main

if __name__ == "__main__":
    uvicorn.run(
        "__main__:app",
        host="localhost",
        port=8000,
        reload=True,
        workers=2
    )