from fastapi import FastAPI,APIRouter
from src.router.user_router import User1
from src.router.lostfound_router import lostfounds
from src.router.user_router import Otp_router
from src.router.LostItemReport_router import Lost_Item_Report

app = FastAPI()
app.include_router(User1)
app.include_router(lostfounds)
app.include_router(Otp_router)
app.include_router(Lost_Item_Report)