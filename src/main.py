from fastapi import FastAPI
from fastapi import APIRouter
from controller import af
from controller import ge

app = FastAPI()
router = APIRouter(prefix="/api/beta")

router.include_router(af.router)
router.include_router(ge.router)

app.include_router(router)
