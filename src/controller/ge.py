from fastapi import APIRouter
from fastapi import HTTPException
from model.base.database import DBsession
from model.data.ge import Page
from model.data.ge import Endpoint
from model.response.ge import Pages
from model.response.ge import PageDetail

router = APIRouter()
database = DBsession()


@router.get("/ge", response_model=Pages)
def list_ge_pages():
    pages = database.query(Page).all()
    return Pages(items=pages) # type: ignore


@router.get("/ge/{page_id}", response_model=PageDetail)
def show_ge_page(page_id):
    page = database.query(Page).filter(Page.id == page_id).first()
    if page:
        endpoint = database.query(Endpoint).filter(Endpoint.page_id == page_id).all()
        page.endpoint = endpoint
        return page
    else:
        raise HTTPException(404)
