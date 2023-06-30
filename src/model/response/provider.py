from typing import List
from model.base.response import ResponseModel

class Provider(ResponseModel):
    id: int
    name: str
    url: str


class ProviderDetail(Provider):
    avatar: str
    description: str


class Providers(ResponseModel):
    items: List[ProviderDetail]
