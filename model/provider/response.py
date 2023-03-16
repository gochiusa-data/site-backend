from typing import List
from model.base.response import ResponseModel

class Provider(ResponseModel):
    id: int
    name: str
    url: str
