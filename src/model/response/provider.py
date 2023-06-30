from typing import List
from model.base.response import ResponseModel


class ProviderResponse(ResponseModel):
    id: int
    name: str
    avatar: str
    url: str
    description: str


class ProviderInfo(ResponseModel):
    id: int
    name: str
