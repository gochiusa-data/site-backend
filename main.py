from fastapi import FastAPI
from fastapi import APIRouter
from controller import af

router = APIRouter(prefix="/api/beta")

router.include_router(af.router)

app = FastAPI()
app.include_router(router)
