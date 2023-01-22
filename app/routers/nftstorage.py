from configuration.dbconfig import interact_db
from configuration.limiter import *
from auth import auth
from schemas import schemas
from operations import crud

from typing import Union, List
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends
from starlette.requests import Request
from pydantic import validate_model


router = APIRouter()

@router.get('/{username}/nftstorage', response_model = schemas.NFTStorage, tags=['NFT Storage'])
@limiter.limit("60/minute")
def Get_NFT_Storage(
    request:Request,
    username:str,
    currUser:schemas.User = Depends(auth.current_user),
    db: Session = Depends(interact_db)):

    print(currUser)
    if currUser.superuser:
        return crud.get_nft_storage(username=username, db=db)

    auth.check_if_currUser(currUser=currUser, username=username)

    return crud.get_nft_storage(username=username, db=db) 

@router.post('/{username}/nftstorage', response_model=schemas.NFT, tags=['NFT Storage'])
@limiter.limit("30/minute")
def Add_NFT(
    request:Request,
    username:str, 
    nft:schemas.NFT,
    currUser:schemas.User = Depends(auth.current_user),
    db: Session = Depends(interact_db)):

    if currUser.superuser:
        return crud.add_nft_to_storage(username=username, nft=nft, db=db)

    auth.check_if_currUser(currUser=currUser,username=username)
    return crud.add_nft_to_storage(username=username, nft=nft, db=db)

@router.get("/{username}/nftstorage/{item_id}", response_model = schemas.NFT, tags= ['NFT Storage'])
@limiter.limit("60/minute")
def Get_NFT_Storage_Item(
    request:Request,
    username:str,
    id:str, 
    currUser:schemas.User = Depends(auth.current_user),
    db: Session = Depends(interact_db)):

    if currUser.superuser:
        return crud.get_nft_item_by_id(username=username,nft_id=id,db=db)

    auth.check_if_currUser(currUser=currUser, username=username)
    return crud.get_nft_item_by_id(username=username,nft_id=id,db=db)


@router.patch("/{username}/nftstorage/{item_id}", response_model = schemas.NFT, tags= ['NFT Storage'])
@limiter.limit("60/minute")
def Update_NFT_Storage_Item(
    request:Request,
    username:str,
    id:str,
    nft:schemas.NFT,
    currUser:schemas.User = Depends(auth.current_user),
    db: Session = Depends(interact_db)):

    if currUser.superuser:
        return crud.update_nft_item(username=username,nft_id=id,nft=nft,db=db)

    auth.check_if_currUser(currUser=currUser, username=username)
    return crud.update_nft_item(username=username,nft_id=id,nft=nft,db=db)

@router.delete("/{username}/nftstorage/{item_id}", response_model = schemas.NFTStorage, tags= ['NFT Storage'])
@limiter.limit("60/minute")
def Delete_NFT_Storage_Item(
    request:Request,
    username:str,
    id:str,
    deleteAll:bool = False, 
    currUser:schemas.User = Depends(auth.current_user),
    db: Session = Depends(interact_db)):

    if currUser.superuser:
        return crud.delete_item_by_nftid(username=username,nft_id=id,db=db)

    auth.check_if_currUser(currUser=currUser, username=username)
    return crud.delete_item_by_nftid(username=username,nft_id=id,deleteAllFlag=deleteAll,db=db)