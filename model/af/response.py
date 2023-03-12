from typing import Union
from typing import List
from model.base import ResponseModel
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
    time: int
    image: str
    description: Union[str, None]


class Activities(ResponseModel):
    items: List[Activity]


class ActivityDetail(Activity):
    endpoint: List[Endpoint]
