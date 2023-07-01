from fastapi import APIRouter
from service.provider import ProviderService
from model.response.provider import ProviderResponse
from model.response.item import ItemsResponse

router = APIRouter()


@router.get('/provider', response_model=ItemsResponse)
def show_activity():
    provider = ProviderService.get_all()
    response = ItemsResponse(items=provider)
    return response
