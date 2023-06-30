from fastapi import FastAPI
from controller import provider
from controller import af
from controller import ge
import os

app = FastAPI(root_path=os.environ.get("ROOT_PATH", ""))

app.include_router(provider.router)
app.include_router(af.router)
app.include_router(ge.router)
