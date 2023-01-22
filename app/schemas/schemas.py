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

class FBAItem(BaseModel):
    asin: Optional[str]
    title: Optional[str]
    brand: Optional[str]
    dimensions:Optional[str]
    weight:Optional[float]
    retail:Optional[confloat(gt=0)]
    resell:Optional[confloat(ge=0)]
    quantity:Optional[conint(gt=0)]
    category:Optional[str]
    status:Optional[Literal['NOT LISTED', 'LISTED', 'PACKED', 'SHIPPED']]

class NFT(BaseModel):
    id : Optional[str]
    name: Optional[str]
    retail: Optional[confloat(gt=0)]
    resell: Optional[confloat(ge=0)]
    metadata: Optional[dict]
    owner_address: Optional[str]
    status: Optional[Literal['NOT LISTED', 'LISTED', 'SOLD']]

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
    fba_storage_space = {"FBA":[], "Stats": {
            "total_retail":0, "total_resell":0, "current_net": 0, "total_quantity":0, "amount_not_listed":0, "amount_listed":0,
            "amount_packed":0,"amount_shipped":0
            }
        }
    nft_storage_space = {"NFT":[], "Stats": {
            "total_retail":0, "total_resell":0, "current_net": 0, "total_quantity":0, "amount_not_listed":0, "amount_listed":0,
            "amount_sold":0
            }
        }

class Storage(StorageBase):
    storageId:UUID
    userid:UUID

    class Config:
        orm_mode=True

class Stats(BaseModel):
    total_retail:conint(ge=0)
    total_resell:conint(ge=0)
    current_net:conint(ge=0)
    total_quantity:conint(ge=0)
    amount_not_listed:conint(ge=0)
    amount_listed:conint(ge=0)
    amount_packed:conint(ge=0)
    amount_shipped:conint(ge=0)


class FlipsStorage(BaseModel):
    Flips:List[FlipsCreation]
    Stats: Stats
class ShoesStorage(BaseModel):
    Shoes:List[ShoeCreation]
    Stats: Stats

class FBAStorage(BaseModel):
    FBA:List[FBAItem]
    Stats: Stats

class NFTStats(BaseModel):
    total_retail:conint(ge=0)
    total_resell:conint(ge=0)
    current_net:conint(ge=0)
    total_quantity:conint(ge=0)
    amount_not_listed:conint(ge=0)
    amount_listed:conint(ge=0)
    amount_sold:conint(ge=0)

class NFTStorage(BaseModel):
    NFT:List[NFT]
    Stats: NFTStats

