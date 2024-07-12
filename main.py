from fastapi import FastAPI,APIRouter
from src.router.user3 import User1
from src.router.lf2 import lostfounds
from src.router.user3 import Otp_router


app = FastAPI()
app.include_router(User1)
app.include_router(lostfounds)
app.include_router(Otp_router)