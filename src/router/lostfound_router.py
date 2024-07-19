from fastapi import FastAPI, HTTPException, APIRouter , Depends , Header
from database.database import SessionLocal
from src.model.lostfound_model import lostfound
from src.model.otp import Otp
from passlib.context import CryptContext
from src.schemas.lostfound_schemas import LostFoundData
from src.utils.otp import generate_otp,send_otp_email
from src.schemas.user_schemas import User_OTP
from src.schemas.user_schemas import OTP_Verify
from datetime import datetime
from logs.log_config import logger


lostfounds = APIRouter()
Otp_router = APIRouter()
db = SessionLocal()

pwd_context = CryptContext(schemes = ["bcrypt"] , deprecated = "auto")

@lostfounds.post("/creat_lostfound_item", response_model=LostFoundData)
def create_user_id(stu: LostFoundData):
    
    logger.info("enter lost detail")
    newUser = lostfound(
    name = stu.name,
    mobile_No = stu.mobile_No,
    email = stu.email,
    branch = stu.branch,
    item = stu.item,
    locationfound = stu.locationfound,
    description = stu.description,
    )
    logger.info("add lost detail")
    db.add(newUser)
    logger.info("commit code")
    db.commit()
    logger.success("lost detail added successfully")
    return stu


@lostfounds.get("/lost_user_details", response_model=LostFoundData)
def read_person(user_id : str):
    logger.info("chekc user id and condition")
    stu = db.query(lostfound).filter(lostfound.id == user_id, lostfound.is_active==True , lostfound.is_deleted == False).first()
    if stu is None:
        logger.error("item not found")
        raise HTTPException(status_code=404, detail="item not found")
    logger.success("detail found successfully")
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