from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List, Any

from sorting.abc import ABCDataHandler


class ABCConvert(ABC):
    @abstractmethod
    def __call__(self, item: Any) -> Any:
        """Converts an item to some type

        Args:
            item (Any): item to convert
        
        Raises:
            ValueError: if item could not be converted

        Returns:
            Any: converted item
        """
        pass


class ConvertItems(ABCDataHandler):
    __slots__ = ("_convert_func",)

    def __init__(self, convert_func: ABCConvert) -> None:
        self._convert_func = convert_func

    def __call__(self, data: List[Any]) -> List[Any]:
        return [item for item in map(self._convert_func, data)]
