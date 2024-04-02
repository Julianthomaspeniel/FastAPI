from sqlalchemy import Boolean, Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from database import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)
    created_by = Column(Integer, ForeignKey('users.id'))
    updated_by = Column(Integer, ForeignKey('users.id'))
    status = Column(Boolean, nullable=False, default=True)

    profile = relationship("Profile", back_populates="user", uselist=False, foreign_keys='Profile.user_id')
    addresses = relationship("Address", back_populates="user", foreign_keys='Address.user_id')

class Profile(Base):
    __tablename__ = "profiles"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    firstname = Column(String)
    lastname = Column(String)
    age = Column(Integer)
    dob = Column(String)
    phone_number = Column(Integer)
    created_by = Column(Integer, ForeignKey('users.id'))
    updated_by = Column(Integer, ForeignKey('users.id'))
    status = Column(Boolean, nullable=False, default=True)
   
    user_id = Column(Integer, ForeignKey('users.id')) 
    user = relationship("User", back_populates="profile",  foreign_keys='Profile.user_id')

class Address(Base):
    __tablename__ = "addresses"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    door_no = Column(String)
    street = Column(String)
    city = Column(String)
    state = Column(String)
    postal_code = Column(String)
    country = Column(String)
    address_type = Column(String)
    created_by = Column(Integer, ForeignKey('users.id'))
    updated_by = Column(Integer, ForeignKey('users.id'))
    status = Column(Boolean, nullable=False, default=True)

    user_id = Column(Integer, ForeignKey('users.id'))  
    user = relationship("User", back_populates="addresses",  foreign_keys='Address.user_id')
