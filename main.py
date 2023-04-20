#Python
from uuid import UUID
from datetime import date
from typing import Optional

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
        min_length=8
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
    pass




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



if __name__ == "__main__":
    uvicorn.run(
        "__main__:app",
        host="localhost",
        port=8000,
        reload=True,
        workers=2
    )