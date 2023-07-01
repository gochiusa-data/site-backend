from fastapi import HTTPException
from model.base.database import DBsession
from model.data.page import Page

database = DBsession()


class PageService:
    @staticmethod
    def get(id):
        page = database.query(Page).filter(Page.id == id).first()
        if page:
            return page
        else:
            raise HTTPException(404)
