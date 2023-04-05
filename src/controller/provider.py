from fastapi import APIRouter
from model.base.database import DBsession
from model.provider.data import Provider
from model.provider.response import Providers

router = APIRouter()
database = DBsession()


@router.get("/provider", response_model=Providers)
def list_providers():
    providers = database.query(Provider).all()
    return Providers(items=providers)
