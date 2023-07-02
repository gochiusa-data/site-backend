from typing import List
from typing import TypeVar
from typing import Generic
from model.base.response import ResponseModel

T = TypeVar('T')


class ItemsResponse(ResponseModel, Generic[T]):
    items: List[T]
