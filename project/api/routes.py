from fastapi import APIRouter,Depends
from project.model.models import User
from sqlalchemy.orm import Session
from project.utils.dependencies import get_db
from project.api.user.service.services import create_user
from project.response.user_response import Usercreate
router=APIRouter()


@router.post("/register/")
def register(user:Usercreate,db:Session=Depends(get_db)):
    return create_user(user,db)


@router.post("/login/")
def login():
    pass


@router.post("/enter_otp/")
def enter_otp():
    pass

@router.get("/verify_otp/")
def verify_otp():
    pass

@router.get("/dashboard/")
def dashboard():
    return {"Welcome":" this is a dashboard page"}