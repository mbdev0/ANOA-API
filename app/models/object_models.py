from sqlalchemy import Column, ForeignKey, Integer, String, JSON, Boolean
from sqlalchemy.orm import relationship
from configuration.dbconfig import Base

class User(Base):
    __tablename__ = 'users'

    userid = Column(String, primary_key = True, index=True)
    username = Column(String, unique = True, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)
    superuser = Column(Boolean, default= False)

    storage = relationship("Storage", backref = 'users',uselist=False, cascade = 'all,delete,delete-orphan')

class Storage(Base):
    __tablename__ = 'user_storage'

    storageId = Column(String, primary_key = True, index=True)
    userid = Column(String, ForeignKey("users.userid"))
    shoe_storage_space = Column(JSON)
    flips_storage_space = Column(JSON)
    amazon_storage_space = Column(JSON)
    nft_storage_space = Column(JSON)
