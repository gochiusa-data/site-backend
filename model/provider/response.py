from typing import Union
from typing import List
from model.base import ResponseModel

class Provider(ResponseModel):
    id: int
    name: str
    url: str
