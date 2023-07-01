from typing import List
from typing import Any
from model.base.response import ResponseModel


class ItemsResponse(ResponseModel):
    items: List[Any]
