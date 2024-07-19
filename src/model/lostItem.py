from sqlalchemy import Column, String, Boolean, DateTime, Integer, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
import uuid
from datetime import datetime
from database.database import Base


class LostItemReports(Base):
    __tablename__ = "lost_item_report"
    id = Column(String(50), primary_key=True, default=lambda: str(uuid.uuid4()))
    user_id = Column(String(50), ForeignKey('users.id'), nullable=False)
    item_name = Column(String(50), nullable=False)
    item_description = Column(String(255), nullable=False)
    lost_date = Column(DateTime, nullable=False)
    lost_location = Column(String(100), nullable=False)
    contact_info = Column(String(100), nullable=False)
    additional_info = Column(String(255), nullable=True)
    is_deleted=Column(Boolean,default=False)
    is_active=Column(Boolean,default=True)
    is_resolved = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.now)
    modified_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)

