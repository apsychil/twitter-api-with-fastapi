#Python
import json
from uuid import UUID
from datetime import date
from datetime import datetime
from typing import Optional, List

#Uvicorn
import uvicorn

#FastAPI
from fastapi import FastAPI
from fastapi import status
from fastapi import Body

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
    birth_date: Optional[date] = Field(default=None)  
    
class UserRegister(User):
    password: str = Field(
        ...,
        min_length=8,
        max_length=64
    )
     
class Tweet(BaseModel):
    tweet_id: UUID = Field(...)
    content: str = Field(
        ...,
        min_length=1,
        max_length=256
    )
    created_at: datetime = Field(default=datetime.now())
    updated_at: Optional[datetime] = Field(default=None)
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
def signup(user: UserRegister = Body(...)):
    """
    Sign Up a User:
    
    This path operation registers a user in the app.
    
    Parameters:
        -Request body parameter
            - user: UserRegister
            
    Returns: A JSON with the basic user information:
        - user_id: UUID
        - email: EmailStr
        - first_name: str
        - last_name: str
        - birth_date: str
    """
    with open("users.json", "r+", encoding="utf-8") as f:
        results = json.loads(f.read())
        user_dict = user.dict()
        user_dict["user_id"] = str(user_dict["user_id"])
        user_dict["birth_date"] = str(user_dict["birth_date"])
        results.append(user_dict)
        f.seek(0)
        f.write(json.dumps(results))
        return user
        

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
    """This path operation shows all users in the app

    Returns:
        JSON: JSON list with all users in the app, with the following keys:
            - user_id: UUID
            - email: EmailStr
            - first_name: str
            - last_name: str
            - birth_date: str 
    """
    with open("users.json", "r", encoding="utf-8") as f:
        results = json.loads(f.read())
        return results
    
    
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
    return {"API de Twitter":"Funciona!"}

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
def post_a_tweet(tweet: Tweet = Body(...)):
    """This path operation post a tweet in the app

    Args:
        tweet (Tweet): content of the tweet in str.

    Returns:
        json: json list with the basic tweet information, with the following keys:
            - tweet_id: UUID
            - content: str
            - created_at: datetime
            - updated_at: Optional[datetime]
            - by: User
    """
    with open("tweets.json", "r+", encoding="utf-8") as f:
        results = json.loads(f.read())
        tweet_dict = tweet.dict()
        tweet_dict["tweet_id"] = str(tweet_dict["tweet_id"])
        tweet_dict["created_at"] = str(tweet_dict["created_at"])
        tweet_dict["updated_at"] = str(tweet_dict["updated_at"])
        tweet_dict["by"]["user_id"] = str(tweet_dict["by"]["user_id"]) 
        tweet_dict["by"]["birth_date"] = str(tweet_dict["by"]["birth_date"])
        
        results.append(tweet_dict)
        f.seek(0)
        f.write(json.dumps(results))
        return tweet

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

#Main para que se ejecute el servidor de uvicorn

if __name__ == "__main__":
    uvicorn.run(
        "__main__:app",
        host="localhost",
        port=8000,
        reload=True,
        workers=2
    )