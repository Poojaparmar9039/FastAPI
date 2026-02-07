from sqlalchemy import Column,String,Integer,ForeignKey
from sqlalchemy.orm import relationship
from src.utils.database import Base

class User(Base):
    __tablename__="users"

    id=Column(Integer,primary_key=True,index=True)
    email=Column(String,unique=True,nullable=False)
    name=Column(String,nullable=False)
    phone=Column(String,nullable=False)
    hashed_password=Column(String,nullable=False)

    address=relationship("UserAddress",back_populates="user",cascade="all , delete-orphan")


class UserAddress(Base):
    __tablename__="user_address"

    id=Column(Integer,primary_key=True,index=True)
    user_id=Column(Integer,ForeignKey("users.id",ondelete="CASCADE"))
    country=Column(String,nullable=False)
    area=Column(String,nullable=False)

    user=relationship("UserAddress",back_populates="address",cascade="all , delete-orphan")