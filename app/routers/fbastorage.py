from configuration.dbconfig import interact_db
from configuration.limiter import *
from auth import auth
from schemas import schemas
from operations import crud

from typing import Union, List
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends
from starlette.requests import Request

router = APIRouter()

@router.get('/{username}/fbastorage',response_model=schemas.FBAStorage, tags=['FBA Storage'])
@limiter.limit("60/minute")
def get_fba_storage(
    request:Request,
    username:str,
    currUser:schemas.User = Depends(auth.current_user),
    db: Session = Depends(interact_db)):

    print(currUser)
    if currUser.superuser:
        return crud.get_amazon_storage(username=username, db=db)

    auth.check_if_currUser(currUser=currUser, username=username)
    return crud.get_amazon_storage(username=username, db=db)

@router.post('/{username}/fbastorage', response_model=schemas.FBAItem, tags=['FBA Storage'])
@limiter.limit("30/minute")
def add_fba(
    request:Request,
    username:str, 
    fba:schemas.FBAItem,
    currUser:schemas.User = Depends(auth.current_user),
    db: Session = Depends(interact_db)):

    if currUser.superuser:
        return crud.add_amazon_to_storage(username=username, fba=fba, db=db)

    auth.check_if_currUser(currUser=currUser,username=username)
    return crud.add_amazon_to_storage(username=username, fba=fba, db=db)

@router.get("/{username}/fbastorage/{item_id}", response_model = schemas.FBAItem, tags= ['FBA Storage'])
@limiter.limit("60/minute")
def get_fba_storage_item(
    request:Request,
    username:str,
    asin:str, 
    currUser:schemas.User = Depends(auth.current_user),
    db: Session = Depends(interact_db)):

    if currUser.superuser:
        return crud.get_amazon_item_by_asin(username=username,asin=asin,db=db)

    auth.check_if_currUser(currUser=currUser, username=username)
    return crud.get_amazon_item_by_asin(username=username,asin=asin,db=db)

@router.patch("/{username}/fbastorage/{item_id}", response_model = schemas.FBAItem, tags= ['FBA Storage'])
@limiter.limit("30/minute")
def update_fba_storage_item(
    request:Request,
    username:str,
    asin:str, 
    fba:schemas.FBAItem,
    currUser:schemas.User = Depends(auth.current_user),
    db: Session = Depends(interact_db)):

    if currUser.superuser:
        return crud.update_amazon_item(username=username,asin=asin,fba=fba,db=db)

    auth.check_if_currUser(currUser=currUser, username=username)
    return crud.update_amazon_item(username=username,asin=asin,fba=fba,db=db)

@router.delete("/{username}/fbastorage/{item_id}", response_model = schemas.FBAStorage, tags= ['FBA Storage'])
@limiter.limit("30/minute")
def delete_fba_storage_item(
    request:Request,
    username:str,
    asin:Union[str,None] = None,
    deleteAll:bool = False,
    currUser:schemas.User = Depends(auth.current_user),
    db: Session = Depends(interact_db)):

    if currUser.superuser:
        return crud.delete_item_by_asin(username=username,asin=asin,deleteAllFlag=deleteAll,db=db)

    auth.check_if_currUser(currUser=currUser, username=username)
    return crud.delete_item_by_asin(username=username,asin=asin,deleteAllFlag=deleteAll,db=db)
