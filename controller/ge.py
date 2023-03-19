from fastapi import APIRouter
from fastapi import HTTPException
from model.base.database import DBsession
from model.ge.data import Page
from model.ge.data import Endpoint
from model.ge.response import Pages
from model.ge.response import PageDetail

router = APIRouter()
database = DBsession()


@router.get("/ge", response_model=Pages)
def list_ge_pages():
    pages = database.query(Page).all()
    return Pages(items=pages)


@router.get("/ge/{id}", response_model=PageDetail)
def show_ge_page(id):
    page = database.query(Page).filter(Page.id == id).first()
    if page:
        endpoint = database.query(Endpoint).filter(Endpoint.page_id == id).all()
        page.endpoint = endpoint
        return page
    else:
        raise HTTPException(404)
