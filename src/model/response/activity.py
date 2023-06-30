from typing import Union
from typing import List
from model.base.response import ResponseModel
from model.response.page import PageInfoResponse


class ActivityResponse(ResponseModel):
    id: int
    name: str
    image: str
    description: Union[str, None]
    page: List[PageInfoResponse]
