from typing import List
from fastapi import APIRouter, Depends, HTTPException, Response, status
from requests import Session
from sqlalchemy import select
from sqlalchemy.orm import Session
from passlib.context import CryptContext
import schemas, models, database, oauth2

router = APIRouter(
    prefix="/profile",
    tags=['Profile'])

get_db = database.get_db

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

@router.get('/', response_model=List[schemas.Profile])
def all_profile(db: Session = Depends(get_db)):
    get_all_profile = db.query(models.Profile).all()
    return get_all_profile

@router.get('/{id}', response_model=schemas.Profile)
def get_profile(id, response: Response, db: Session = Depends(get_db)):
    check_profile = db.query(models.Profile).filter(models.Profile.id== id).first()  
    if not all:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Profile with the id {id} is not available")
    return  check_profile

@router.post('/', response_model=schemas.Profile)
def create_profile(request: schemas.Profile, user_id:int, db: Session = Depends(get_db)):
    new_profile = models.Profile(firstname=request.firstname, lastname=request.lastname, dob=request.dob, age=request.age, phone_number=request.phone_number, created_by=user_id, user_id=user_id)
    db.add(new_profile)
    db.commit()
    db.refresh(new_profile)
    return new_profile

@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def update_profile(id: int, request: schemas.Profile, db: Session = Depends(get_db)):
    put_profile= db.query(models.Profile).filter(models.Profile.id == id).first()
    if put_profile is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"There is no profile with {id}")
    update_profile.firstname = request.firstname,
    update_profile.lastname = request.lastname
    update_profile.age = request.age
    update_profile.dob = request.dob
    update_profile.phone_number = request.phone_number
    db.commit()
    put_profile.updated_by = put_profile.id
    db.commit()
    return {'message': 'Profile details is updated successfully'}

@router.delete('/{id}', status_code= status.HTTP_204_NO_CONTENT)
def destroy(id, db: Session = Depends(get_db)):
    db.query(models.Profile).filter(models.Profile.id == id).delete(synchronize_session=False)
    db.commit()
    return 'deleted'

    

