from fastapi import FastAPI
from controller import activity
from controller import page
from controller import provider
import os

app = FastAPI(root_path=os.environ.get("ROOT_PATH", ""))

app.include_router(activity.router)
app.include_router(page.router)
app.include_router(provider.router)
