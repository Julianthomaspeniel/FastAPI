from typing import List
from fastapi import APIRouter, Depends, HTTPException, Response, status, Header
from requests import Session
from sqlalchemy.orm import Session
from passlib.context import CryptContext
import schemas, models, database

router = APIRouter(
    prefix="/user",
    tags=['Users'])

get_db = database.get_db

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

    
@router.get('/', response_model=List[schemas.User])
def get_all_user(db: Session = Depends(get_db)):
    all_users = db.query(models.User).all()
    return all_users

@router.get('/{id}', response_model=schemas.User)
def get_user(id, response: Response, db: Session = Depends(get_db)):
    check_user = db.query(models.User).filter(models.User.id== id).first()  
    if not check_user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with the id {id} is not available")
    return  check_user

@router.post('/', response_model=schemas.User)
def create_user(request: schemas.User, db: Session = Depends(get_db)):
    hashedPassword = pwd_context.hash(request.password)
    new_user = models.User(username=request.username,email= request.email, password=hashedPassword) 
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    new_user.created_by = new_user.id
    db.commit()
    return(new_user)

@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def update_user(id: int, request: schemas.User, db: Session = Depends(get_db)):
    put_user= db.query(models.User).filter(models.User.id == id).first()
    if put_user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"There is no user with {id}")
    update_user.username = request.username
    update_user.password = request.password
    update_user.email = request.email
    db.commit()
    put_user.updated_by = put_user.id
    db.commit()
    return {'message': 'User details is updated successfully'}

@router.delete('/{id}', status_code= status.HTTP_204_NO_CONTENT)
def destroy(id, db: Session = Depends(get_db)):
    db.query(models.User).filter(models.User.id == id).delete(synchronize_session=False)
    db.commit()
    return 'deleted'

    

