from pydantic import BaseModel 
from datetime import datetime,date,time
from typing import Optional

class LostFoundData(BaseModel):
    name : str
    mobile_No : str
    email : str
    branch : str
    item : str
    locationfound : str
    description :str
    

class LostItem(BaseModel):
    user_id : str
    item_name : str
    item_description : str
    lost_date : datetime
    lost_location : str
    contact_info : str
    additional_info : str


class LostItemPatch(BaseModel):
    user_id : Optional[str] = None
    item_name : Optional[str] = None
    item_description : Optional[str] = None
    lost_date : Optional[datetime] = None
    lost_location : Optional[str] = None
    contact_info : Optional[str] = None
    additional_info : Optional[str] = None
    
