from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List, Any


class ABCOutput(ABC):
    @abstractmethod
    def write(self, data: List[Any]) -> None:
        pass
