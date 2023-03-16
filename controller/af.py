from fastapi import APIRouter
from fastapi import HTTPException
from model.base.database import DBsession
from model.af.data import Activity
from model.af.data import Endpoint
from model.af.response import Activities
from model.af.response import ActivityDetail

router = APIRouter()
database = DBsession()


@router.get('/af', response_model=Activities)
def list_af_activity():
    activities = database.query(Activity).all()
    return Activities(items=activities)


@router.get('/af/{id}', response_model=ActivityDetail)
def show_af_activity(id: int):
    activity = database.query(Activity).filter(Activity.id == id).first()
    if activity:
        endpoint = database.query(Endpoint).filter(Endpoint.activity_id == id).all()
        return ActivityDetail(
            id=activity.id,
            name=activity.name,
            time=activity.time,
            image=activity.image,
            description=activity.description,
            endpoint=endpoint
        )
    else:
        raise HTTPException(404, "相关资源未找到！")
