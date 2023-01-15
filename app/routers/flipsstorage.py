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

@router.get('/{username}/flipsstorage',response_model=schemas.FlipsStorage, tags=['Flips Storage'])
@limiter.limit("60/minute")
def get_flips_storage(
    request:Request,
    username:str,
    currUser:schemas.User = Depends(auth.current_user),
    db: Session = Depends(interact_db)):

    print(currUser)
    if currUser.superuser:
        return crud.get_flips_storage(username=username, db=db)

    auth.check_if_currUser(currUser=currUser, username=username)
    return crud.get_flips_storage(username=username, db=db)



@router.post('/{username}/flipsstorage', response_model=List[schemas.FlipsCreation], tags=['Flips Storage'])
@limiter.limit("30/minute")
def add_flip(
    request:Request,
    username:str, 
    flip:schemas.Flips,
    currUser:schemas.User = Depends(auth.current_user),
    db: Session = Depends(interact_db)):

    if currUser.superuser:
        return crud.add_flips_to_storage(username=username, item=flip, db=db)

    auth.check_if_currUser(currUser=currUser,username=username)
    return crud.add_flips_to_storage(username=username, item=flip, db=db)

@router.get("/{username}/flipstorage/{item_id}", response_model = schemas.FlipsCreation, tags= ['Flips Storage'])
@limiter.limit("60/minute")
def get_flips_storage_item(
    request:Request,
    username:str,
    item_id:str, 
    currUser:schemas.User = Depends(auth.current_user),
    db: Session = Depends(interact_db)):

    if currUser.superuser:
        return crud.get_flip_item_by_id(username=username,item_id=item_id,db=db)

    auth.check_if_currUser(currUser=currUser, username=username)
    return crud.get_flip_item_by_id(username=username,item_id=item_id,db=db)



@router.patch("/{username}/flipsstorage/{item_id}", response_model=schemas.FlipsCreation, tags=['Flips Storage'])
@limiter.limit("60/minute")
def update_item_by_id(
    request:Request,
    username:str, 
    item_id:str, 
    item_updating:schemas.Flips,
    currUser:schemas.User = Depends(auth.current_user),
    db:Session = Depends(interact_db)):

    if currUser.superuser:
        return crud.update_flip_item(username=username,item_id=item_id, item=item_updating, db=db)

    auth.check_if_currUser(currUser=currUser, username=username)
    return crud.update_flip_item(username=username,item_id=item_id, item=item_updating, db=db)


    
@router.delete('/{username}/flipsstorage',response_model=schemas.FlipsStorage, tags=['Flips Storage'])
@limiter.limit("60/minute")
def delete_flip(
    request:Request,
    username:str, 
    item_id:Union[str,None]=None, 
    deleteAll: bool = False,
    currUser:schemas.User = Depends(auth.current_user),
    db:Session= Depends(interact_db)):

    if currUser.superuser:
        return crud.delete_item_by_itemid(username=username, item_id=item_id, deleteAllFlag=deleteAll,db=db)

    auth.check_if_currUser(currUser=currUser, username=username)
    return crud.delete_item_by_itemid(username=username, item_id=item_id, deleteAllFlag=deleteAll,db=db)



