from pydantic import BaseModel, conint, confloat, EmailStr
from typing import Union, Optional, Literal, List, TypedDict
from uuid import UUID

class Token(BaseModel):
    access_token:str
    token_type:str

class TokenData(BaseModel):
    username:Union[str,None] = None
    
class UserBase(BaseModel):
    username: Union[str, None] = None
    email: Union[EmailStr, None] = None
  
class UserCreation(UserBase):
    password:Union[str, None] = None

    class Config:
        orm_mode=True
            
class User(UserBase):
    userid: UUID

    class Config:
        orm_mode=True

class Flips(BaseModel):
    brand: Optional[str]
    model: Optional[str]
    #quantity: Optional[conint(gt=0)]
    retail: Optional[confloat(gt=0)]
    status: Optional[Literal['NOT LISTED', 'LISTED', 'PACKED', 'SHIPPED']]
    resell: Optional[confloat(ge=0)]

class FlipsCreation(Flips):
    id:UUID

class FlipsQuantity(Flips):
    quantity: conint(gt=0)

class Shoe(Flips):
    colorway: Optional[str]
    size: Optional[confloat(gt=0)]
    Sku: Optional[str]

class ShoeCreation(Shoe):
    id:UUID

class ShoeQuantity(Shoe):
    quantity: conint(gt=0)

class StorageBase(BaseModel):
    shoe_storage_space = {"Shoes":[], "Stats": {
            "total_retail":0, "total_resell":0, "current_net": 0, "total_quantity":0, "amount_not_listed":0, "amount_listed":0,
            "amount_packed":0,"amount_shipped":0
            }
        }
    flips_storage_space =  {"Flips":[], "Stats": {
            "total_retail":0, "total_resell":0, "current_net": 0, "total_quantity":0, "amount_not_listed":0, "amount_listed":0,
            "amount_packed":0,"amount_shipped":0
            }
        }

class Storage(StorageBase):
    storageId:UUID
    userid:UUID

    class Config:
        orm_mode=True

class Stats(BaseModel):
    Stats: TypedDict('Stats',{"total_retail":int, "total_resell":int, "current_net": int, "total_quantity":int, "amount_not_listed":int, "amount_listed":int,
            "amount_packed":int,"amount_shipped":int})

class FlipsStorage(Stats):
    Flips:List[FlipsCreation]

class ShoesStorage(Stats):
    Shoes:List[ShoeCreation]

