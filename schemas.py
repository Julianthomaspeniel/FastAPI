from typing import List, Optional
from pydantic import BaseModel


class User(BaseModel):
    username: str
    email: str
    password: str

class Profile(BaseModel):
    firstname: str
    lastname: str
    age: int
    dob: str
    phone_number: int

class Address(BaseModel):
    door_no: str
    street: str
    city: str
    state: str
    postal_code: str
    country: str
    address_type: str
 
class Login(BaseModel):
    username: str
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    email: Optional[str] = None