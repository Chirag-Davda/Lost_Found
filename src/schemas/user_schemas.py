from pydantic import BaseModel
from  typing import Optional

class StuBase(BaseModel):
    user_name : str
    Mobile_No : int
    email : str
    Date_of_Birth : str
    password : str
    Gender : str

class StuBasePatch(BaseModel):
    user_name : Optional[str] = None
    Mobile_No : Optional[int] = None
    email : Optional[str] = None
    Date_of_Birth : Optional[str] = None
    password : Optional[str] = None
    Gender : Optional[str] = None


class User_OTP(BaseModel):
    email : str
    
class OTP_Verify(BaseModel):
    email : str
    otp : str