from fastapi import HTTPException
from model.base.database import DBsession
from model.data.provider import Provider

database = DBsession()


class ProviderService:
    @staticmethod
    def get_all():
        provider = database.query(Provider).all()
        return provider
