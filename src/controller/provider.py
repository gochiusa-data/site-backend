from fastapi import APIRouter
from service.provider import ProviderService
from model.response.provider import ProvidersResponse

router = APIRouter()


@router.get('/provider', response_model=ProvidersResponse)
def show_activity():
    provider = ProviderService.get_all()
    response = ProvidersResponse(items=provider) # type: ignore
    return response
