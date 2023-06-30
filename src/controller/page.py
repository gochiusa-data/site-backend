from fastapi import APIRouter
from service.page import PageService
from model.response.page import PageResponse


router = APIRouter()


@router.get('/page/{page_id}', response_model=PageResponse)
def show_activity(page_id: int):
    activity = PageService.get_by_id(page_id)
    return page_id
