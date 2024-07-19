from fastapi import FastAPI, HTTPException, APIRouter , Depends , Header
from database.database import SessionLocal
from src.model.lostItem import LostItemReports
from src.model.otp import Otp
from passlib.context import CryptContext
from src.schemas.lostfound_schemas import LostFoundData,LostItem,LostItemPatch
from src.utils.otp import generate_otp,send_otp_email
from src.schemas.user_schemas import User_OTP
from src.schemas.user_schemas import OTP_Verify
from datetime import datetime




Lost_Item_Report = APIRouter()
Otp_router = APIRouter()
db = SessionLocal()

pwd_context = CryptContext(schemes = ["bcrypt"] , deprecated = "auto")

@Lost_Item_Report.post("/create_Lostreportuser_id", response_model=LostItem)
def create_Lostreportuser_id(stu: LostItem):
    newUser = LostItemReports(
    
    user_id = stu.user_id,
    item_name = stu.item_name,
    item_description = stu.item_description,
    lost_date = stu.lost_date,
    lost_location = stu.lost_location,
    contact_info = stu.contact_info,
    additional_info = stu.additional_info,

 
    )
    db.add(newUser)
    db.commit()
    return newUser



@Lost_Item_Report.get("/lost_Item_details", response_model=LostItem)
def lost_Item_details(user_id : str):
    stu = db.query(LostItemReports).filter(LostItemReports.id == user_id, LostItemReports.is_active==True , LostItemReports.is_deleted == False).first()
    if stu is None:
        raise HTTPException(status_code=404, detail="item not found")
    return stu

@Lost_Item_Report.get("/all_Item_detail",response_model=list[LostItem])
def all_Item_detail():
    stu=db.query(LostItemReports).filter(LostItemReports.is_active == True,).all()
    if stu is None :
        raise HTTPException (status_code=404,detail="User Not Found")
    return stu


@Lost_Item_Report.put("/update_lost_details")
def update_user_data(lost: LostItem, lost_id : str):
    breakpoint()
    db_user = db.query(LostItemReports).filter(LostItemReports.id == lost_id, LostItemReports.is_active == True).first()
    if db_user is None:
        raise HTTPException(status_code=404, detail="User Not Found!!!!")
    
    db_user.user_id = lost.user_id,
    db_user.item_name =lost.item_name,
    db_user.item_description =lost.item_description,
    db_user.lost_date =lost.lost_date,
    db_user.lost_location =lost.lost_location,
    db_user.contact_info =lost.contact_info,
    db_user.additional_info =lost.additional_info,
    
    
    db.commit()
    return "Your Detail Changed Successfully!!!!!!!!!!!"

@Lost_Item_Report.patch("/update_lost_detail")
def update_catering(updateevent:LostItemPatch,lost_id : str):
    # logger.info("decode id token")
    db_lost = db.query(LostItemReports).filter(LostItemReports.id == lost_id,LostItemReports.is_active == True,LostItemReports.is_deleted == False).first()
    if db_lost is None:
        # logger.error("logistic id not found")
        raise HTTPException(status_code=404, detail="lost id is not found")
    update_data = updateevent.dict(exclude_unset = True)
    for key,value in update_data.items():
        # logger.info("change specific detail")
        setattr(db_lost, key, value)
    db.commit()
    db.refresh(db_lost)
    # logger.success("detail change successfully")
    return{"message":"details changes successfully","User": db_lost}


# Delete a lost item report
@Lost_Item_Report.delete("/delete_lost_item_report", response_model=LostItem)
def delete_lost_item_report(report_id: str):
    db_report = db.query(LostItemReports).filter(LostItemReports.id == report_id).first()
    if db_report is None:
        raise HTTPException(status_code=404, detail="Report not found")
    
    db.delete(db_report)
    db.commit()
    return db_report