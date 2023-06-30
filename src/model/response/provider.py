from typing import List
from model.base.response import ResponseModel


class Provider(ResponseModel):
    id: int
    name: str
    avatar: str
    url: str
    description: str


class ProviderInfo(Provider):
    id: int
    name: str
