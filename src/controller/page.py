from fastapi import APIRouter
from service.page import PageService
from model.response.page import PageResponse


router = APIRouter()


@router.get('/page/{page_id}', response_model=PageResponse)
def show_activity(page_id: int):
    page = PageService.get(page_id)
    response = PageResponse.from_orm(page)
    return response
