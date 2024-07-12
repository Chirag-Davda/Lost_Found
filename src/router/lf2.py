from fastapi import FastAPI, HTTPException, APIRouter , Depends , Header
from database.database import SessionLocal
from src.model.lf import lostfound
from src.model.otp import Otp
from passlib.context import CryptContext
from src.schemas.lf1 import LostFoundData
from src.utils.otp import generate_otp,send_otp_email
from src.schemas.user1 import User_OTP
from src.schemas.user1 import OTP_Verify
from datetime import datetime

lostfounds = APIRouter()
Otp_router = APIRouter()
db = SessionLocal()

pwd_context = CryptContext(schemes = ["bcrypt"] , deprecated = "auto")

@lostfounds.post("/create_user_id", response_model=LostFoundData)
def create_user_id(stu: LostFoundData):
    newUser = lostfound(
    
    name = stu.name,
    mobile_No = stu.mobile_No,
    email = stu.email,
    branch = stu.branch,
    item = stu.item,
    locationfound = stu.locationfound,
    description = stu.description,

 
    )
    db.add(newUser)
    db.commit()
    return stu


@lostfounds.get("/lost_user_details", response_model=LostFoundData)
def read_person(user_id : str):
    stu = db.query(lostfound).filter(lostfound.id == user_id, lostfound.is_active==True , lostfound.is_deleted == False).first()
    if stu is None:
        raise HTTPException(status_code=404, detail="item not found")
    return stu

@lostfounds.get("/lostdetail",response_model=list[LostFoundData])
def all_lostdetail():
    stu=db.query(lostfound).filter(lostfound.is_active == True,lostfound.is_verified == True).all()
    if stu is None :
        raise HTTPException (status_code=404,detail="User Not Found")
    return stu


@lostfounds.put("/update_lost_detail")
def update_user_data(user: LostFoundData, lost_id : str):
    # breakpoint()
    db_user = db.query(lostfound).filter(lostfound.id == lost_id, lostfound.is_active == True, lostfound.is_verified == True).first()
    if db_user is None:
        raise HTTPException(status_code=404, detail="User Not Found!!!!")
    
    db_user.name = user.name,
    db_user.email =user.email,
    db_user.mobile_No =user.mobile_No,
    db_user.branch =user.branch,
    db_user.item =user.item,
    db_user.locationfound =user.locationfound,
    db_user.description =user.description,
    
    
    db.commit()
    return "Your Detail Changed Successfully!!!!!!!!!!!"