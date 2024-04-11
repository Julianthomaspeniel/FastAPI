from typing import List
from fastapi import APIRouter, Depends, HTTPException, Response, status
from requests import Session
from sqlalchemy import select
from sqlalchemy.orm import Session
from passlib.context import CryptContext
import schemas, models, database, oauth2


router = APIRouter(
    prefix="/address",
    tags=['Address'])

get_db = database.get_db

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

@router.get('/', response_model=List[schemas.Address])
def all_address(db: Session = Depends(get_db)):
    address = db.query(models.Address).all()
    return address

@router.get('/{id}', response_model=schemas.Address)
def get_address(id, response: Response, db: Session = Depends(get_db)):
    check_address = db.query(models.Address).filter(models.Address.id== id).first()  
    if not check_address:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Address with the id {id} is not available")
    return  check_address

@router.post('/', response_model=schemas.Address)
def create_address(request: schemas.Address,user_id: int,  db: Session = Depends(get_db)):
    new_address = models.Address(door_no=request.door_no, street= request.street,city= request.city, state= request.state, country= request.country, postal_code= request.postal_code, address_type= request.address_type, created_by = user_id)
    db.commit()
    db.add(new_address)
    db.commit()
    db.refresh(new_address)
    return new_address

@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def update_address(id: int, request: schemas.ShowAddress, db: Session = Depends(get_db)):
    put_adress= db.query(models.Address).filter(models.Address.id == id).first()
    if put_adress is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"There is no adress with {id}")
    update_address.door_no, = request.door_no
    update_address.street = request.street
    update_address.city = request.city
    update_address.state = request.state
    update_address.country = request.country
    update_address.postal_code = request.postal_code
    update_address.address_type = request.address_type
    db.commit()
    put_adress.updated_by = put_adress.id
    db.commit()
    return {'city': 'address details is updated successfully'}

@router.delete('/{id}', status_code= status.HTTP_204_NO_CONTENT)
def destroy(id, db: Session = Depends(get_db)):
    db.query(models.Address).filter(models.Address.id == id).delete(synchronize_session=False)
    db.commit()
    return 'deleted'

    

