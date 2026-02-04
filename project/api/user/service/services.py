from fastapi import Depends,HTTPException,status
from sqlalchemy.orm import Session
from project.model.models import User
from project.utils.dependencies import get_db
from project.utils.security import hash_password


def  create_user(user,db):
    exist_user=db.query(User).filter(User.email==user.email).first()
    if exist_user:
        raise HTTPException(status_code=400,detail="user already exists")
    new_user=User(
        name=user.name,
        email=user.email,
        hashed_password=hash_password(user.password)
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return {"message":"stroed"}