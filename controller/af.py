from typing import List
from fastapi import APIRouter
from fastapi import HTTPException
from model.base import DBsession
from model.af.data import Activity
from model.af.data import Endpoint
from model.af.response import Activities
from model.af.response import ActivityDetail

router = APIRouter()
database = DBsession()


@router.get('/af', response_model=Activities)
def list_af_activity():
    result = database.query(Activity).all()
    items = []
    for i in result:
        items.append(i)
    return {"items": items}


@router.get('/af/{id}', response_model=ActivityDetail)
def show_af_activity(id: int):
    result = database.query(Activity).filter(Activity.id == id).first()
    if result == None:
        raise HTTPException(404, "相关资源未找到！")
    else:
        item = {
            "id": result.id,
            "time": result.time,
            "name": result.name,
            "image": result.image,
            "description": result.description,
            "endpoint": []
        }
        result = database.query(Endpoint).filter(Endpoint.activity_id == id).all()
        for i in result:
            item["endpoint"].append(i)
        return item
