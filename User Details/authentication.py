from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
import models, database,schemas
from sqlalchemy.orm import Session
from passlib.context import CryptContext
import tokens

router = APIRouter(prefix="/login", tags=['authentication'])

get_db = database.get_db

@router.post('/')
def login(request: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
    
    user = db.query(models.User).filter(models.User.email == request.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Invalid Credentials")

    if not pwd_context.verify(request.password, user.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Incorrect Password")
    access_tokens = tokens.create_access_token(data={"sub": user.email})
    return {"access_tokens" : access_tokens, "tokens_type":"bearer"}

# def user_login(request:OAuth2PasswordRequestForm=Depends(),db:Session=Depends(get_db)):
#     user=db.query(models.User).filter(models.User.email_id==request.username).first()
     
#     if not user:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Invalid Credentials")
#     if not passwordHashing.verify_password(request.password,user.password):
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Invalid Credentials")
    
#     access_token = token.create_access_token(
#         data={"sub": user.email_id} 
#     )
#     return {"email_id":user.email_id,"access_token":access_token, "token_type":"bearer"}