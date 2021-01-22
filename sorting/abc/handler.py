from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List, Any


class ABCDataHandler(ABC):
    @abstractmethod
    def __call__(self, data: List[Any]) -> List[Any]:
        pass
