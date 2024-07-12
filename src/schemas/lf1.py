from pydantic import BaseModel 

class LostFoundData(BaseModel):
    name : str
    mobile_No : int
    email : str
    branch : str
    item : str
    locationfound : str
    description :str
    

