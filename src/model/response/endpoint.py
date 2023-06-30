from typing import List
from model.base.response import ResponseModel
from model.response.provider import ProviderInfo


class EndpointResponse(ResponseModel):
    id: int
    name: str
    url: str
    status: int
    provider: ProviderInfo
