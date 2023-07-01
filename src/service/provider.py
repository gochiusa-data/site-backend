from fastapi import HTTPException
from model.base.database import DBsession
from model.data.provider import Provider

database = DBsession()


class ProviderService:
    @staticmethod
    def get(id):
        provider = database.query(Provider).filter(Provider.id == id).first()
        if provider:
            return provider
        else:
            raise HTTPException(404)
