from sqlalchemy import Column,Integer,String,Boolean,DateTime
from database.database import Base
from datetime import datetime
import uuid

class lostfound(Base):
    __tablename__ = "Lost_found"
    id = Column(String(50), primary_key=True, default=str(uuid.uuid4()))
    name = Column(String(20),nullable=False)
    mobile_No = Column(String(10),nullable=False)
    email = Column(String(30),nullable=False)
    branch = Column(String(30),nullable=False)
    item = Column(String(50),nullable=False)
    locationfound = Column(String(50),nullable=False)
    description = Column(String(50),nullable=False)
 
    is_deleted=Column(Boolean,default=False)
    is_active=Column(Boolean,default=True)
    created_at=Column(DateTime,default=datetime.now)
    modified_at=Column(DateTime,default=datetime.now,onupdate=datetime.now)