from typing import List, Optional
from pydantic import BaseModel

class User(BaseModel):
    username: str
    email: str
    password: str

class ShowUser(BaseModel):
    username: Optional[str] = None
    email: Optional[str] = None
    password: Optional[str] = None

class Profile(BaseModel):
    firstname: str
    lastname: str
    age: int
    dob: str
    phone_number: int

class ShowProfile(BaseModel):
    firstname: Optional[str] = None
    lastname: Optional[str] = None
    age: Optional[int] = None
    dob: Optional[str] = None
    phone_number: Optional[int] = None

class Address(BaseModel):
    door_no: str
    street: str
    city: str
    state: str
    postal_code: str
    country: str
    address_type: str

class ShowAddress(BaseModel):
    door_no: Optional[str] = None
    street: Optional[str] = None
    city: Optional[str] = None
    state: Optional[str] = None
    postal_code: Optional[str] = None
    country: Optional[str] = None
    address_type: Optional[str] = None
 
class Login(BaseModel):
    username: str
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    email: Optional[str] = None