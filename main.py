from fastapi import FastAPI
from database import engine
import models,user, address, profiledetails, authentication
app = FastAPI()

models.Base.metadata.create_all(engine)

app.include_router(user.router)
app.include_router(address.router)
app.include_router(profiledetails.router)
app.include_router(authentication.router)