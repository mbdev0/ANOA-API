from models import object_models
from configuration.dbconfig import engine, interact_db
from schemas import schemas
from auth import auth, authconfig
from routers import flipsstorage, shoestorage, users, nftstorage, fbastorage
from configuration.limiter import *

from datetime import timedelta
from fastapi import Depends, FastAPI, HTTPException
from fastapi.responses import RedirectResponse
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from starlette.requests import Request

object_models.Base.metadata.create_all(bind=engine)

app.include_router(flipsstorage.router)
app.include_router(shoestorage.router)
app.include_router(users.router)
app.include_router(nftstorage.router)
app.include_router(fbastorage.router)

@app.get("/")
@limiter.limit("30/minute")
def response(request:Request):
    return RedirectResponse("/docs")

@app.post("/token", response_model=schemas.Token, tags=['Token'])
def login(formdata: OAuth2PasswordRequestForm = Depends(), db:Session = Depends(interact_db)):
    user = auth.validate_user(formdata=formdata, db=db)
    if not user:
        raise HTTPException(
            status_code=401,
            detail='Invalid Credentials',
            headers= {'WWW-Authentication':'Bearer'}
        )
    access_token = auth.create_acess_token({'sub':user.username},expiry_delta=timedelta(minutes=authconfig.ACCESS_TOKEN_EXPIRY_MINS))
    return schemas.Token(access_token=access_token,token_type='Bearer')


