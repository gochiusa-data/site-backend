from typing import List
from typing import Any
from pydantic import create_model


class ItemsResponse:
    @staticmethod
    def create(model):
        return create_model("ItemsResponse", items = (List[model], ...))
