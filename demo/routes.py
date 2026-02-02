from fastapi import APIRouter
from service import get_data
router=APIRouter()

@router.get("/user")
def get_user():
    return  get_data