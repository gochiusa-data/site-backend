from typing import Union
from typing import List
from datetime import datetime
from model.base.response import ResponseModel
from model.provider.response import Provider


class Endpoint(ResponseModel):
    id: int
    name: str
    provider: Provider
    url: str
    status: int


class Activity(ResponseModel):
    id: int
    name: str
    time: datetime
    image: str
    description: Union[str, None]


class Activities(ResponseModel):
    items: List[Activity]


class ActivityDetail(Activity):
    endpoint: List[Endpoint]
