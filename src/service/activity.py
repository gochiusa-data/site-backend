from fastapi import HTTPException
from model.base.database import DBsession
from model.data.activity import Activity

database = DBsession()


class ActivityService:
    @staticmethod
    def get_by_id(id):
        activity = database.query(Activity).filter(Activity.id == id).first()
        if activity:
            return activity
        else:
            raise HTTPException(404)
