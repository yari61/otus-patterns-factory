from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List, Any

from sorting.abc import ABCDataHandler


class Convert(ABC):
    @abstractmethod
    def __call__(self, item: Any) -> Any:
        pass


class ConvertItems(ABCDataHandler):
    __slots__ = ("_convert_func",)

    def __init__(self, convert_func: Convert) -> None:
        self._convert_func = convert_func

    def __call__(self, data: List[str]) -> List[float]:
        converted_data = list()
        for item in data:
            converted_data.append(self._convert_func(item=item))
        return converted_data
