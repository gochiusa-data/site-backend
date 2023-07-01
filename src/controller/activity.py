from fastapi import APIRouter
from service.activity import ActivityService
from model.response.activity import ActivityResponse


router = APIRouter()


@router.get('/activity/{activity_id}', response_model=ActivityResponse)
def show_activity(activity_id: int):
    activity = ActivityService.get(activity_id)
    response = ActivityResponse.from_orm(activity)
    return response
