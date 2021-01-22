from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List, Any

from sorting.abc import ABCDataHandler


class Filter(ABC):
    @abstractmethod
    def __call__(self, item: Any) -> bool:
        pass


class FilterItems(ABCDataHandler):
    __slots__ = ("_filter_func",)

    def __init__(self, filter_func: Filter) -> None:
        self._filter_func = filter_func

    def __call__(self, data: List[str]) -> List[float]:
        filtered_data = list()
        for item in data:
            if self._filter_func(item=item):
                filtered_data.append(item)
        return filtered_data
