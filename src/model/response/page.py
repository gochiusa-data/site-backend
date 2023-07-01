from typing import Union
from typing import List
from datetime import datetime
from model.base.response import ResponseModel
from model.response.endpoint import EndpointResponse


class PageResponse(ResponseModel):
    id: int
    name: str
    time: datetime
    image: str
    description: Union[str, None]
    endpoint: List[EndpointResponse]


class PageInfoResponse(ResponseModel):
    id: int
    name: str
    image: str
