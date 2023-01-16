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

@router.get('/{username}/shoestorage',response_model=schemas.ShoesStorage, tags=['Shoe Storage'])
@limiter.limit("60/minute")
def get_shoe_storage(
    request:Request,
    username:str,
    currUser:schemas.User = Depends(auth.current_user),
    db: Session = Depends(interact_db)
    ):

    if currUser.superuser:
        return crud.get_shoe_storage(username=username, db=db)

    auth.check_if_currUser(currUser=currUser, username=username)
    return crud.get_shoe_storage(username=username, db=db)

@router.post('/{username}/shoestorage', response_model=List[schemas.ShoeCreation], tags=['Shoe Storage'])
@limiter.limit("30/minute")
def add_shoe(
    request:Request,
    username:str,
    shoe:schemas.ShoeQuantity,
    currUser:schemas.User = Depends(auth.current_user),
    db: Session = Depends(interact_db)):

    if currUser.superuser:
        return crud.add_shoe_to_storage(username=username, shoe=shoe, db=db)

    auth.check_if_currUser(currUser=currUser, username=username)
    return crud.add_shoe_to_storage(username=username, shoe=shoe, db=db)

@router.get("/{username}/shoestorage/{shoe_id}", response_model= schemas.ShoeCreation, tags=['Shoe Storage'])
@limiter.limit("60/minute")
def get_shoe_storage_item(
    request:Request,
    username:str,
    shoe_id:str,
    currUser:schemas.User = Depends(auth.current_user),
    db: Session = Depends(interact_db)):

    if currUser.superuser:
        return crud.get_shoe_item_by_id(username=username, shoe_id=shoe_id, db=db)

    auth.check_if_currUser(currUser=currUser,username=username)
    return crud.get_shoe_item_by_id(username=username, shoe_id=shoe_id, db=db)

@router.patch("/{username}/shoestorage/{shoe_id}", response_model= schemas.ShoeCreation, tags=['Shoe Storage'])
@limiter.limit("60/minute")
def update_shoe_by_id(
    request:Request,
    username:str, 
    shoe_id: str, 
    shoe: schemas.Shoe,
    currUser:schemas.User = Depends(auth.current_user),
    db:Session = Depends(interact_db)):

    if currUser.superuser:
        return crud.update_shoe_item(username=username,shoe_id=shoe_id, shoe=shoe, db=db)

    auth.check_if_currUser(currUser=currUser, username=username)
    return crud.update_shoe_item(username=username,shoe_id=shoe_id, shoe=shoe, db=db)

@router.delete('/{username}/shoestorage', response_model= schemas.ShoesStorage, tags=['Shoe Storage'])
@limiter.limit("60/minute")
def delete_shoe(
    request:Request,
    username:str, 
    shoe_id:Union[str,None]=None, 
    deleteAll: bool = False,
    currUser:schemas.User = Depends(auth.current_user),
    db:Session= Depends(interact_db)):

    if currUser.superuser:
        return crud.delete_item_by_shoeid(username=username, shoe_id=shoe_id, deleteAllFlag=deleteAll, db=db)

    auth.check_if_currUser(currUser=currUser, username=username)
    return crud.delete_item_by_shoeid(username=username, shoe_id=shoe_id, deleteAllFlag=deleteAll, db=db)