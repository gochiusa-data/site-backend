from typing import Union
from typing import List
from datetime import datetime
from model.base.response import ResponseModel
from model.response.endpoint import Endpoint


class Page(ResponseModel):
    id: int
    name: str
    time: datetime
    image: str
    description: Union[str, None]
    endpoint: List[Endpoint]


class PageInfo(ResponseModel):
    id: int
    name: str
    image: str
