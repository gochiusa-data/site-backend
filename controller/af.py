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
def list_af_activities():
    activities = database.query(Activity).all()
    return Activities(items=activities)


@router.get('/af/{activity_id}', response_model=ActivityDetail)
def show_af_activity(activity_id: int):
    activity = database.query(Activity).filter(Activity.id == activity_id).first()
    if activity:
        endpoint = database.query(Endpoint).filter(Endpoint.activity_id == activity_id).all()
        activity.endpoint = endpoint
        return activity
    else:
        raise HTTPException(404)
