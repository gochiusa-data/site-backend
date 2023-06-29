from typing import Union
from typing import List
from datetime import datetime
from model.base.response import ResponseModel
from model.response.provider import Provider


class Endpoint(ResponseModel):
    id: int
    name: str
    provider: Provider
    url: str
    status: int


class Activity(ResponseModel):
    id: int
    name: str
    image: str
    description: Union[str, None]


class Activities(ResponseModel):
    items: List[Activity]


class ActivityDetail(Activity):
    time: datetime
    endpoint: List[Endpoint]
