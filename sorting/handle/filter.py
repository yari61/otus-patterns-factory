from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List, Any

from sorting.abc import ABCDataHandler


class ABCFilter(ABC):
    @abstractmethod
    def __call__(self, item: Any) -> bool:
        """Checks if item should be filtered out

        Args:
            item (Any): item to check
        
        Raises:
            ValueError: if item could not be checked

        Returns:
            bool: True if item fits to filter, False if item should be filtered out
        """
        pass


class FilterItems(ABCDataHandler):
    __slots__ = ("_filter_func",)

    def __init__(self, filter_func: ABCFilter) -> None:
        self._filter_func = filter_func

    def __call__(self, data: List[Any]) -> List[Any]:
        return [item for item in filter(self._filter_func, data)]
