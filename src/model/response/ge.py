from typing import Union
from typing import List
from model.base.response import ResponseModel
from model.response.provider import Provider


class Endpoint(ResponseModel):
    id: int
    name: str
    provider: Provider
    url: str
    status: int


class Page(ResponseModel):
    id: int
    name: str
    image: str
    description: Union[str, None]


class Pages(ResponseModel):
    items: List[Page]


class PageDetail(Page):
    endpoint: List[Endpoint]
